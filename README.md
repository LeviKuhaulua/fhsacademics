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
2. [Folder Structure](#Folder-Structure)

# Getting Started

## Django

To install your python packages, please make sure to have [pipenv](https://pipenv.pypa.io/en/latest/) installed. To do this, run the following command in your terminal: `pip install pipenv --user`. Then open the folder housing the project and run these commands

```bash
pipenv shell --> creates virtual environment for project
pipenv install --ignore-pipfile --> Downloads packages from Pipfile.lock
```

&#x2606; Pipfile.lock is important as that handles version compatibility between different packages. **If you install using the pipfile, it may download the latest version of packages, which could cause issues due to version** 

&#x2606; Highly recommend reading the pipenv CLI reference to understand what commands are available in pipenv 

&#x2606; Also have the `requirements.txt` file as an alternative to `pipenv` if it's giving you issues or you're more comfortable working with that instead

## React

1. `cd` into the *client* folder
2. Run `npm install` to install all the dependencies
3. Run `npm run dev` to start up development server


## Basic Workflow

1. Run `pipenv shell` in your terminal to load up the virtual environment 
2. In another terminal, run `npm run dev` to load up development server for front end
2. Make your changes
3. End `npm run dev` by pressing <kbd>Ctrl</kbd>+<kbd>C</kbd> (Windows) or <kbd>Ctrl</kbd>+<kbd>Z</kbd> (Mac)
4. (**If you want**) Exit your virtual environment by typing in *exit* into the terminal 



# Folder Structure

- **server/** &rarr; Django application. 
    - **core/** &rarr; Main app that holds settings, configurations, and routes
    - **announcements/** &rarr; App to handle announcement logic. 

- **client/** &rarr; React application. 
    - **node_modules/** &rarr; Helps get the React app running
    - **src/** &rarr; Holds all the react pages, react components, assets, and styles

- **public/** &rarr; Deployed frontend application.
    - **assets/** &rarr; Any assets that are available to the public such as favicon icons and pictures 
    - **dist/** &rarr; Stores the script file for each html page. 

## Important Files

**Server Side**: 

- *urls.py* &rarr; Handles routing to different apps in the project or different views in the app

- *views.py* &rarr; Logic behind what kind of HttpResponse is being returned by Django 

- *models.py* &rarr; Defines how data will be stored in your database 

- *tests.py* &rarr; Place to create your test cases for each app

- *serializers.py* &rarr; How the data gets serialized to a readable format for the client (ex. JSON)

**Client Side**: 

- *styles.css* &rarr; Tailwind CSS output to that file 

- *tailwind.css* &rarr; Defines Tailwind CSS directives that gets added into your css

