---
date: 2024-04-15T13:27:13.706625
author: AutoGPT <info@agpt.co>
---

# Email Validation API

Based on the task requirements and the information gathered, the goal is to create an email validation endpoint using FastAPI and Python, which incorporates various checks to ensure an email's validity. Here are the key steps to accomplish this:

1. **Email Format and Syntax Verification**:
   - Utilize the `re` module in Python to implement a regular expression that matches valid email formats. This is critical for initial verification to filter out obviously incorrect email formats.

2. **Email Domain and MX Record Checks**:
   - Employ the `dns.resolver` module from the `dnspython` library to verify the email domain's existence and resolve its MX records. This step is necessary to ensure the email domain is real and capable of receiving emails.

3. **Disposable Email Detection and Role-based Address Identification**:
   - Integrate a third-party library like `validate_email_address` to identify disposable emails and role-based addresses. This is important for preventing temporary or non-individual email usage which could affect the application's integrity.

4. **Endpoint Creation and Response**:
   - Develop a FastAPI endpoint that performs the above checks on an input email address. The endpoint will return a comprehensive validation result, indicating whether the email is valid, and if not, what issues were detected (e.g., invalid format, nonexistent domain, disposable email).

**Tech Stack**:
- **Programming Language**: Python
- **API Framework**: FastAPI
- **Database**: PostgreSQL (if persistence of requests or results is needed)
- **ORM**: Prisma (for interacting with the database in an efficient way)

This system aims to provide a robust solution for email validation, covering various aspects from format checking to domain validation, ensuring only valid emails are processed or accepted in applications.

## What you'll need to run this
* An unzipper (usually shipped with your OS)
* A text editor
* A terminal
* Docker
  > Docker is only needed to run a Postgres database. If you want to connect to your own
  > Postgres instance, you may not have to follow the steps below to the letter.


## How to run 'Email Validation API'

1. Unpack the ZIP file containing this package

2. Adjust the values in `.env` as you see fit.

3. Open a terminal in the folder containing this README and run the following commands:

    1. `poetry install` - install dependencies for the app

    2. `docker-compose up -d` - start the postgres database

    3. `prisma generate` - generate the database client for the app

    4. `prisma db push` - set up the database schema, creating the necessary tables etc.

4. Run `uvicorn project.server:app --reload` to start the app

## How to deploy on your own GCP account
1. Set up a GCP account
2. Create secrets: GCP_EMAIL (service account email), GCP_CREDENTIALS (service account key), GCP_PROJECT, GCP_APPLICATION (app name)
3. Ensure service account has following permissions: 
    Cloud Build Editor
    Cloud Build Service Account
    Cloud Run Developer
    Service Account User
    Service Usage Consumer
    Storage Object Viewer
4. Remove on: workflow, uncomment on: push (lines 2-6)
5. Push to master branch to trigger workflow
