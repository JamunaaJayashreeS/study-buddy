#!/usr/bin/env python
# coding: utf-8

# In[5]:


# !pip install sqlite3
import sqlite3

conn = sqlite3.connect('Studybuddy.db')
cur = conn.cursor()
cur.execute('DROP TABLE users')
cur.execute('''CREATE table users (UTA_ID INTEGER PRIMARY KEY NOT NULL, User_Name TEXT,
                                                 Dept_name TEXT, Intake_year INTEGER, Intake_term TEXT, Mail_ID TEXT)''')


# In[6]:


cur.execute('''INSERT INTO  users (UTA_ID, User_Name,
                                                 Dept_name, Intake_year, Intake_term, Mail_ID ) 
                                                 values(1002034156,'Manasa12','Business',2022,'Spring','mxg4156@mavs.uta.edu')''')


# In[7]:


cur.execute('''INSERT INTO  users (UTA_ID, User_Name,
                                                 Dept_name, Intake_year, Intake_term, Mail_ID ) 
                                                 values(1001966627,'Jamunaa','CSE',2022,'Spring','jxs6627@mavs.uta.edu')''')


# In[8]:


cur.execute('''INSERT INTO  users (UTA_ID, User_Name,
                                                 Dept_name, Intake_year, Intake_term, Mail_ID ) 
                                                 values(1002042661,'Shreethika','CSE',2022,'Spring','sxs2661@mavs.uta.edu')''')


# In[23]:


cur.execute('DROP TABLE users_profile')
cur.execute('PRAGMA foreign_keys = ON')

cur.execute('''CREATE table users_profile (UTA_ID INTEGER PRIMARY KEY NOT NULL, Degree TEXT,
                                                 Dept_name TEXT, LinkedIN TEXT, Github TEXT, Area_of_Interests 
                                                 TEXT,projects TEXT,Tutoring BOOLEAN,Looking_for_Study_group BOOLEAN,
                                                 Course_ID TEXT,
                                                 FOREIGN KEY(UTA_ID) REFERENCES Books(users),
                                                 FOREIGN KEY(Course_ID) REFERENCES Books(Courses))''')


# In[24]:


cur.execute('''INSERT INTO  users_profile (UTA_ID , Degree ,
                                                 Dept_name , LinkedIN , Github, Area_of_Interests, 
                                                projects ,Tutoring,Looking_for_Study_group,Course_ID)
                                                 values (1002034156,'Masters','Business',
                                                 'https://www.linkedin.com/in/manasa-gonuguntla29/',
                                                 'https://github.com/Manasa-1229',
                                                 'Data preprocessing Data Analytics and  Data Science', 
                                                 'Cyberbulling and Airline customber satisfaction','TRUE','False','INSY5378')''')


# In[25]:


cur.execute('''INSERT INTO  users_profile (UTA_ID , Degree ,
                                                 Dept_name , LinkedIN , Github, Area_of_Interests 
                                                ,projects ,Tutoring,Looking_for_Study_group,Course_ID)
                                                 values (1001966627,'Masters','CSE',
                                                 'https://www.linkedin.com/in/jamunaa-jayashree-selvaprabhu/',
                                                 'https://github.com/JamunaaJayashreeS',
                                                 'Software Enigineer & cybersercurity', 
                                                 'Graph visualization & max node connection','False','TRUE','CSE5301')''')


# In[26]:


cur.execute('DROP TABLE Courses')
cur.execute('''Create table Courses(Course_ID TEXT PRIMARY KEY NOT NULL, Course_name TEXT, Dept_name TEXT ) ''')


# In[16]:


cur.execute('''INSERT INTO Courses(Course_ID, Course_name, Dept_name) values ('CSE5301','DAMT','CSE')''')


# In[17]:


cur.execute('''INSERT INTO Courses(Course_ID, Course_name, Dept_name) values ('INSY5378','Data Science','Business')''')


# In[ ]:


cur.execute('''IF NOT EXISTS 
    (SELECT User_Name  
     FROM users
     WHERE User_Name = 'LoginName')
BEGIN
    CREATE LOGIN [LoginName] WITH PASSWORD = N'password'
END''')

