import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Home = () => {
  const [country, setCountry] = useState(null);
  const [capital, setCapital] = useState('');
  const [capitalApiResponse, setCapitalApiResponse] = useState(null);

  const getRandomCountry = async () => {
    try {
      const response = await axios.get(`${process.env.REACT_APP_BASE_URL}/api/getRandomCapitalCity/`);
      setCountry(response.data);
      setCapital('');
      setCapitalApiResponse(null);
    } catch (error) {
      console.log(error);
    }
  };

  const checkCapital = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        `${process.env.REACT_APP_BASE_URL}/api/checkCapital/`,
        { capital, country: country.country }
      );
      setCapitalApiResponse(response.data);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    getRandomCountry();
  }, []);

  return (
    <>
      <div className='center'>
        <h1>Guess The Capital</h1>
      </div>
      <div className='column'>
        {country ? (
          <form onSubmit={checkCapital} className='column w-100'>
            <p>What is the capital city of {country.country}?</p>
            <input
              required
              onChange={(e) => setCapital(e.target.value)}
              value={capital}
              placeholder='Enter capital'
            />
            <button type='submit'>Check</button>
          </form>
        ) : (
          <p>Loading</p>
        )}
        <br />
        {capitalApiResponse && (
          <>
            <p className={`${capitalApiResponse.found ? 'success' : 'danger'}`}>
              {capitalApiResponse.details}
            </p>
            <button onClick={getRandomCountry}>Play Again</button>
          </>
        )}
      </div>
    </>
  );
};

export default Home;
