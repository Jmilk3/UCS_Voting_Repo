# A file with functions that run different ballot generators
from votekit.ballot_generator import name_pl_profile_generator, name_bt_profile_generator,cambridge_profile_generator,name_bt_profile_generator_using_mcmc
from votekit.cleaning import clean_rank_profile, condense_rank_profile

def btGenerator(config):
    """
    A function that uses the Bradley-Terry ballot generator to generate ballots using the given config object.
    config: A BlocSlateConfig object with the paramaters for generation
    """
    # Generate the ballots, switching methods if needed for large candidate pools
    numCandidates = sum([len(config.slate_to_candidates[key]) for key in config.slate_to_candidates.keys()])
    if numCandidates < 12:
        ballots = name_bt_profile_generator(config)
    else:
        ballots = name_bt_profile_generator_using_mcmc(config)
    
    # Clean the ballots and return
    return cleanHelper(ballots)


def plGenerator(config):
    """
    A function that uses the Plackett-Luce ballot generator to generate ballots using the given config object.
    config: A BlocSlateConfig object with the paramaters for generation
    """
    # Generate the ballots
    ballots = name_pl_profile_generator(config)
    
    # Clean the ballots and return
    return cleanHelper(ballots)
    
def cambridgeGenerator(config):
    """
    A function that uses the Cambridge Sampler to generate ballots using the given config object.
    config: A BlocSlateConfig object with the paramaters for generation
    """
    # Generate the ballots
    ballots = cambridge_profile_generator(config)

    # Clean the ballots and return
    return cleanHelper(ballots)

def generateAll(config):
    """
    A function that calls all 3 ballot generators using the given config. It returns a list with
    the results in the order [pl, bt, cambridge]
    config: A BlocSlateConfig object with the paramaters for generation
    """
    return [plGenerator(config), btGenerator(config), cambridgeGenerator(config)]

def cleanHelper(ballots):
    """A function that cleans the given ballot by removing any tied candidates then consolidating the profile"""
    # TODO: Create a better method for tie resolution than 'delete ties'
    return condense_rank_profile(
        clean_rank_profile(ballots,
                            lambda rankings :
                              tuple(i if len(i) <= 1 else frozenset() for i in rankings)))

