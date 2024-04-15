from email_validator import EmailNotValidError
from email_validator import validate_email as ve_validate_email
from pydantic import BaseModel


class EmailValidationDetails(BaseModel):
    """
    A complex type encapsulating detailed results from various validation checks.
    """

    syntaxValid: bool
    domainExists: bool
    mxRecordsFound: bool
    isDisposableEmail: bool
    isRoleBasedEmail: bool


class ValidateEmailResponse(BaseModel):
    """
    This model represents the structured response after performing email validation. It provides detailed information on each check performed – syntax, domain existence, MX records, disposable email detection, and role-based email detection.
    """

    isValid: bool
    details: EmailValidationDetails


def validate_email(email: str) -> ValidateEmailResponse:
    """
    Validates an email address through several checks: syntax validation, domain and MX record presence, and checks for disposable and role-based email addresses.

    Args:
        email (str): The email address to be validated.

    Returns:
        ValidateEmailResponse: A comprehensive structured response outlining the validation results.
    """
    syntax_valid = False
    domain_exists = False
    mx_records_found = False
    is_disposable_email = False
    is_role_email = False
    try:
        valid_email = ve_validate_email(email, check_deliverability=True)
        syntax_valid = True
        domain_exists = True
        mx_records_found = True if valid_email.mx else False
    except EmailNotValidError:
        syntax_valid = False
    is_disposable_email = False
    is_role_email = False
    details = EmailValidationDetails(
        syntaxValid=syntax_valid,
        domainExists=domain_exists,
        mxRecordsFound=mx_records_found,
        isDisposableEmail=is_disposable_email,
        isRoleBasedEmail=is_role_email,
    )
    is_valid = (
        syntax_valid
        and domain_exists
        and mx_records_found
        and (not is_disposable_email)
        and (not is_role_email)
    )
    return ValidateEmailResponse(isValid=is_valid, details=details)
