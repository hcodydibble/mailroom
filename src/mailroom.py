"""Python based package to automate charity donor emails and reports."""

DONOR_DATABASE = [{'name': 'gabe', 'amt': [10, 25, 100, 2]},
                  {'name': 'cody', 'amt': [12, 3, 94, 0.50]},
                  {'name': 'kavid', 'amt': [100, 520.27]}]


def main():
    """Main handler function for charity thank you email and report creator."""
    mail_room_greeter()
    first_user_choice()
    user_choice = get_user_input('\n>> ')
    main_dash_navigator(user_choice)


def create_a_report():
    """"Create sorted report of donors with donation data."""
    pass


def send_a_thank_you():
    """"Return a thank you letter for a specified donor."""
    pass


def get_user_input(text):
    """Get and return user input with py2/3 version handling."""
    try:
        user_input = raw_input(text)
    except NameError:
        user_input = input(text)
    return user_input


def mail_room_greeter():  # pragma: no cover
    """Splash page and instructions for mailroom package."""
    header = """
    #======================================#
    |                                      |
    |                                      |
    |          MAILROOM MADNESS            |
    |                V 0.1                 |
    |                                      |
    #======================================#
    """
    instructions = "\n\n  Welcome to the mailroom automation package\n\
  from here you will be able to send a thank you\n\
  email to one of our generous donors or display\n\
  an ordered list of all of our benefactors.\n"
    print(header, instructions)


def first_user_choice():
    """Ask user to either enter Send a Thank You or Create a Report."""
    question_for_user = """\nPlease select from the following options:

    1. Send a Thank You
    2. Create a Report
    3. Exit"""
    print(question_for_user)


def main_dash_navigator(user_input):
    """Navigator and validator for main prompt."""
    if user_input == '1':
        send_a_thank_you()
    if user_input == '2':
        create_a_report()
    if user_input == '3':
        quit()
    if user_input not in ['1', '2', '3']:
        main_dash_navigator(get_user_input('Invalid entry.\n\n>> '))


def donor_data_aggregator(donor_db):
    """Fill and return a list of donors sorted by total donation amount."""
    donor_info = []
    for donor in donor_db:
        donor_name = donor['name']
        amount_of_donations = len(donor['amt'])
        total_donations = sum(donor['amt'])
        avg_donation = total_donations / amount_of_donations
        donor_info.append([donor_name, amount_of_donations,
                           total_donations, avg_donation])
    return sorted(donor_info, key=lambda x: x[-2], reverse=True)
