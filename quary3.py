from data.users import User
from data import db_session

db_session.global_init(input())
session = db_session.create_session()

users = session.query(User).filter(User.address == 'module_1', User.speciality.notlike('%engineer%'),
                                   User.position.notlike('%engineer%')).all()
for user in users:
    print(user.id)

#database/mars_exploer.db
#select * grom user