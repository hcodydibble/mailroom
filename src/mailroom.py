"""Python based package to automate charity donor emails and reports."""

DONOR_DATABASE = {}


def main():
    """Main handler function for charity thank you email and report creator."""
    pass


def create_a_report():
    """"Create sorted report of donors with donation data."""
    pass


def send_a_thank_you():
    """"Return a thank you letter for a specified donor."""
    pass


def get_user_input():
    """Get and return user input with py2/3 version handling."""
    try:
        user_input = raw_input('py2')
    finally:
        user_input = input('py3')
    return user_input
