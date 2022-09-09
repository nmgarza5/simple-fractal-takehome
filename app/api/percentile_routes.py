from flask import Blueprint, jsonify, session, request
from app.models import Company, Record, db
import math
from scipy import stats

percentile_routes = Blueprint('percentile', __name__)

def are_similar(company_1_FI, company_2_FI):
    similar = math.fabs(company_1_FI['fractal_index'] - company_2_FI['fractal_index']) < 0.15
    return similar

# returns a set with the IDs of all canidates who are similar
def find_similar_candidates(candidate_record):
  all_companies = Company.query.all()
  similar_candidates = set()
  for ele in all_companies:
    company = ele.to_dict()
    if are_similar(company, candidate_record['company']):
        records = company['score_records']
        for record in records.values():
            if record['title'] == candidate_record['title']:
              similar_candidates.add(record['id'])
  return similar_candidates


# return the a dictionary containing the specified candidate's coding and communication percentiles
def calculatePercentiles(similar_candidates, candidate_record):
  candidate_coding_score = candidate_record['coding_score']
  candidate_communication_score = candidate_record['communication_score']
  all_records = Record.query.all()
  # find the coding/comms scores for all similar canidates
  similar_candidates_coding = [record.to_dict()['coding_score'] for record in all_records if record.to_dict()['id'] in similar_candidates]
  similar_candidates_comms = [record.to_dict()['communication_score'] for record in all_records if record.to_dict()['id'] in similar_candidates]
  comms_percentile = round(stats.percentileofscore(similar_candidates_comms, candidate_communication_score), 2)
  coding_percentile = round(stats.percentileofscore(similar_candidates_coding, candidate_coding_score), 2)
  return {'comms_percentile': comms_percentile, 'coding_percentile': coding_percentile}


@percentile_routes.route('/<int:id>', methods=["GET"])
def calculate__candidate_percentile(id):
  try:
  #   get candidate record
    candidate_records = Record.query.filter(Record.candidate_id == (id))
    candidate_record = None
    for record in candidate_records:
      candidate_record = record.to_dict()
  # obtain records of all candidates who are similar (simialr company and same position)
    similar_candidates = find_similar_candidates(candidate_record)
  # calculate coding and communication percentiles
    percentiles = calculatePercentiles(similar_candidates, candidate_record)
    return {
      'candidate': candidate_record,
      'comms_percentile': percentiles['comms_percentile'],
      'coding_percentile': percentiles['coding_percentile'],
      }
  except:
    return {'errors': 'The requested Candidate ID could not be found. Please try again.'}, 404
