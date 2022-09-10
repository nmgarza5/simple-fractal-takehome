from flask import Blueprint
from app.models import Record
from .helpers import calculate_percentiles, find_similar_candidates

percentile_routes = Blueprint('percentile', __name__)

@percentile_routes.route('/<int:id>', methods=["GET"])
def calculate__candidate_percentile(id):
  try:
  #   get candidate record
    candidate_record = Record.query.filter(Record.candidate_id == (id)).first().to_dict()

  # obtain records of all candidates who are similar (simialr company and same position)
    similar_candidates = find_similar_candidates(candidate_record)

  # calculate coding and communication percentiles
    percentiles = calculate_percentiles(similar_candidates, candidate_record)

    return {
      'candidate': candidate_record,
      'comms_percentile': percentiles['comms_percentile'],
      'coding_percentile': percentiles['coding_percentile'],
      }

  except:
    return {'errors': 'The requested Candidate ID could not be found. Please try again.'}, 404
