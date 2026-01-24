# A file with functions that run different ballot generators
from votekit.ballot_generator import slate_pl_profile_generator, slate_bt_profile_generator,cambridge_profile_generator,slate_bt_profile_generator_using_mcmc
from math import factorial
def btGenerator(config):
    """
    A function that uses the Bradley-Terry ballot generator to generate ballots using the given config object.
    config: A BlocSlateConfig object with the paramaters for generation
    """
    # Generate the ballots, switching methods if needed for large ballot pools
    numBallots = len(config.candidates) ^ len(config.blocs)
    if numBallots < factorial(12): # Checks if total number of possible ballots is too large for normal method
        return slate_bt_profile_generator(config)
    else:
        return slate_bt_profile_generator_using_mcmc(config)


def plGenerator(config):
    """
    A function that uses the Plackett-Luce ballot generator to generate ballots using the given config object.
    config: A BlocSlateConfig object with the paramaters for generation
    """
    # Generate the ballots
    return slate_pl_profile_generator(config)
    
def cambridgeGenerator(config):
    """
    A function that uses the Cambridge Sampler to generate ballots using the given config object.
    config: A BlocSlateConfig object with the paramaters for generation
    """
    # Generate the ballots
    return cambridge_profile_generator(config)

def generateAll(config):
    """
    A function that calls all 3 ballot generators using the given config. It returns a list with
    the results in the order [pl, bt, cambridge]
    config: A BlocSlateConfig object with the paramaters for generation
    """
    return [plGenerator(config), btGenerator(config), cambridgeGenerator(config)]


