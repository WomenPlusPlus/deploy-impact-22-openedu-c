# deploy-impact-22-openedu-c
Repository for Team openedu-c for deploy(impact) 2022

Contact person for Wikimedia: 
danielapavia@gmail.com  (technical part)
iwona.braun@gmail.com (project management part)

# Project Description
OpenEdu is an open education platform launched in 2020 by wikimedia CH.  
Open education platforms allow their users to edit and integrate projects, training tools and news from the world of open education. The goal of the platform is to help educators in the orientation towards finding inspiration for new teaching methodologies or professional updating.
We started a 6-week project on OpenEdu in order to make it more effective and efficient while allowing the user to enjoy using the platform. Our main task was to propose an ontology for storing content metadata, as well as to propose a complete data architecture. The client also wanted us to review and suggest solutions for the uploading procedure. 
Our main challenge in the first phase (discovery) phase was understanding the current OpenEdu structure and its functionalities.

Once the understanding of OpenEdu was clearer and the possible areas of improvements were defined to make the platform more effective and efficient, the approach was focused on the following challenges & end user’s needs and problems:
Usability: It is difficult for the user to find information, resources, or educational material on the website
User experience: The Interface of the website is overloaded creating cognitive load to the end user
Value proposition: The aim of the website does not send a clear message

In order to maximize the user experience and provide them with an easy to use platform, we proposed the following solutions to improve the website:
1. We developed an ontology to provide the database with a better structure with the intention of easing the data collection and data processing.
2. We optimized the Search feature of the website and the related content feature related to the search that has been done.
3. We maximized the user experience by reducing information on landing page and on a better way to ease the uploading process of new projects.


# Additional Documents and Souce
 - [Team Board](https://miro.com/app/board/uXjVPO_hDiA=/): A Miro board where team share and organize thoughts and ideas
 - [Miro Board](https://miro.com/app/board/uXjVPRForEg=/): Weekly Retrospective
 - [Presentation](https://www.canva.com/design/DAFRclqQvVc/WA8bONken9AouR8n8UpdqQ/view?utm_content=DAFRclqQvVc&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink): Our pitch presentation you can view in Canva or [Google Drive](https://docs.google.com/presentation/d/1YGaBBD5dSjZfEWSn8VzBD_vT51LJrYkO/edit?usp=share_link&ouid=113270707159335923135&rtpof=true&sd=true)

## Context and Main Challenge

We reversed the OPENEDU website and database to identify the initial problems as follows:

1. Usability: The user cannot find information, resources or educational materials on the website
2. User experience: Information overloaded on the webpage creates cognitive loading to end users
3. Value proposition: Unclear message, unclear target audience and what the website offers


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
- [UX|UI:](https://github.com/WomenPlusPlus/deploy-impact-22-openedu-c/blob/main/UX%7CUI.md) documents design process of the visual prototype
- [doc:](https://github.com/WomenPlusPlus/deploy-impact-22-openedu-c/tree/main/doc) Our description of the project, more documentation of the solution and summary. 

# How to run and install the project
All the final implementation of the project are written in python. The requirements.txt file contains the librarys needed for running our code.

To run the dummy UI: go into the django_openedu folder, where the manage.py file recides, and run the command "python manage.py runserver"

To update the database: go to the NLP folder and run update_database.py

# Website Prototype
 - [Visual Prototype:](https://www.figma.com/proto/gRaDjSdaGjpapaVguTvRux/OpenEdu?page-id=0%3A1&node-id=5%3A22&viewport=-43%2C-199%2C0.13&scaling=scale-down-width&starting-point-node-id=5%3A22) a Figma file where you can interact with the website prototype
There are three main features you can test:
1. Search bar: try to entry "scie" and click science competetion to see the search result
2. Filters: a list of dropdown menu that user can interacte with
3. Sign up and uploading form: once you click sign up, it will guide you through the sign up and add file processes
