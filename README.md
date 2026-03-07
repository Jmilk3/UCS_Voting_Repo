# UCS_Voting_Repo
A repository that stores the programs used to examine and analyze how election results might change with different methods of Proportional Representation. This is part of the UCS voting project, meant to help inform people about Proportional Representation, examining different methods and how they might influence the outcome of elections.

See our report on our findings here: LINK TO REPORT

## Navigating the Repository
### Data Folders
* The 'Raw Data' folder contains the complete, original data that we used for this project.
* The 'Clean Data' folder contains the modified, cleaned, and split data which we used when actually running ER.

### Result Folders
* The ER_Results folder has the output graphs and text results from running ER, split by city.
* The Simulation_Results folder has the election outcomes and ballot distributions from our various simulations

### Code Folder
* The code folder has all of the actual code used during this project, split by what the code was used for.

## Running the Code
### Setting up the Python environment
We used Anaconda to install and manage packages. The following instructions explain how to setup the environment so that you can run our code locally.
1. Install the Anaconda distribution from https://www.anaconda.com/. You will need to make an account or sign in with google in order to download it.
    * You can use either miniconda or the full distribution. The full distribution will let you create environments more quickly but will take longer to install and uses more memory.
2. Open the Anaconda terminal, or activate Anaconda in your default terminal
3. Navigate to the UCS Voting repo folder, where the environment.yaml file is stored.
4. Run the command "conda env create --name UCS_Voting --file environment.yaml" in your terminal
5. Activate the environment with the command "conda activate UCS_Voting", then you can run our python scripts from the command line.

### A note on filepaths
In the process of making the repository easier to navigate, we moved a lot of our csv files around. Any csv that is named in a script is still present in the repository, but the file path may have changed. Please check the file paths of any existing file prior to using the code. It is also worth noting that many functions will output all files in the same place. These output files will then need to be sorted manually. 
