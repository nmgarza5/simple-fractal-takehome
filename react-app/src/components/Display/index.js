import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';

const Display = () => {
  const dispatch = useDispatch();
  const record = useSelector((state) => state.record)

  let error;
  if (record === 'cleared') error = true

  let candidateId = record?.candidate?.candidate_id
  let title = record?.candidate?.title
  let codingScore = record?.candidate?.coding_score.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')
  let communicationScore = record?.candidate?.communication_score.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')
  let codingPercentile = record.coding_percentile
  let commsPercentile = record.comms_percentile

  useEffect(() => {
  }, [dispatch, candidateId]);

  return (
        <>
            {
            candidateId ?
              <div className='display'>
                <div className='headers'>
                  <h3>
                    <strong>ID:</strong> {candidateId}
                  </h3>
                  <h3>
                    <strong>Title:</strong> {title}
                  </h3>
                  <h3>
                    <strong>Coding Score:</strong> {codingScore}
                  </h3>
                  <h3>
                    <strong>Communication Score:</strong> {communicationScore}
                  </h3>
                </div>
                <div className='percentile'>
                  <h5>
                      Coding Score Percentile
                  </h5>
                  <p>
                      {codingPercentile}
                  </p>
                </div>
                <div className='percentile'>
                  <h5>
                      Communication Score Percentile
                  </h5>
                  <p>
                      {commsPercentile}
                  </p>
                </div>
              </div>
              :
                error != null
              ?
              <>
              </>
              :
              <div className='display'>
                <h3>
                  Please enter an ID above to see the candidate's percentile rankings.
                </h3>
              </div>
            }
        </>
  );
}

export default Display;
