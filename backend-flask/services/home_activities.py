from datetime import datetime, timedelta, timezone
from opentelemetry import trace
import logging
from time import strftime

from lib.db import db

#tracer = trace.get_tracer("home.activities")

class HomeActivities:
  # def run():
  def run(cognito_user_id=None):    
  # def run(logger):  
  #   logger.info("Incoming logs from /api/activities/home")
    # with tracer.start_as_current_span("home-activites-mock-data"):
    #   span = trace.get_current_span()
    #   now = datetime.now(timezone.utc).astimezone()
    #   span.set_attribute("app.now", now.isoformat())
    sql = db.template('activities','home')
    results = db.query_array_json(sql)
    return results