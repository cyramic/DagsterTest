# Dagster Test
This is a simple setup that runs dagster in containers so that I can test how it could be deployed 
to a production environment.

## How to run
1. Copy the `.env.sample` file to `.env` and update the values inside to what you want
2. Run `docker compose build` to build the docker images, and `docker compose up` to run them
3. Navigate to `https://localhost:3000` for the dagit interface.