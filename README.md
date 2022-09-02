## Getting starterd
### Dev Containers (M1 Users, follow this guide)
1. Make sure you have the [Microsoft Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension installed.
2. Make sure you have [Docker](https://www.docker.com/products/docker-desktop/) installed on your computer.
3. Clone the repository.
4. Open the repo in VS Code.
5. Click "Open in Container" when VS Code prompts to open container in the bottom right hand corner.
6. **Be Patient!** The initial install will take a LONG time, it's building a container that has postgres preconfigured and even installing all your project dependencies. (For both flask and react!)
7. Once everything is up, be sure to make a `.env` file based on `.env.example` in both the root directory and the *react-app* directory before running your app.
8.1 Setup your PostgreSQL user, password and database and make sure it matches your **.env** file. An example .env file is provided with the settings I used (in a real world scenario this information will be private).
   - IMPORTANT: The postgres user must be a SUPERUSER. The next step is dependent on it.
8.2 If your PostgreSQL database and user were setup correctly, the following command should properly seed your database:
   - ```psql -d 'database name' -a -f app/sample-data/seeders.sql```
   
9. Get into your pipenv, migrate your database, seed your database, and run your flask app

   ```bash
   pipenv shell
   ```
      ```bash
   flask db migrate
   ```

   ```bash
   flask db upgrade
   ```
   
   ```bash
   psql -d 'database name' -a -f app/sample-data/seeders.sql
   ```

   ```bash
   flask run
   ```

10. To run the React App in development, checkout the [README](./react-app/README.md) inside the `react-app` directory.

<br>

### Standard (Traditional)

1. Clone this repository.
2. Install dependencies

      ```bash
      pipenv install --dev -r dev-requirements.txt && pipenv install -r requirements.txt
      ```

3. Create a **.env** file based on the example with proper settings for your
   development environment
4.1 Setup your PostgreSQL user, password and database and make sure it matches your **.env** file. An example .env file is provided with the settings I used (in a real world scenario this information will be private).
   - IMPORTANT: The postgres user must be a SUPERUSER. The next step is dependent on it.
   
5. Get into your pipenv, migrate your database, seed your database, and run your flask app

   ```bash
   pipenv shell
   ```
      ```bash
   flask db migrate
   ```

   ```bash
   flask db upgrade
   ```
   
   ```bash
   psql -d 'database name' -a -f app/sample-data/seeders.sql
   ```

   ```bash
   flask run
   ```

6. To run the React App in development, checkout the [README](./react-app/README.md) inside the `react-app` directory.

***
