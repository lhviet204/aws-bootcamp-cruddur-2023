from flask import request, g
from aws_xray_sdk.core import xray_recorder
from lib.cognito_jwt_token import jwt_required
from flask_cors import cross_origin

from services.message_groups import MessageGroups
from services.messages import Messages
from services.create_message import CreateMessage

from lib.helpers import model_json

def load(app):
    @app.route("/api/message_groups", methods=['GET'])
    @jwt_required()
    def data_message_groups():
        model = MessageGroups.run(cognito_user_id=g.cognito_user_id)
        return model_json(model)

    @app.route("/api/messages/<string:message_group_uuid>", methods=['GET'])
    @jwt_required()
    def data_messages(message_group_uuid):
        model = Messages.run(
            cognito_user_id=g.cognito_user_id,
            message_group_uuid=message_group_uuid
            )
        return model_json(model)

    @app.route("/api/messages", methods=['POST','OPTIONS'])
    @cross_origin()
    @jwt_required()
    def data_create_message():
        message_group_uuid   = request.json.get('message_group_uuid',None)
        user_receiver_handle = request.json.get('handle',None)
        message = request.json['message']
        if message_group_uuid == None:
            # Create message for the first time if group uuid is not avaiable
            model = CreateMessage.run(
                mode="create",
                message=message,
                cognito_user_id=g.cognito_user_id,
                user_receiver_handle=user_receiver_handle
            )
        else:
            # Push message onto existing Message Group based on group uuid
            model = CreateMessage.run(
                mode="update",
                message=message,
                message_group_uuid=message_group_uuid,
                cognito_user_id=g.cognito_user_id
            )
        return model_json(model)