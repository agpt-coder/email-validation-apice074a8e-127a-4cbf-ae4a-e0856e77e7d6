import logging
from contextlib import asynccontextmanager

import project.validate_email_service
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response
from prisma import Prisma

logger = logging.getLogger(__name__)

db_client = Prisma(auto_register=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db_client.connect()
    yield
    await db_client.disconnect()


app = FastAPI(
    title="Email Validation API",
    lifespan=lifespan,
    description="Based on the task requirements and the information gathered, the goal is to create an email validation endpoint using FastAPI and Python, which incorporates various checks to ensure an email's validity. Here are the key steps to accomplish this:\n\n1. **Email Format and Syntax Verification**:\n   - Utilize the `re` module in Python to implement a regular expression that matches valid email formats. This is critical for initial verification to filter out obviously incorrect email formats.\n\n2. **Email Domain and MX Record Checks**:\n   - Employ the `dns.resolver` module from the `dnspython` library to verify the email domain's existence and resolve its MX records. This step is necessary to ensure the email domain is real and capable of receiving emails.\n\n3. **Disposable Email Detection and Role-based Address Identification**:\n   - Integrate a third-party library like `validate_email_address` to identify disposable emails and role-based addresses. This is important for preventing temporary or non-individual email usage which could affect the application's integrity.\n\n4. **Endpoint Creation and Response**:\n   - Develop a FastAPI endpoint that performs the above checks on an input email address. The endpoint will return a comprehensive validation result, indicating whether the email is valid, and if not, what issues were detected (e.g., invalid format, nonexistent domain, disposable email).\n\n**Tech Stack**:\n- **Programming Language**: Python\n- **API Framework**: FastAPI\n- **Database**: PostgreSQL (if persistence of requests or results is needed)\n- **ORM**: Prisma (for interacting with the database in an efficient way)\n\nThis system aims to provide a robust solution for email validation, covering various aspects from format checking to domain validation, ensuring only valid emails are processed or accepted in applications.",
)


@app.post(
    "/validate/email",
    response_model=project.validate_email_service.ValidateEmailResponse,
)
async def api_post_validate_email(
    email: str,
) -> project.validate_email_service.ValidateEmailResponse | Response:
    """
    Endpoint for receiving email validation requests and returning validation results.
    """
    try:
        res = project.validate_email_service.validate_email(email)
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )
