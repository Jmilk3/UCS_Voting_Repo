# Defines a Bloc class for storing data about different groups of voters

class Bloc:
    """
A class which stores the data needed for a bloc when using votekit ballot generation.
    """
    # Declare private vars
    __name = None
    __size = None
    __candidates = None
    __cohesion = None

    def __init__(self, name, size, candidates, cohesion):
        """
        name (str): The name of the bloc.
        size (int): The number of voters in the bloc.
        candidates (list<str>): A list with the names of candidates that are part of the bloc.
        cohesion (dict<str, float>): A dictionary where keys are bloc names and values are a
          corresponding cohesion value for that block. These values must sum to 1.
        """
        self.__name = name
        self.__size = size
        self.__candidates = candidates
        self.__cohesion = cohesion
        
    
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

    @staticmethod
    def outputVars(blocs):
        """
        A function which returns the expected inputs for votekit's from_params method.
        blocs (list<Bloc>): A list of bloc objects from which to pull and format the data.
        """
        # define dicts to store various bloc values
        candidate_slates = {} # Stores lists of candidates from each bloc
        voter_counts = {} # Stores voter count for each bloc
        cohesion_params = {} # Stores cohesion params from each bloc

        

        # Get the necessary data from each bloc and put it into a dict
        for bloc in blocs:
            candidate_slates[bloc.name()] = bloc.candidates()
            voter_counts[bloc.name()] = bloc.size()
            cohesion_params[bloc.name()] = bloc.cohesion()
        
        # convert from voter counts to voter proportion
        total_votes = float(sum(voter_counts.values()))
        voter_props = {}
        for bloc_name in voter_counts.keys():
            voter_props[bloc_name] = voter_counts[bloc_name] / total_votes

        # Return the various values
        return candidate_slates, voter_props, cohesion_params
        
    
