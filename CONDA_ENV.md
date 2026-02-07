## How to set up a conda environment for this project
1. Install the Anaconda distribution from https://www.anaconda.com/. You will need to make an account or sign in with google in order to download it.
    * You can use either miniconda or the full distribution. The full distribution will let you create environments more quickly but will take longer to install and uses more memory.
2. Open the anaconda terminal, or activate anaconda in your default terminal
3. Navigate to the UCS Voting repo folder, where the environment.yaml file is stored.
4. Run the command "conda env create --name UCS_Voting --file environment.yaml" in your terminal
5. You should then be able to set the environment as the interpreter in VS code by clicking on the python version in the bottom left corner.
6. If you prefer to run code in the terminal, you can activate the environment with the command "conda activate UCS_Voting"