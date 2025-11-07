# Implementation of Test class, used as a straightforward way to define a test's paramaters

class TestParams:
    """
    A class to store the necessary data for a test.
    It includes the name of the test, the bloc objects the test uses, and the number of seats to elect
    """
    def __init__(self, test_name, bloc1, bloc2, num_seats = 1, num_ballots = 1000):
        """
        Creates a new Test object.
        test_name (str): The name of the test. This is what the test will be called in the test runner
        bloc1 (Bloc): The first bloc for this test
        bloc2 (Bloc): The second bloc for this test
        num_seats (int): The number of seats that should be elected. Defaults to 1
        num_ballots (int): The number of ballots that should be generated for each round of testing
        """
        self.test_name = test_name
        self.bloc1 = bloc1
        self.bloc2 = bloc2
        self.num_seats = num_seats
        self.num_ballots = num_ballots