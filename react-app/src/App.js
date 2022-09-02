import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { receivePercentiles } from './store/percentiles';

function App() {
  const dispatch = useDispatch();
  const record = useSelector((state) => state.record)

  let candidateId = record?.candidate?.candidate_id
  let title = record?.candidate?.title
  let codingScore = record?.candidate?.coding_score
  let communicationScore = record?.candidate?.communication_score

  const [id, setId] = useState('')
  const [errors, setErrors] = useState('');

  useEffect(() => {
  }, [dispatch, candidateId, errors]);

  const onSubmit = async (e) => {
		e.preventDefault();
    setErrors('');

    const candidateRecord = await dispatch(receivePercentiles(id));
    if (candidateRecord.errors) {
      console.log(candidateRecord.errors)
      setErrors(candidateRecord.errors);
    }
}

  return (
    <BrowserRouter>
      <Switch>
        <Route path='/' >
          <h1>Candidate Engineering Skills Rankings</h1>
          <div>
            <div className='input_container'>
              <label htmlFor="candidate ID">Candidate ID:</label>
              <input
                name="candidate_id"
                type='number'
                placeholder="Enter your ID."
                required
                value={id}
                onChange={(e) => setId(e.target.value)}
              ></input>
              <div onClick={onSubmit} className='button'>
                Submit
              </div>
            </div>
            {
              errors ?
              <div className='display'>
                <h3>
                 {errors}
                </h3>
              </div>
            :
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
                      Coding Score Percentile (Similar Companies)
                  </h5>
                  <p>
                      {record.company_coding_percentile}
                  </p>
                </div>
                <div className='percentile'>
                  <h5>
                  Coding Score Percentile (Similar Title)
                  </h5>
                  <p>
                      {record.title_coding_percentile}
                  </p>
                </div>
                <div className='percentile'>
                  <h5>
                  Communication Score Percentile (Similar Companies)
                  </h5>
                  <p>
                      {record.company_communication_percentile}
                  </p>
                </div>
                <div className='percentile'>
                  <h5>
                  Communication Score Percentile (Similar Title)
                  </h5>
                  <p>
                      {record.title_communication_percentile}
                  </p>
                </div>
              </div>
              :
              <div className='display'>
                <h3>
                  Please enter an ID above to see the candidate's percentile rankings.
                </h3>
              </div>
            }
          </div>
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
