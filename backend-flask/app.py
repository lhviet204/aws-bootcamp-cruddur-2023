from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
# Uncomment if using jwt validation from BE
# from lib.cognito_jwt_token import CognitoJwtToken, TokenVerifyError, extract_access_token

# # AWS CloudWatch Log  
# import watchtower
# import logging

# ROLLBAR libs
import os
import rollbar.contrib.flask
from flask import got_request_exception
from time import strftime
from flask import got_request_exception

# # XRAY libs
# from aws_xray_sdk.core import xray_recorder
# from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

from services.home_activities import *
from services.notifications_activities import *
from services.user_activities import *
from services.create_activity import *
from services.create_reply import *
from services.search_activities import *
from services.message_groups import *
from services.messages import *
from services.create_message import *
from services.show_activity import *

# HONEYCOMB libs
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

# Initialize tracing and an exporter that can send data to Honeycomb
provider = TracerProvider()
processor = BatchSpanProcessor(OTLPSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)

# to send logs to console on BE flask by STDOUT 
simple_processor = SimpleSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(simple_processor)

# Initialize automatic instrumentation with Flask
app = Flask(__name__)

# Uncomment if using validation from BE
# cognito_jwt_token = CognitoJwtToken(
#   user_pool_id=os.getenv("REACT_APP_AWS_USER_POOLS_ID"), 
#   user_pool_client_id=os.getenv("REACT_APP_CLIENT_ID"),
#   region=os.getenv("AWS_DEFAULT_REGION")
# )

FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

# Initialize XRAY
# xray_url = os.getenv("AWS_XRAY_URL")
# xray_recorder.configure(service='cruddur-be-flask', dynamic_naming=xray_url)
# XRayMiddleware(app, xray_recorder)

#Configure Logger to send log to Cloud Watch
# LOGGER = logging.getLogger(__name__)
# LOGGER.setLevel(logging.DEBUG)
# console_handler = logging.StreamHandler()
# cw_handler = watchtower.CloudWatchLogHandler(log_group='cruddur')
# LOGGER.addHandler(console_handler)
# LOGGER.addHandler(cw_handler)
# LOGGER.info("test log")

frontend = os.getenv('FRONTEND_URL')
backend = os.getenv('BACKEND_URL')
envoy = os.getenv('ENVOY_URL')
origins = [frontend, backend, envoy]
cors = CORS(
  app,
  resources={r"/api/*": {"origins": origins}},
  expose_headers=["Authorization"],
  allow_headers=["Content-Type", "if-modified-since", "traceparent", "Authorization", 'x-cognito-username'],
  methods="OPTIONS,GET,HEAD,POST"
)


rollbar_access_token = os.getenv('ROLLBAR_ACCESS_TOKEN')

@app.before_first_request
def init_rollbar():
    """init rollbar module"""
    rollbar.init(rollbar_access_token,
        'production',
        root=os.path.dirname(os.path.realpath(__file__)),
        allow_logging_basic_config=False)
    # send exceptions from `app` to rollbar, using flask's signal system.
    got_request_exception.connect(rollbar.contrib.flask.report_exception, app)

# #Logger to log any after
# @app.after_request
# def after_request(response):
#    timestamp = strftime('[%Y-%b-%d %H:%M]')
#    LOGGER.error('%s %s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status)
#    return response

@app.route("/api/message_groups", methods=['GET'])
def data_message_groups():
  user_handle  = 'andrewbrown'
  model = MessageGroups.run(user_handle=user_handle)
  if model['errors'] is not None:
    return model['errors'], 422
  else:
    return model['data'], 200

@app.route("/api/messages/@<string:handle>", methods=['GET'])
def data_messages(handle):
  user_sender_handle = 'andrewbrown'
  user_receiver_handle = request.args.get('user_reciever_handle')

  model = Messages.run(user_sender_handle=user_sender_handle, user_receiver_handle=user_receiver_handle)
  if model['errors'] is not None:
    return model['errors'], 422
  else:
    return model['data'], 200
  return

@app.route("/api/messages", methods=['POST','OPTIONS'])
def data_create_message():
  user_sender_handle = 'andrewbrown'
  user_receiver_handle = request.json['user_receiver_handle']
  message = request.json['message']

  model = CreateMessage.run(message=message,user_sender_handle=user_sender_handle,user_receiver_handle=user_receiver_handle)
  if model['errors'] is not None:
    return model['errors'], 422
  else:
    return model['data'], 200
  return

@app.route("/api/activities/home", methods=['GET'])
# @xray_recorder.capture('activities_home')
def data_home():
  # # data = HomeActivities.run(LOGGER)
  # access_token = extract_access_token(request.headers)
  # try:
  #   claims = cognito_jwt_token.verify(access_token)
  #   # authenicatied request
  #   app.logger.debug("authenicated")
  #   app.logger.debug(claims)
  #   app.logger.debug(claims['username'])
  #   data = HomeActivities.run(cognito_user_id=claims['username'])
  # except TokenVerifyError as e:
  #   # unauthenicatied request
  #   app.logger.debug(e)
  #   app.logger.debug("unauthenicated")
  #   data = HomeActivities.run()
  # return data, 200

  ## For aws-jwt-verify
  app.logger.debug(request.headers)
  cognito_usr = request.headers.get("x-cognito-username", None)
  if cognito_usr is not None:
    app.logger.debug(f"Authenticated request from {cognito_usr}")
    data = HomeActivities.run(cognito_user_id=cognito_usr)
  else:
    data = HomeActivities.run()
  return data, 200  

@app.route("/api/activities/notifications", methods=['GET'])
@cross_origin()
def data_notifications():
  data = NotificationsActivities.run()
  return data, 200

@app.route("/api/activities/@<string:handle>", methods=['GET'])
@cross_origin()
@xray_recorder.capture('activities_user')
def data_handle(handle):
  model = UserActivities.run(handle)
  if model['errors'] is not None:
    return model['errors'], 422
  else:
    return model['data'], 200

@app.route("/api/activities/search", methods=['GET'])
@cross_origin()
def data_search():
  term = request.args.get('term')
  model = SearchActivities.run(term)
  if model['errors'] is not None:
    return model['errors'], 422
  else:
    return model['data'], 200
  return

@app.route("/api/activities", methods=['POST','OPTIONS'])
@cross_origin()
def data_activities():
  user_handle  = 'andrewbrown'
  message = request.json['message']
  ttl = request.json['ttl']
  model = CreateActivity.run(message, user_handle, ttl)
  if model['errors'] is not None:
    return model['errors'], 422
  else:
    return model['data'], 200
  return

@app.route("/api/activities/<string:activity_uuid>", methods=['GET'])
@cross_origin()
# @xray_recorder.capture('activities_show')
def data_show_activity(activity_uuid):
  data = ShowActivity.run(activity_uuid=activity_uuid)
  return data, 200

@app.route("/api/activities/<string:activity_uuid>/reply", methods=['POST','OPTIONS'])
@cross_origin()
def data_activities_reply(activity_uuid):
  user_handle  = 'andrewbrown'
  message = request.json['message']
  model = CreateReply.run(message, user_handle, activity_uuid)
  if model['errors'] is not None:
    return model['errors'], 422
  else:
    return model['data'], 200
  return

# For RollBar endpoint
@app.route('/rollbar/test')
@cross_origin()
def rollbar_test():
    rollbar.report_message('Hello Andrew and friends', 'warning')
    return "Hello Andrew and friends!"

if __name__ == "__main__":
  app.run(debug=True)