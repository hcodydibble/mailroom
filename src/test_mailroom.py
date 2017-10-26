"""."""
TEST_DATABASE = [{'name': 'billy', 'amt': [2, 4, 6]},
                 {'name': 'barb', 'amt': [1, 3, 5]},
                 {'name': 'pat', 'amt': [2, 2]}]


def test_donor_data_aggregator():
    """Test for donor_list_gen function."""
    from mailroom import donor_data_aggregator
    assert donor_data_aggregator(TEST_DATABASE) == [['billy', 3, 12, 4.0],
                                                    ['barb', 3, 9, 3.0],
                                                    ['pat', 2, 4, 2.0]]


def test_header_data_type():
    """Test return type of header function."""
    from mailroom import mail_room_greeter
    assert type(mail_room_greeter()) == str


def test_thank_you_data_type():
    """Test return type of thank you writer function."""
    from mailroom import thank_you_writer
    assert type(thank_you_writer('gabe', '1000')) == str
