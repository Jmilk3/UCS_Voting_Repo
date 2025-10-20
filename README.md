# UCS_Voting_Repo
A repository that stores the programs used to examine and analyze how election results might change with different methods of Proportional Representation. This is part of the UCS voting project, meant to help inform people about Proportional Representation, examining different methods and how they might influence the outcome of elections.

## Design Notes
* I don't see any built in methods that create ballots with real world data then fill in rankings with a ballot generator. If we want to force each sample set to use the real world vote results as top choices, we might need to create our own method of generating a preference profile.
* The ballot generators can generate ballots with ties. We'll need to decide how to resolve these ties to actually run elections on them.

## Additional Notes
* The placeholder.txt files are there because we can't add empty folders to a repo. We should remove them once we add any file to a folder.

## 10/19/25: Notes on GerryChain and Recombination, for use similar to the MGGG study in Massachusetts 
* The MGGG code is poorly organized and clearly not ready for direct usage. It would primarly serve as a reference.
    * Fortunately, votekit handles a lot of the more complex work for us, so we can just follow their descriptions to set up tests.
* GerryChain is a python library that provides tools for random district generation, which may be useful for examining city council elections
    * If we want to use this library, we'll need to switch to python 3.11. It isn't supported on newer versions and the issues are deeply embedded in the code. It would be too difficult to adapt it to python 3.13 in the time we have.
* If we decide to try generating new districts, we may find the census data by Zip Code useful when constructing the initial graph of the area.
* From the paper, it seems like we won't be using the election results directly, but instead looking for info that helps us come up with values for voter participation and the like. Similarly, we won't be using candidates directly. If we follow this path, we'll basically create a baseline result and then compare that to variant results.
* It looks like we will want to use plurality elections as well as our actual elections, since doing so and comparing the results to the actual results can help establish how accurate our models are.
* I am going to go check if any of our current code breaks with this version change.

## New Setup Notes (10/19/25)
It is best practice to not include the python virtual environment within the repo, so here are the setup instructions instead.
1. Create a virtual environment inside of the repo's top level folder using python 3.11 (I'm using 3.11.13, but any 3.11 version should work)
    * You can do this following the guide [here](docs.python.org/3/library/venv.html)
    * You can also use the package manager uv, which can be downloaded [here](https://docs.astral.sh/uv/getting-started/installation/)
2. Use the requirements.txt file in the repo to download all of the necessary dependencies
3. You should now be able to run the code. If you need to install a new library, be sure to update the requirements.txt file as well.
    * Don't forget to activate the environment if you are running anything from the command line.
    * If you are using VSCode, you may need to update which python interpreter it is using for the dependency detection to work correctly.
