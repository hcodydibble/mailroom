"""Python based package to automate charity donor emails and reports."""
from __future__ import print_function

DONOR_DATABASE = [{'name': 'gabe', 'amt': [10, 25, 100, 2]},
                  {'name': 'cody', 'amt': [12, 3, 94, 0.50]},
                  {'name': 'kavdi', 'amt': [100, 520.27]}]


def main():  # pragma: no cover
    """Initial display function and handler."""
    mail_room_greeter()
    main_prompt()


def main_prompt():  # pragma: no cover
    """Main prompt handler function for charity thank you email and report creator."""
    first_user_choice()
    user_choice = get_user_input('\n>> ')
    main_dash_navigator(user_choice)


def create_a_report():
    """"Create sorted report of donors with donation data."""
    sorted_donors = donor_data_aggregator(DONOR_DATABASE)
    header = """
    @============================================@
    |                     |     |        |       |
    |     DONOR NAME      | AMT | TOTAL  |  AVG  |
    |                     |     |        |       |
    @============================================@"""
    return header
    print(header)
    for donor in sorted_donors:  # pragma: no cover
        print('    |{:<20} | {:>3} | {:>6.2f} | {:>6.2f}|'.format(donor[0].title(), donor[1], donor[2], donor[3]))
    print('    @' + '=' * 44 + '@\a')
    main_prompt()


def send_a_thank_you():  # pragma: no cover
    """"Return a thank you letter for a specified donor."""
    donor_name = get_user_input("Please input donor name:\n>> ")
    if donor_name == "list":
        donor_list_gen(DONOR_DATABASE)
    for donor in DONOR_DATABASE:
        if donor_name == donor["name"]:
            donation_validator(donor_name)
        else:
            DONOR_DATABASE.append({'name': donor_name, 'amt': []})
            donation_validator(donor_name)


def donation_validator(donor_name):  # pragma: no cover
    """Validate and inputs donation."""
    donation = float(get_user_input("What is the donation ammount:\n>> "))
    if isinstance(donation, (int, float)) and donation > 0:
        for donor in DONOR_DATABASE:
            if donor['name'] == donor_name:
                donor['amt'].append(donation)
                thank_you_writer(donor_name, donation)
                main_prompt()
    else:
        donation_validator(donor_name) 


def get_user_input(text):  # pragma: no cover
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
    return instructions


def first_user_choice():  # pragma: no cover
    """Ask user to either enter Send a Thank You or Create a Report."""
    question_for_user = """\nPlease select from the following options:

    1. Send a Thank You
    2. Create a Report
    3. Exit"""
    print(question_for_user)


def main_dash_navigator(user_input):  # pragma: no cover
    """Navigator and validator for main prompt."""
    if user_input == '1':
        send_a_thank_you()
    if user_input == '2':
        create_a_report()
    if user_input == '3':
        exit()
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


def donor_list_gen(db):  # pragma: no cover
    """Display list of donor names."""
    donor_names = [donor['name'] for donor in db]
    for name in donor_names:
        print(name)
    send_a_thank_you()


def thank_you_writer(donor_name, amt):
    """Send a thank you 'email' to a donor."""
    email_template = """
    Dear {},
    
    We at the society for lost and unloved pokemons thank you 
    for your generous donation of ${}. Your donation will
    go towards rehabilitating injured pokemons and finding 
    them new loving homes.

    V/R
    Professor Oak

    """.format(donor_name, amt)
    print(email_template)
    return email_template

if __name__ == '__main__':  # pragma: no cover
    main()
