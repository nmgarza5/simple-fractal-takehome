from flask import Blueprint, jsonify, session, request
from app.models import Company, Record, db


percentile_routes = Blueprint('percentile', __name__)


def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{field} : {error}')
    return errorMessages


# # Definitions
# - communication_score: a measurement of the candidate's ability to communicate
# - coding_score: a measurement of the candidate's technical ability
# - title: the role that the candidate performs at their company, e.g. Senior Engineer
# - similar companies: A similar company is any company who's absolute difference of fractal_index is less than .15. A company is similar to itself.

@percentile_routes.route('/', methods=["GET"])
def get_scores():
  all_records = Record.query.all()
  return {record.id: record.to_dict() for record in all_records}


@percentile_routes.route('/', methods=["GET"])
def calculate_percentile(candidate_id):
  all_records = Record.query.all()

  candidate_records = Record.query.query.filter(Record.candidate_id == (candidate_id))



  return {record.id: record.to_dict() for record in candidate_records}
