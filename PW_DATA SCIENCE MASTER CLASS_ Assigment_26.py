#!/usr/bin/env python
# coding: utf-8

# # Assignment_ 02.03.2023 ( Matplotlib)

# ## Q1. What is Matplotlib ? why it is used ? Name five plots that can be plotted using the python module of Matplotlib.
# 
# ### Ans :-
# 
#     Matplotlib is a Python library for data visualization that allows users to create a variety of static, animated, and 
#     interactive visualizations in Python. It provides a wide range of customizable plots and graphs, from simple line plots
#     to complex heatmaps and 3D plots.
#     
#     Matplotlib is used to visualize and explore data in scientific research, engineering, and business analytics. It can be
#     used to create publication-quality figures, interactive plots, and visualizations for web applications.
#     
#     There are five types of plots that can be created using Matplotlib in Python: mention in given below
#     
#     1.Line plots - Matplotlib provides various line plotting methods, such as plot(), scatter(), and stem(), to create line
#     plots. Line plots are useful for visualizing trends and patterns in data.
#     
#     2.Bar charts - Bar charts are used to represent categorical data with rectangular bars. Matplotlib provides various bar
#     plotting methods, such as bar(), barh(), and hist(), to create bar charts.
#     
#     3.Pie charts - Pie charts are used to represent data in a circular graph, with each slice of the pie representing a 
#     different category. Matplotlib provides a pie() method to create pie charts.
#     
#     4.Scatter plots - Scatter plots are used to represent the relationship between two variables. Matplotlib provides a 
#     scatter() method to create scatter plots.
#     
#     5.Heatmaps - Heatmaps are used to represent data in a 2D array format, with each cell colored according to its value.
#     Matplotlib provides a pcolormesh() method to create heatmaps.
# 

# ## Q2. What is Scatter Plot ? Use the following code to generate data for X and Y. Using this generated data plot a Scatter plot.
# 
# ### np.random.seed(3)
# ### x=3+np.random.normal(0,2,50)
# ### y=3=np.random.normal(0,2,len(x))  Note :- Also add title, xlabel and ylabel to the plot.
# 
# ### Ans:-

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


import numpy as np


# In[3]:


np.random.seed(3)
x = np.random.normal(0,2,50)
y= np.random.normal(0,2,len(x))
plt.figure(figsize=(10,6))
plt.scatter(x,y, c= '#141D93',alpha=1)
plt.xlabel("This is my x-axis")
plt.ylabel("This is my y-axis")
plt.title("This is my first Scatter plot")
plt.grid()


# ## Q3. Why is the subplot() function used? Draw the line plots using the subplot() function.
# 
# ### Use the following Data:
# ### for line 1 : x=np.array([0,1,2,3,4,5]) and y = np.array([0,100,200,300,400,500])
# ### for line 2 : x=np.array([0,1,2,3,4,5]) and y= np.array ([50,20,40,20,60,70])
# ### for line 3 : x= np.array([0,1,2,3,4,5]) and y= np.array ([10,20,30,40,50,60])
# ### for line 4 : x= np.array([0,1,2,3,4,5]) ans y = np.array([200,350,250,550,450,150])
# 
# ### Ans:-
# 
#         The subplot() function is used in Matplotlib, a popular data visualization library in Python, to create multiple 
#         plots within the same figure. It allows you to create a grid of subplots where each subplot represents a different
#         view or aspect of the data you are visualizing.
# 

# In[4]:


# Data for line 1
x1 = np.array([0,1,2,3,4,5])
y1 = np.array([0,100,200,300,400,500])
#Data for line 2
x2 = np.array([0,1,2,3,4,5])
y2 = np.array([50,20,40,20,60,70])
#Data for line 3
x3 = np.array([0,1,2,3,4,5])
y3 = np.array([10,20,30,40,50,60])
#Data for line 4
x4 = np.array([0,1,2,3,4,5])
y4 = np.array([200,350,250,550,450,150])

# creat a subplot with 1 rows and 4 columns.
fig, axs= plt.subplots(nrows=2,ncols=2,figsize=(8,6))

#Plot the first line
axs[0,0].plot(x1,y1)
axs[0,0].set_title('Line-1')

#Plot the second line
axs[0,1].plot(x2,y2)
axs[0,1].set_title('Line-2')

#Plot the third line
axs[1,0].plot(x3,y3)
axs[1,0].set_title('Line-3')

#Plot the fourth line
axs[1,1].plot(x4,y4)
axs[1,1].set_title('Line-4')

# show the plot
plt.show()





# ## What is a bar plot?why is it used?Using the following data plot and horizontal barplot.
# ### company = np.array(["Apple","Microsoft","Google","AMD")
# ### Profit = np.array([3000,8000,1000,10000)
# 
# ### Ans:-
# 
#        A bar plot is a type of data visualization that displays data using rectangular bars. The height or length of each
#        bar is proportional to the value it represents. Bar plots are used to compare different groups or categories of data.
#         
#        Bar plots are particularly useful when you want to compare the magnitudes of different quantities, or when you want 
#        to show how a quantity changes over time. They are commonly used in fields such as economics, business, and social
#        sciences to display data on sales, revenues, market shares, or survey responses.
#         
#       In a bar plot, the x-axis typically represents the categories being compared, and the y-axis represents the magnitude
#       of the values. The bars can be oriented either horizontally or vertically, depending on the nature of the data and the
#       desired visual effect.

# In[5]:


company = np.array(["Apple","Microsoft","Google","AMD"])
Profit = np.array([3000,8000,1000,10000])
plt.figure(figsize=(6,4))
plt.bar(company,Profit,color = '#BE23BC')
plt.xlabel("Companies Name")
plt.ylabel("Profite axis")
plt.title("Company Profit chat")
plt.grid()
plt.show()


# In[6]:


company = np.array(["Apple","Microsoft","Google","AMD"])
Profit = np.array([3000,8000,1000,10000])
plt.figure(figsize=(6,4))
plt.barh(company,Profit,color = '#BE23BC')
plt.ylabel("Companies Name")
plt.xlabel("Profite axis")
plt.title("Company Profit chat")
plt.grid()
plt.show()


# ## Q5. What is the box plot? why is it used?using the following data plot a box plot,
# ### box1 = np.random.normal(100,10,200)
# ### box2 = np.random.normal(90,20,200)
# 
# ### Ans:-
# 
#     A box plot, also known as a box-and-whisker plot, is a type of data visualization that provides a summary of the
#     distribution of a set of data. It is useful for detecting outliers, comparing distributions, and identifying patterns
#     or trends in the data.
#     
#     A box plot displays the range, median, quartiles, and outliers of the data in a compact format. The box in the middle 
#     of the plot represents the interquartile range (IQR), which contains 50% of the data. The median is shown as a line 
#     inside the box. The whiskers extend from the box to the minimum and maximum values that are not considered outliers.
#     Outliers, which are values that fall outside the whiskers, are shown as individual points or asterisks.

# In[7]:


# create the data for the box plots
box1=np.random.normal(100,10,200)
box2=np.random.normal(90,20,200)

# plot the box plots
plt.boxplot([box1,box2])
plt.xticks([1, 2], ['Box 1', 'Box 2'])
plt.ylabel('Value')
plt.title("Box plot")
plt.show()

