# deploy-impact-22-openedu-c
Repository for Team openedu-c for deploy(impact) 2022

# Project Description
TODO: project description.

# Additional Documents and Souce
 - [Team Board](https://miro.com/app/board/uXjVPO_hDiA=/): A Miro board where team share and organize thoughts and ideas
 - [Miro Borad](https://miro.com/app/board/uXjVPRForEg=/): Weekly Retrospective
 - [Figma](https://www.figma.com/file/gRaDjSdaGjpapaVguTvRux/OpenEdu?node-id=5%3A22&t=FF9hq4vn9oFgGKFd-1): Visual Prototype

## Context and Main Challenge

We reversed the OPENEDU website and database to identify the initial problems as follows:

1. Usability: The user cannot find information, resources or educational materials on the website
2. User experience: Information overloaded on the webpage creates cognitive loading to end users
3. Value proposition: Unclear message, target audience and offers of the website


Based on the project requirements and initial problems, we proposed three actionable solutions which are implemented within six weeks, the solutions are:

1) Refine ontology, data model and data pipeline
2) Search engine optimization with NLP approach 
3) Visual Prototype: redesign landing page, result search page and upload form

# File Structure
- [NLP:](https://github.com/WomenPlusPlus/deploy-impact-22-openedu-c/tree/main/NLP) This folder contains 4 python files used for related projects (similarity feature) and finding project that are related to a search-key (search feature).
  - update_database.py: updates the related projects in the database and pre-computes the project-embeddings used for search requests. The function update_database() that should be called everytime a projects in the database is modified or added. 
  - pre_process_text.py: the function is called from update_database(). It prepares the text before it can be used from the NLP model.
  - get_similarities.py: the function is called from update_database(). It takes a dataframe containing all the text information of the project and uses an NLP model to calculate an n by n matrix that tells how similar the projects are.
  - semantic_search.py: this function takes a search string, computes its embedding, loads the project embeddings from the database, and returns the the projects that are related to the search-key.
- [django_openedu:](https://github.com/WomenPlusPlus/deploy-impact-22-openedu-c/tree/main/django_openedu) cotains the implementation of a Dummy UI to test the NLP search and related projects functions. The Dummy UI is programmed in django using python. It is connected to a PostgreSQL database running in Azure.
- [doc:](https://github.com/WomenPlusPlus/deploy-impact-22-openedu-c/tree/main/doc) Some documentation of our solution is given in this folder.

# How to run and install the project
All the final implementation of the project are written in python. The requirements.txt file contains the librarys needed for running our code.

To run the dummy UI: go into the django_openedu folder, where the manage.py file recides, and run the command "python manage.py runserver"

To update the database: go to the NLP folder and run update_database.py
