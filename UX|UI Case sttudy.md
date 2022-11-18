# UX|UI Case Study: OPENEDU.CH

#### Optimizing use experience and web usability by redesigning search, filters and uploading file process 



## Summary

Considering the main challenges in this project, usanility, user expereince and value propostion are the main objectives we want to sovle within the project timeline. In this document, User Experience and User Interface will be addressed based on our pre define challeges.



## Overview

### About OPENEDU.CH

**OPENEDU.CH** is launched in 2020 by the WIKIMEDIA CH organization. **OPENEDU.CH** is an open education resource platform, that advocates fair education, and encourages educators to connect, collaborate and share knowledge through this platform. Through this platform, educators can benefit from accessing educational rescore on any topic, anywhere, in addition,  **OPENEDU.CH** also provides training services and tools upon request. To achieve a business goal, and build such a platform,  a strategic business analysis and data-driven approach are needed.



### The Process

After discussing the business goal and main requirement with the PO, we first reversed the existing website based on four criteria: design, structure, functionality and value to identify initial problems, then we gathered each member's feedback and extract key information to form user interview:

1. The context: In what situation educators would visit an educational resource platform

2. Behaviour: What do educators look for when visiting educational resource platforms

3. Motivation: What is the motivation for using an educational resource platform

4. Expatriation: What product/ service do you expect to see on an educational resource platform 

5. User Engagement: What is the motivation for engaging with other users on an educational resource platform 

   

To achieve the business goal, the **Double Diamond Process Model** is applied as this model is not only focus on design elements but taking a holistic view to design a system that can be run technically and visually. The Double Diamond Process Model consists of four phases as follows:

![image-20221118154658527](/Users/carol/Library/Application Support/typora-user-images/image-20221118154658527.png)

- **Discover:** 
  - Understand what is ontology; who are the key stakeholders, and how they will be affected by the ontology.
  - Reverse the existing database structure, and design, function, and service that offer on the current website  
- **Define:** 
  - Gathering insights from all team members and defining the domain and purpose of ontology and formulating the structure of the database 
  - Identify key problems that need to be addressed now. we decided to focus on optimizing searching, filtering and uploading functions.
- **Develop:** Once we define our key problems, and common goal, we divieded tasks based on member's expertise, which are **Database**, **Data science**  and **UX|UI**, and each member can focus on developing solutions
- **Delivery:** we proposed three actionable solutions which are implemented within six weeks
  - Refine ontology, data model and data pipeline
  - Search engine optimization with NLP approach 
  - Visual Prototype: redesign landing page, result search page and upload form



## 1. Discover



#### 1.1 Assesment

![image-20221118154757358](/Users/carol/Library/Application Support/typora-user-images/image-20221118154757358.png)

#### Competivie analysis

We compared existing **Open Education Resource(OER)** platforms and media sharing platform : Medium, Google Scholar, MIT, Oercommons, BC campus and Europeana and made benchmarks on information architecture, navigation, search function, filters and search results to get ideas on how to restructure OPENEDU Website.

![image-20221118154942765](/Users/carol/Library/Application Support/typora-user-images/image-20221118154942765.png)

![image-20221118151723153](/Users/carol/Library/Application Support/typora-user-images/image-20221118151723153.png)



![image-20221118151735405](/Users/carol/Library/Application Support/typora-user-images/image-20221118151735405.png)



![image-20221118151747029](/Users/carol/Library/Application Support/typora-user-images/image-20221118151747029.png)

![image-20221118151808705](/Users/carol/Library/Application Support/typora-user-images/image-20221118151808705.png)



### Persona

In addition, we also create 2 persona to get better understanding how OPENEDU.CH's user probably look like and be able to come up better solutions to tackle their problems

![img](https://lh4.googleusercontent.com/tvXnuDZW4je6-bG2Kk14wi_B7XNsdMcjJaUXIDHRrtR11v0ajQM5rHymm2g7hwgfXn3LzHA7xWVOTQ8OpZl9hC-eSGM2snHv_ww2bop0_QAl2i3RABl_CnzO7BxmsVkOuNz7T6AxqmTUaw6IrmcMMOxgRfcL6LBRCVEspUgslQ8LYZGYZSFXMOo8PwC1HRvC)



### **User Jounrey and Interview**

We mapped out user journey based on the persona profile and designed eight open questions as follows:

![image-20221118155333373](/Users/carol/Library/Application Support/typora-user-images/image-20221118155333373.png)



**Usage of the educational platform**

1. When you go to the educational platform, what was your goal/task that makes you visit these sites (the sites you provided)?
2. What functions help you to complete your tasks
3. What struggle you during the process, and what can help you to complete your tasks

**Uploading / sharing your work on an educational platform**

1. How much time would you like to invest in the uploading process including registering as a user and filling out an information sheet?
2. IF you have uploaded files on an educational platform (or any platform), what struggle did you have during the process, and what can help you to complete your tasks?

**Collaboration & networking on an educational platform**

1. What would motivate you to sign up as a member of an educational platform?
2. What would you expect this platform can offer you?
3. How would you like to interact with other educators?

we conducted user interviews with 5 potential users (one internal and 4 external users.

- 90 % of the Users search bar to start their search on the majority platform
- Online Community, Peer review and students feedback are critical touchpoints
- Having a clear instructions and guidance would help the user to complete the uploading process
- Users wishing to get in touch with other teachers and connect in a simple, easy way



## Define

We collected ideas from team brainstorming, user interview and and competitive analysis, and we finally selected the most prominent features which are: **Search UI**, **Filters**, **Uploading Form**, and **Redesign Landing page** that are aligned with solution from our technical team, and be able to visualize in the final prototype



### Develop

At this stage, we compiled potential solutions and we selected the most reasonable ideas to develop. Here are the decisions:



| Features                 | Actions                                                      | Impact                                                       | Decision |
| ------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | -------- |
| **Search bar**           | 1.Enlarge and ceterned this feature in the landing page <br />2.Implement autocomplete function for key word search | Visible search UI especially on website with heavy information can help user to find content easily | Approved |
| **Filters**              | 1.Rename unclear or confuse filters<br />2.Remove overladped filters<br />3. Applied dropdown function on the filters<br />4. Applied Use vertical filters section help user to prioritize tasks they wish to do on the site | Eliminate uncertainty and confusion that can deter users motivation to use the website | Approved |
| **Uploading Form**       | 1. Reduce user effort in the input fileds<br />2. Simplify uploading process with an indication and procedure<br />3. Tooltips | Reduce the obstacle and potential drop out during the process | Approved |
| **Website Landing page** | 1. Reduce information overload<br />2. Create **a clear message**: how people who you are, what do you do and what offers they can expect when visiting the website<br />3.Highlight<br/>**Call-to-Action** button to encourage users engagement | Building trust and connection users                          | Approved |



#### User Flow

After we define the key features, I designed the user flow of the search and file uploading process.

![image-20221118151600076](/Users/carol/Library/Application Support/typora-user-images/image-20221118151600076.png)

### Prototype

Many users expect what they believe will interact with the product and service and therefore, making the website similar to their competitor can help users to easily navigate on the site without hesitating. In the design phase, we implemented the Mental model and design principle to reduce the cognitive loading on the web page and create pleasant experiences for the user, as well as help them to easily navigate on the website.

<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FgRaDjSdaGjpapaVguTvRux%2FOpenEdu%3Fnode-id%3D5%253A22%26t%3DyiTU9HblL70df30C-1" allowfullscreen></iframe>



- **Redesigning landing page**
  - Core message:  a short and power slogan tell users Who we are, what we do and what service and products offers on this site
  - Enlarge Search UI: make the search bar visible
  - CTA button: invite people to sign up and explore the site
  - Clear navigation: make the navigation visible to navigate users to visit different pages

[![img](https://lh3.googleusercontent.com/97dOeRtHV7AD-R0YNz-z-SE7aBWk2fnT5W7TcoOccgvcmH31_7PtIVMWG_QuLAogYYCXhJfXtwL9bwlHBbjVEk0NgdQ4PAdADp4SC8JheTc-0Cvj5Gsg9ZgkQdL8Kfb3nFXgboVPwaXxyGoMaFrSbcmpXEk6wErgm-6disbCU2J_TlrbhU8O6H7ZGN_w6i1_)](https://www.figma.com/file/gRaDjSdaGjpapaVguTvRux/OpenEdu?node-id=5%3A22)

- **Resource page: Use Dropdown animation in the filter feature**

  ![img](https://lh6.googleusercontent.com/xOA2ED_VHJmRGnAjH436G8W5Zt6G23NFq54AJWLf04PC0QnlbANvcT0qjipPve8AHJWC_wZbxxKuNbI23kOrFrzN97tMB9cPfOHOtxBN8C9N6X0sUzQN9dwPnf6PxFmya_mz-_SwpAgcOCs4RXFhoduKJC3rQf8aJ4lCHVckbIkzFehruBlTz4n-oRT9kWyk)

  

- **Sign up pages**

In the sign up page, we want to collect more user basic information, not just their name and email. However, to make the user feel comfortable and share their information with us, we implemented some tags and a drop down menu to help users to fill out their information in a simple way. 





- **Uploading Pages**

We make the uploading form simpler and divide the process into four steps, to make the user informed and know which section they are and be able to estimate how much time they need to complete this task.

![img](https://lh4.googleusercontent.com/APi-MYmVZ-WeekbvVPBE7oLnjKXLPNL8JMZ0tbO8z-gcRdXZKCJXUhdRLMh-pro42DIuavf1CBetcjgu3XJtzVHdpsbCjiH8YglKyC-laduHqoWtfqu0YDzeBkLBgkha5-qs3QoxGF93JL_dFKHNZ0BmIZ9Pq9cOQDWjGNC7neFIRYg5yjesefImQdmWrrA3)

![img](https://lh4.googleusercontent.com/ao0jT7LZFXcTHhrCSygm4zecjOGJrZK7gnkG6lErcJZx8yilnMbamZpFKgM9tmfZPyj9g1cHZXt0HhSQ1G63PAbtKx210TQyTwKHaVItu0sDwjtAjlXCaVCHeLY-1MPuoZU6LouN-73S8kZZDmqOoSZDYK3EVfdWjsykfLtfARgh5xSvrGzTFFDX0xamgHRx)

![img](https://lh6.googleusercontent.com/GURvvfMAfN43OAVh5tlCex84W47sRobat0kgUrDivIyuFAlcz4njYc2WhZ3aWuDusGt8BoM-tOyvjAJqq_umY8za1ZkO8dFDDhOS4SqdOisJX_j8z2wRpnjrQwS4sRRHTUvO0TIVcpOYmN6boEk11lcRO1GgIGJKG8kYPkjKttZhxsfmEcuWvGcv_tN3OcYP)

![img](https://lh5.googleusercontent.com/LjMGt_eS6u5Xbl1SDVVL7BdjnDWFDR8KgUBP7YfC8VOw3_qka5Ce4tcT4G3SmPTwcaSb-wAQwnojY3PUBe7BLTonpNvYszzHP_Oterhp9feu9G3UpC7eAGCxZpulux2YvNKqNl5ELielakTC4-sl6mlISMcQCDOZ-QHrtJfYVpwETRpxuvXNFYhFpm85PqUP)



### Go to the Market

Now that we had achieved the outcome. our team also design and pitch desk to support the launch of these exciting features that we have developed over the past six week.

### Reflection

The purpose for this project is to provide tangible and actionable solutions for the client, although the redesign website was not required by the people, we believe having a website prototype that can visualize our solution in a feasible way is more convincing when pitching our idea, There were some flaws in the process and improvement that need to be addressed accordingly based on the data collection in the future development. 





