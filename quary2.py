from data.jobs import Jobs
from data import db_session
import datetime


db_session.global_init('database/mars_exploer.db')
session = db_session.create_session()

capitan = Jobs()
capitan.team_leader =  1
capitan.job = 'deployment of residential modules 1 and 2'
capitan.work_size =  15
capitan.collaborators =  '2, 3'
capitan.start_date = datetime.datetime.now()
capitan.is_finished = False

session.add(capitan)
session.commit()

