-- CREATE TABLE companies (
--   id SERIAL PRIMARY KEY,
--   fractal_index DECIMAL NOT NULL
-- );

-- CREATE TABLE score_records (
--   id SERIAL PRIMARY KEY,
--   candidate_id INTEGER NOT NULL,
--   communication_score INTEGER,
--   coding_score INTEGER,
--   title VARCHAR(255),
--   company_id INTEGER NOT NULL REFERENCES companies (id)
-- );


COPY companies(fractal_index)
FROM 'app/seeders.sql'
DELIMITER ','
CSV HEADER;


COPY score_records(candidate_id,communication_score,coding_score,title,company_id)
FROM 'app/seeders.sql'
DELIMITER ','
CSV HEADER;
