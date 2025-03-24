from flask import jsonify, abort
from flask_restful import Resource, reqparse
from data.db_session import create_session
from data.users import User

parser = reqparse.RequestParser()
parser.add_argument('surname', required=False)
parser.add_argument('name', required=False)
parser.add_argument('age', required=False, type=int)
parser.add_argument('position', required=False)
parser.add_argument('speciality', required=False)
parser.add_argument('address', required=False)
parser.add_argument('email', required=False)
parser.add_argument('hashed_password', required=False)


class UserResourse(Resource):
    def get(self, user_id):
        sess = create_session()
        user = sess.query(User).filter(User.id == user_id).first()
        if not user:
            abort(404, 'not found')
        return jsonify(user.to_dict(
            only=('id', 'surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'hashed_password')))

    def delete(self, user_id):
        sess = create_session()
        user = sess.query(User).filter(User.id == user_id).first()
        if not user:
            abort(404, 'not found')
        sess.delete(user)
        sess.commit()
        return jsonify({'status': 'ok'})


class UserListResourse(Resource):
    def get(self):
        sess = create_session()
        users = sess.query(User).all()
        return jsonify([
            user.to_dict(only=(
                'id', 'team_leader', 'collaborators', 'job', 'work_size', 'start_date', 'end_date', 'is_finished')) for
            user
            in users
        ])

    def post(self):
        args = parser.parse_args()
        sess = create_session()
        user = User(
            surname=args['surname'],
            name=args['name'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            email=args['email'],
            hashed_password=args['hashed_password']
        )
        sess.add(user)
        sess.commit()
        return jsonify({'user_id': user.id})
