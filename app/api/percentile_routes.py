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
    similar_companies = []
    similar_companies_coding = []
    similar_company_communication = []
    for ele in all_companies:
      company = ele.to_dict()
      # print('\n\n', company)
      if are_similar(company, candidate_company):
          similar_companies.append(company)
          records = company['score_records']
          for record in records.values():
              similar_companies_coding.append(record['coding_score'])
              similar_company_communication.append(record['communication_score'])
      # print('\n\n', similar_companies_coding)

    # get similar candidates
    all_records = Record.query.all()
    similar_candidates_coding = []
    similar_candidates_communication = []
    for ele in all_records:
      candidate = ele.to_dict()
      if candidate['title'] == candidate_title:
          similar_candidates_coding.append(candidate['coding_score'])
          similar_candidates_communication.append(candidate['communication_score'])


  #   get percentiles
    company_coding_percentile = round(stats.percentileofscore(similar_companies_coding, candidate_coding_score), 2)
    company_communication_percentile = round(stats.percentileofscore(similar_company_communication, candidate_communication_score), 2)
    title_coding_percentile = round(stats.percentileofscore(similar_candidates_coding, candidate_coding_score), 2)
    title_communication_percentile = round(stats.percentileofscore(similar_candidates_communication, candidate_communication_score), 2)


    return {
      'candidate': candidate_record,
      'company_coding_percentile': company_coding_percentile,
      'company_communication_percentile': company_communication_percentile,
      'title_coding_percentile': title_coding_percentile,
      'title_communication_percentile': title_communication_percentile
      }
  except:
    return {'errors': 'The requested Candidate ID could not be found. Please try again.'}, 404
