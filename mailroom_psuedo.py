"""Pseudo code for Mailroom Madness."""


def main_function():
    """Run different function based on users input."""
    prompt user to send a thank you or create a report
    if send a thank you run send_a_thank_you main_function
    if create a report run create_a_report function
    display instructions for user to quit


def send_a_thank_you():
    """Send a thank you."""
    display instructions to quit or return to original prompt
    list of donors
    prompt user for a name
    if answer is 'list':
        display donor names and reprompt
    if name is not in list of donors:
        add it to the list and use it
    else name is in list
        use it
    prompt user for donation amount
    if amount is not an integer or negative:
        reprompt for valid integer
    else amount is valid
        add the amount to the users donation
    print thank you email using donors name and amount
    return to original prompt


def create_a_report():
    """Create a report to display a list of donors sorted by historical donation
     amount.
    """
    display instructions to quit or return to original prompt
    sort donor list by historical donation amount
    display donor name, total donated, number of donations, average donations
    in a nice formated list
    return to original prompt


def get_user_input():
    """"."""
    user_input = raw_input('What you want? ')
