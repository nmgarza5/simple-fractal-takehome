## Simple Fractal Coding Assessment

Nikolas Garza's Simple Fractal coding assessment. The tech stack employed is a backend built with Python/Flask and a PostgreSQL database. The frontend is built with React/Redux. A project starter was used as a base for this application. The starter is built to be deployed to heroku however this functionality was not used. Simply create the postgres database, install the requirements as indicated below, and run on localhost. 

## Getting started

1. Clone this repository.

2. Install dependencies

      ```bash
      pipenv install --dev -r dev-requirements.txt && pipenv install -r requirements.txt
      ```
3. Create a **.env** file based on the example with proper settings for your
   development environment
   
4 Setup your PostgreSQL user, password and database and make sure it matches your **.env** file. An example .env file is provided with the settings I used (in a real     world scenario this information will be private).
   - IMPORTANT: The postgres user must be a SUPERUSER. The next step is dependent on it. 

5. Get into your pipenv, seed your database, and run your flask app

   ```bash
   pipenv shell
   ```
   
   ```bash
   psql -d 'database name' -a -f app/sample-data/seeders.sql
   ```
   - in order to seed the database, the path to the seeder file will need to be changed on your machine. In app/seeders.sql change the following:
   
   ![image](https://user-images.githubusercontent.com/90273783/188048709-58caeb9f-4cde-4bb3-9df2-367630058f22.png)

   ```bash
   flask run
   ```

6. To run the React App in development, checkout the [README](./react-app/README.md) inside the `react-app` directory.
   - in summary: cd into react-app and run the following command:
   - ``` npm run start ```

