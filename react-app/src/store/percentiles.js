
const GET_PERCENTILES = 'percentiles/receivePercentiles';
const CLEAR_PERCENTILES = 'percentiles/clearPercentiles';

const receivedPercentiles = (percentiles) => ({
  type: GET_PERCENTILES,
  payload: percentiles
});

const clearedPercentiles = () => ({
  type: CLEAR_PERCENTILES,
});

export const receivePercentiles = (candidate_id) => async (dispatch) => {
	const res = await fetch(`/api/percentile/${candidate_id}`);
    const candidate_percentiles = await res.json();
    if (candidate_percentiles.errors) {
        return candidate_percentiles
    } else {
        dispatch(receivedPercentiles(candidate_percentiles));
        return candidate_percentiles;
    }
};

export const clearPercentiles = () => async (dispatch) => {
    dispatch(clearedPercentiles());
}

const percentilesReducer = (state = {}, action) => {
	let newState = { ...state };

    switch (action.type) {
		case GET_PERCENTILES: {
			newState = action.payload;
			return newState;
		}
		case CLEAR_PERCENTILES: {
			newState = 'cleared';
			return newState;
		}
		default:
			return state;
	}
};

export default percentilesReducer;
