# A file with functions that run different ballot generators

def btGenerator(config):
    """
    A function that uses the Bradley-Terry ballot generator to generate ballots using the given config object.
    config: A BlocSlateConfig object with the paramaters for generation
    """

def plGenerator(config):
    """
    A function that uses the Plackett-Luce ballot generator to generate ballots using the given config object.
    config: A BlocSlateConfig object with the paramaters for generation
    """
    
def cambridgeGenerator(config):
    """
    A function that uses the Cambridge Sampler to generate ballots using the given config object.
    config: A BlocSlateConfig object with the paramaters for generation
    """

def generateAll(config):
    """
    A function that calls all 3 ballot generators using the given config. It returns a list with
    the results in the order [pl, bt, cambridge]
    config: A BlocSlateConfig object with the paramaters for generation
    """
    return [plGenerator(config), btGenerator(config), cambridgeGenerator(config)]