# UCS_Voting_Repo
A repository that stores the programs used to examine and analyze how election results might change with different methods of Proportional Representation. This is part of the UCS voting project, meant to help inform people about Proportional Representation, examining different methods and how they might influence the outcome of elections.

## Setup Notes
It is best practice to not include the python virtual environment within the repo, so here are the setup instructions instead.
1. Create a virtual environment inside of the repo's top level folder using python 3.13 (I'm using 3.13.7, but any 3.13 version should work)
    * You can do this following the guide [here](docs.python.org/3/library/venv.html)
    * You can also use the package manager uv, which can be downloaded [here](https://docs.astral.sh/uv/getting-started/installation/)
2. Use the requirements.txt file in the repo to download all of the necessary dependencies
3. You should now be able to run the code. If you need to install a new library, be sure to update the requirements.txt file as well.
    * Don't forget to activate the environment if you are running anything from the command line.
    * If you are using VSCode, you may need to update which python interpreter it is using for the dependency detection to work correctly.

## Design Notes
* I don't see any built in methods that create ballots with real world data then fill in rankings with a ballot generator. If we want to force each sample set to use the real world vote results as top choices, we might need to create our own method of generating a preference profile.
* The ballot generators can generate ballots with ties. We'll need to decide how to resolve these ties to actually run elections on them.

## Additional Notes
* The placeholder.txt files are there because we can't add empty folders to a repo. We should remove them once we add any file to a folder.
* The Bradley-Terry MCMC generator breaks if a bloc will only vote for a single candidate. This shouldn't be an issue in any real tests.
* I found a bug in VoteKit's STV election method. In line 93 of stv.py, the code uses an incorrect numpy array method. However, this line is only used when printing a value error, so it shouldn't cause any issues (I'll still look into flagging it for a library update.)