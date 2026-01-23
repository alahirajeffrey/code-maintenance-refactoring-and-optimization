# Flask Microservice Refactor

Refactor a legacy Python flask monolith by modularizing configurations into environment-specific settings, extracting routes handlers into blueprints and service classes, introducing dependency injection, enforcing PEP8 with Black and Flake8, and verifying all existing pytest tests and CI checks pass unchanged.

## Requirements

Requirements to run the project:

1. Docker compose

How to run:

1. Navigate to the directory
2. Run the command `docker compose up --build` to build the application
3. Create a `.env` file and populate with the `.env.example file`
4. Then run the command `docker compose up -d`
5. Open postman and make a request to `localhost:5000/health` to run the health checker or `localhost:5000/users` to fetch users or `localhost:5000/users/{userId}` to fetch users by ID.

**NB:**

This project should:

1. Create a flask microservice
2. Route handlers should be setup using blueprints
3. Setup configurations that user environment specific settings
4. Setup dependency injection
5. Enforce PEP8 coding standards with black and flake8
6. Pass existing tests
7. Create CI pipeline to run lints and tests
