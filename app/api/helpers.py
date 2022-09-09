from app.models import Company, Record
import math
from scipy import stats

def are_similar(company_1_FI, company_2_FI):
    similar = math.fabs(company_1_FI['fractal_index'] - company_2_FI['fractal_index']) < 0.15
    return similar

# returns a set with the IDs of all canidates who are similar
def find_similar_candidates(candidate_record):
  similar_candidates = set()
  all_records = Record.query.all()

  for record in all_records:
    title = record.to_dict()['title']
    company = record.to_dict()['company']
    id = record.to_dict()['id']
    if title == candidate_record['title'] and are_similar(company, candidate_record['company']):
      similar_candidates.add(id)

  return similar_candidates


# return the a dictionary containing the specified candidate's coding and communication percentiles
def calculate_percentiles(similar_candidates, candidate_record):
  candidate_coding_score = candidate_record['coding_score']
  candidate_communication_score = candidate_record['communication_score']
  all_records = Record.query.all()
  # find the coding/comms scores for all similar canidates
  similar_candidates_coding = [
                                record.to_dict()['coding_score']
                                for record in all_records
                                if record.to_dict()['id']
                                in similar_candidates
                                ]
  similar_candidates_comms = [
                                record.to_dict()['communication_score']
                                for record in all_records
                                if record.to_dict()['id']
                                in similar_candidates
                                ]
  # use scipy function to calculate percentile, passing in the candidate's and similar candidates' scores
  comms_percentile = round(stats.percentileofscore(similar_candidates_comms, candidate_communication_score), 2)
  coding_percentile = round(stats.percentileofscore(similar_candidates_coding, candidate_coding_score), 2)
  return {'comms_percentile': comms_percentile, 'coding_percentile': coding_percentile}
