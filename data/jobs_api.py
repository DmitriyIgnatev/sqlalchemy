import request

import flask
from flask import jsonify

from . import db_session
from .jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)

# @blueprint.route('/api/jobs')
# def get_news():
#     db_sess = db_session.create_session()
#     jobs = db_sess.query(Jobs).all()
#     return jsonify(
#         {
#             'jobs':
#                 [item.to_dict(only=('id', 'team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'is_finished'))
#                  for item in jobs]
#         }
#     )

# @blueprint.route('/api/jobs/<int:job_id>')
# def get_news(job_id):
#     db_sess = db_session.create_session()
#     jobs = db_sess.query(Jobs).get(job_id)
#     if not jobs:
#         return jsonify({'error': 'Not found'})
#     return jsonify(
#         {
#             'jobs': jobs.to_dict(only=(
#                 'id', 'team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'is_finished'))
#         }
#     )

@blueprint.route('/api/jobs', methods=['POST'])
def create_jobs():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id', 'team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'is_finished']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    jobs = Jobs(
        id=request.json['id'],
        team_leader=request.json['team_leader'],
        job=request.json['job'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        start_date=request.json['start_date'],
        is_finished=request.json['is_finished'],
    )
    db_sess.add(jobs)
    db_sess.commit()
    return jsonify({'success': 'OK'})