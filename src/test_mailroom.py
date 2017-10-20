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
