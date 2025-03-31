from flask import Blueprint, jsonify, request, make_response
from data import db_session
from data.jobs import Jobs

blueprint = Blueprint('jobs_api', __name__, template_folder='templates')


@blueprint.route('/api/jobs')
def get_jobs():
    sess = db_session.create_session()
    jobs_list = sess.query(Jobs).all()
    return jsonify({
        'jobs': [job.to_dict(only=('id', 'team_leader', 'collaborators', 'job', 'work_size', 'start_date', 'end_date', 'is_finished')) for job in jobs_list]
    })


@blueprint.route('/api/jobs/<int:id>')
def get_jobs_id(id):
    sess = db_session.create_session()
    jobs_list = sess.query(Jobs).filter(Jobs.id == id).first()
    if not jobs_list:
        return jsonify({'status': 404})
    return jsonify({
        'job': jobs_list.to_dict(
            only=('id', 'team_leader', 'collaborators', 'job', 'work_size', 'start_date', 'end_date', 'is_finished'))
    })


@blueprint.route('/api/jobs', methods=['POST'])
def create_job():
    if not request.json():
        return make_response(jsonify({'error': 'Bad request'}), 400)
    column = ['team_leader', 'job', 'collaborators', 'is_finished', 'work_size']
    if not all([key in column for key in request.json]):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    sess = db_session.create_session()
    jobs = Jobs()
    jobs.team_leader = request.json['team_leader']
    jobs.collaborators = request.json['collaborators']
    jobs.is_finished = request.json['is_finished']
    jobs.work_size = request.json['work_size']
    jobs.job = request.json['job']
    sess.add(jobs)
    sess.commit()
    return jsonify({'jobs.id': jobs.id})
