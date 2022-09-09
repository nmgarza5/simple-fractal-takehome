from flask import Blueprint, jsonify, session, request
from app.models import Company, Record, db
import math
from scipy import stats



percentile_routes = Blueprint('percentile', __name__)


def are_similar(company_1_FI, company_2_FI):
    similar = math.fabs(company_1_FI['fractal_index'] - company_2_FI['fractal_index']) < 0.15
    return similar


@percentile_routes.route('/<int:id>', methods=["GET"])
def calculate__candidate_percentile(id):


  try:

  #   get candidate record
    candidate_records = Record.query.filter(Record.candidate_id == (id))
    candidate_record = None
    for record in candidate_records:
      candidate_record = record.to_dict()

  # candidate info
    candidate_company = candidate_record['company']
    candidate_title = candidate_record['title']
    candidate_coding_score = candidate_record['coding_score']
    candidate_communication_score = candidate_record['communication_score']

  # get similar companies
    all_companies = Company.query.all()
    # similar_companies = []

    similar_candidates = set()
    for ele in all_companies:
      company = ele.to_dict()
      if are_similar(company, candidate_company):
          records = company['score_records']
          for record in records.values():
              if record['title'] == candidate_title:
                similar_candidates.add(record['id'])

    all_records = Record.query.all()
    similar_candidates_coding = []
    similar_candidates_comms = []
    for record in all_records:
      dict = record.to_dict()
      if dict['id'] in similar_candidates:
        similar_candidates_coding.append(dict['coding_score'])
        similar_candidates_comms.append(dict['communication_score'])

  #   get percentiles
    comms_percentile = round(stats.percentileofscore(similar_candidates_comms, candidate_communication_score), 2)
    coding_percentile = round(stats.percentileofscore(similar_candidates_coding, candidate_coding_score), 2)


    return {
      'candidate': candidate_record,
      'comms_percentile': comms_percentile,
      'coding_percentile': coding_percentile,
      }
  except:
    return {'errors': 'The requested Candidate ID could not be found. Please try again.'}, 404
