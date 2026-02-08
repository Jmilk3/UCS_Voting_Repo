# Defines a Bloc class for storing data about different groups of voters
from votekit.ballot_generator import BlocSlateConfig
from votekit import PreferenceInterval

class Bloc:
    """
A class which stores the data needed for a bloc when using votekit ballot generation.
    """
    # Declare private vars
    __name = None
    __size = None
    __candidates = None
    __cohesion = None
    __preference = None

    def __init__(self, name, size, candidates, cohesion, preference):
        """
        name (str): The name of the bloc.
        size (float): The percentage of total voters in the bloc
        candidates (list<str>): A list with the names of candidates that are part of the bloc.
        cohesion (dict<str, float>): A dictionary where keys are bloc names and values are a
          corresponding cohesion value for that block. These values must sum to 1.
        preference (dict<string, dict<string, list>>): A dictionary mapping bloc names to dictionaries with preference values
         eg. {Bloc 1: {A: [], B: []}, Bloc 2: {C: []}}
        """
        self.__name = name
        self.__size = size
        self.__candidates = candidates
        self.__cohesion = cohesion
        self.__preference = preference
        
    
    def name(self):
        """Access function for bloc name"""
        return self.__name
    
    def size(self):
        """Access function for bloc size"""
        return self.__size
    
    def candidates(self):
        """Access function for bloc candidate slate"""
        return self.__candidates
    
    def cohesion(self):
        """Access function for bloc cohesion"""
        return self.__cohesion
    
    def preference(self):
        """Access function for preference params"""
        return self.__preference


    @staticmethod
    def outputVars(blocs, numVoters):
        """
        A function which returns a BlocSlateConfig object for the given blocs
        blocs (list<Bloc>): A list of bloc objects from which to pull and format the data.
        numVoters (int): The number of voters that the config option should have. 
        returns a list with [numVoters, candidates, voter_proportions, preference_params (unprocessed), cohesion_params]
        """
        # define dicts to store various bloc values
        candidate_slates = {} # Stores lists of candidates from each bloc
        voter_props = {} # stores the voter proportion for each bloc
        cohesion_params = {} # Stores cohesion params from each bloc
        preference_params = [] # stores the preference params from each bloc
        # Get the necessary data from each bloc and put it into a dict
        for bloc in blocs:
            candidate_slates[bloc.name()] = bloc.candidates()
            voter_props[bloc.name()] = bloc.size()
            cohesion_params[bloc.name()] = bloc.cohesion()
            preference_params.append(bloc.name())
            preference_params.append(bloc.preference())

        return [numVoters, candidate_slates, voter_props, preference_params, cohesion_params]

    
