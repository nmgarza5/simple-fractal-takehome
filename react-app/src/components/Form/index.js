import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { clearPercentiles, receivePercentiles } from '../../store/percentiles.js'

const Form = () => {
  const dispatch = useDispatch();

  const [id, setId] = useState('')
  const [errors, setErrors] = useState('');

  useEffect(() => {
  }, [dispatch, errors]);

  const onSubmit = async (e) => {
		e.preventDefault();
    setErrors('');

    const candidateRecord = await dispatch(receivePercentiles(id));
    if (candidateRecord.errors) {
      await dispatch(clearPercentiles())
      setErrors(candidateRecord.errors);
    }
}

  return (
    <>
        <div className='input_container'>
            <label htmlFor="candidate ID">
                Candidate ID:
            </label>
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
        {errors &&
            <div className='display'>
                <h3>
                    {errors}
                </h3>
            </div>
        }
    </>
  );
}

export default Form;
