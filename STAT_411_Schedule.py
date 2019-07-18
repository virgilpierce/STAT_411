#!/usr/bin/env python
# coding: utf-8

# In[62]:


import pandas as pa
import datetime as dt
pa.set_option('max_colwidth', 200)


# In[63]:


first_day = dt.date(2019, 8, 27)


# In[64]:


holidays = [dt.date(2019, 9, 2) ]
thanksgiving_start = dt.date(2019, 11, 27)
thanksgiving_end = dt.date(2019, 12, 1)
thanksgiving_delta = thanksgiving_end - thanksgiving_start
holidays += [thanksgiving_start + dt.timedelta(i) for i in range(thanksgiving_delta.days+1)]


# In[65]:


last_day = dt.date(2019, 12, 5)


# In[66]:


final_exam = dt.date(2019, 12, 11)


# In[67]:


semester_length = last_day - first_day


# In[68]:


class_days = []
for i in range((semester_length.days //7 + 1)):
    class_days += [first_day + dt.timedelta(i*7), first_day + dt.timedelta(i*7+2)]
class_days += [final_exam]


# In[69]:


schedule = pa.DataFrame(class_days, columns = ['Day'])
weekday_dict = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
for i in range(schedule.shape[0]):
    schedule.loc[i,'Week_Day'] = schedule.loc[i, 'Day'].weekday()
schedule.Week_Day = schedule.Week_Day.map(weekday_dict)


# In[70]:


for holiday in holidays:
    schedule.loc[schedule.Day==holiday, 'Title'] = 'No Class - University Holiday'


# In[71]:


def add_day(title='', description='', notes=''):
    global schedule
    global day
    
    while schedule.loc[day, 'Day'] in holidays:
        day += 1
    if day >= schedule.shape[0]:
        print('Error to many days')
        return 'ERROR'
    else:
        schedule.loc[day, 'Title'] = title
        schedule.loc[day, 'Description'] = description
        schedule.loc[day, 'Notes'] = notes
        
        day += 1
    


# In[72]:


day = 0

add_day('Course Introduction', 'What is Data Science?')

add_day('Motivating Examples', 'What kinds of questions can we ask?')

add_day('Data', 'What is data, where to get it?')

add_day('Team - Forming Teams', 'Deciding how we will divide up into teams', 'Team Day 1')

add_day('Tools of the Trade', 'Python / Jupyter Basics, Importing and Exporting Data,'+                       'Development and Version Control')

add_day('The Data Science Process', 'Controlling for Error, Professional ethics')

add_day('Team - Proposal', "Developing your team's proposal", 'Team Day 2')

add_day('Wrangling the Data - 1', 'Formating the data, dealing with numerical data, '+                       'dealing with categorical data, dealing with missing data, dealing with strings, '+                       'dealing with images*')

add_day('Exploratory Data Analysis', 'Plots with seaborn, summary statistics, background '+                        'on linear regression', 'Linear regression is our first model')

add_day('Principal Component Analysis', 'Singular value decomposition and principal component analysis', 
       'The most important fact from Linear Algebra')

add_day('Team - Wrangling and Exploring YOUR Data', "Taking a look at the team's data - identifying and dealing "+        'with issues, looking at plots', 'Team Day 3')


add_day('Statistical Learning and Models', 'Review of the Data Science workflow, '+                       'boostrapping our data, building our model - linear regression, testing our model')

add_day('K-Nearest Neighbors', 'K-Nearest Neighbors for regression and categorization', 
                       'Building the actual model, plotting and testing the results.')

add_day('Team - K-Nearest Neighbors', 'Building K-Nearest Neighbors for your data', 'Team Day 4')

add_day('A Zoo of Models for Regression', 'Nonlinear regression, Ridge, and Lasso Methods', 
                       'Different types of errors and plotting results')

add_day('A Zoo of Models for Categorization - 1', 'Linear Discriminant Analysis, Support Vector Machines')

add_day('Team - Modeling your data - 1', 'Digging Deeper into modeling your data', 'Team Day 5')

add_day('A Zoo of Models for Cateogrization - 2', 'Decision Trees, and exploring lots of examples')


add_day('Team - Modeling your data - 2', 'Digging Deeper into modeling your data', 'Team Day 6')

add_day('Team - Presentations - A', 'Preliminary Reports and Presentations from the teams', 'Team Day 7')

add_day('Ensembles of Models, and Neural Networks', 'Avoiding overfitting and advanced ideas')

add_day('Team - Modeling your data - 3', 'Digging Deeper still into modeling your data', 'Team Day 8')

add_day('Unsupeervised Learning', 'Examples of unsupervised learning')

add_day('Team - Modeling your data - 4', 'Digging Deeper still into modeling your data', 'Team Day 9')

add_day('Advanced Topics - 1', 'Spatial Data')

add_day('Team - Preparing Reports', 'Putting it all together', 'Team Day 10')

add_day('Advanced Topics - 2', 'Text Mining and AI')

add_day('Team - Preparing Reports', 'Putting it all together', 'Team Day 11')

add_day('Advanced Topics - 3', 'Big data, big iron, and parallel processing')

add_day('Team - Final Presentations', '8am - 10:30am', '35 minutes per team + 15 minutes for questions')

schedule


# In[ ]:




