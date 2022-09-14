from app.models import Record
import math
from scipy import stats

def are_similar(company_1_FI, company_2_FI):
    return math.fabs(company_1_FI['fractal_index'] - company_2_FI['fractal_index']) < 0.15

# returns a set with the IDs of all canidates who are similar
def find_similar_candidates(candidate_record):
  all_records = Record.query.all()
#   create a list of all records where the titles match and companies are similar
  return [
            record.to_dict()['id']
            for record in all_records
            if record.to_dict()['title'] == candidate_record['title']
            and are_similar(record.to_dict()['company'], candidate_record['company'])
        ]



# return a dictionary containing the specified candidate's coding and communication percentiles
def calculate_percentiles(similar_candidates, candidate_record):
  coding_score = candidate_record['coding_score']
  communication_score = candidate_record['communication_score']

  # create a list and query the database to find every record in similar_candidates
  similar_records = [Record.query.get(id).to_dict() for id in similar_candidates]

  # find the coding/comms scores for all similar canidates
  similar_candidates_coding = [record['coding_score'] for record in similar_records]
  similar_candidates_comms = [record['communication_score'] for record in similar_records]

  # use scipy function to calculate percentile, passing in the candidate's and similar candidates' scores
  comms_percentile = round(stats.percentileofscore(similar_candidates_comms, communication_score), 2)
  coding_percentile = round(stats.percentileofscore(similar_candidates_coding, coding_score), 2)

  return {
            'comms_percentile': comms_percentile,
            'coding_percentile': coding_percentile
        }
