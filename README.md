# FHS Academics

Purpose: To help students at Farrington High School understand what is the Advanced Placement (AP) program, and 
how that can help prepare them for college. Students will learn the following: 

- What exactly is AP? 
- How does AP prepare them for college and how is it beneficial? 
- What AP classes are offered at Farrington? 
- Any announcements / events associated with AP. 

<br> 

# Table of Contents

1. [Getting Started](#Getting-Started)


# Getting Started

To install your python packages, please make sure to have [pipenv](https://pipenv.pypa.io/en/latest/) installed. To do this, run the following command in your terminal: `pip install pipenv --user`. Then open the folder housing the project and run these commands

```bash
pipenv shell --> creates virtual environment for project
pipenv install --ignore-pipfile --> Downloads packages from Pipfile.lock
```

&#x2606; Pipfile.lock is important as that handles version compatibility between different packages. **If you install using the pipfile, it may download the latest version of packages, which could cause issues due to version** 

&#x2606; Highly recommend reading the pipenv CLI reference to understand what commands are available in pipenv. 

## Basic Workflow

1. Run `pipenv shell` in your terminal to load up the virtual environment 
2. Do whatchu need to do
3. (**If you want**) Exit your virtual environment by typing in *exit* into the terminal. 

