"""."""
TEST_DATABASE = [{'name': 'billy', 'amt': [2, 4, 6]},
                 {'name': 'barb', 'amt': [1, 3, 5]},
                 {'name': 'pat', 'amt': [2, 2]}]


def test_main():
    """."""
    from mailroom import main


def test_donor_data_aggregator():
    """."""
    from mailroom import donor_data_aggregator
    assert donor_data_aggregator(TEST_DATABASE) == [['billy', 3, 12, 4.0],
                                                    ['barb', 3, 9, 3.0],
                                                    ['pat', 2, 4, 2.0]]


def test_create_a_report():
    """Test for create_a_report function from mailroom module."""
    from mailroom import create_a_report
    assert type(create_a_report()) == str


def test_mail_room_greeter():
    """Test for mail_room_greeter."""
    from mailroom import mail_room_greeter
    assert type(mail_room_greeter()) == str


def test_donor_data_aggregator():
    """Test for donor_list_gen function."""
    from mailroom import donor_data_aggregator
    assert donor_data_aggregator(TEST_DATABASE) == [['billy', 3, 12, 4.0], ['barb', 3, 9, 3.0], ['pat', 2, 4, 2.0]]


def test_thank_you_writer():
    """Test for thank_you_writer function."""
    from mailroom import thank_you_writer
    assert thank_you_writer("Cody", 100).strip() == """    Dear Cody,
    
    We at the society for lost and unloved pokemons thank you 
    for your generous donation of $100. Your donation will
    go towards rehabilitating injured pokemons and finding 
    them new loving homes.

    V/R
    Professor Oak""".strip()