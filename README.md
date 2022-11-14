# deploy-impact-22-openedu-c
Repository for Team openedu-c for deploy(impact) 2022

# Project Description
TODO: project description.

All the final implementation of the project are written in python. The requirements.txt file contains the librarys needed for running our code

# File Structure

- [NLP:](https://github.com/WomenPlusPlus/deploy-impact-22-openedu-c/tree/main/NLP) This folder contains 4 python files used for related projects (similarity feature) and finding project that are related to a search-key (search feature).
  - update_database.py: updates the related projects in the database and pre-computes the project-embeddings used for search requests. The function update_database() that should be called everytime a projects in the database is modified or added. 
  - pre_process_text.py: the function is called from update_database(). It prepares the text before it can be used from the NLP model.
  - get_similarities.py: the function is called from update_database(). It takes a dataframe containing all the text information of the project and uses an NLP model to calculate an n by n matrix that tells how similar the projects are.
  - semantic_search.py: this function takes a search string, computes its embedding, loads the project embeddings from the database, and returns the the projects that are related to the search-key.
- [django_openedu:](https://github.com/WomenPlusPlus/deploy-impact-22-openedu-c/tree/main/django_openedu) cotains the implementation of a Dummy UI to test the NLP search and related projects functions. 
- [doc:](https://github.com/WomenPlusPlus/deploy-impact-22-openedu-c/tree/main/doc) Some documentation of our solution is given in this folder.

# How to run and install the project
