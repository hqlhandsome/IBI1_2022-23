import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#This imports the necessary libraries for the code: os, pandas, matplotlib.pyplot, and numpy.
os.chdir("/Users/mr.he/Downloads")
#This sets the working directory to the "Downloads" folder in the user's directory.
covid_data=pd.read_csv ("full_data.csv")
#This reads a file called "full_data.csv" and stores it in a Pandas DataFrame called covid_data.
print(covid_data.head(5))
#This prints the first five rows of the covid_data.
#         date     location  new_cases  new_deaths  total_cases  total_deaths
#0  2019-12-31  Afghanistan          0           0            0             0
#1  2020-01-01  Afghanistan          0           0            0             0
#2  2020-01-02  Afghanistan          0           0            0             0
#3  2020-01-03  Afghanistan          0           0            0             0
#4  2020-01-04  Afghanistan          0           0            0             0
covid_data.info()
#This prints information about the covid_data, such as the number of rows and columns, data types, and memory usage.
#<class 'pandas.core.frame.DataFrame'>
#RangeIndex: 7996 entries, 0 to 7995
#Data columns (total 6 columns):
 ##   Column        Non-Null Count  Dtype
#---  ------        --------------  -----
 #0   date          7996 non-null   object
 #1   location      7996 non-null   object
 #2   new_cases     7996 non-null   int64
 #3   new_deaths    7996 non-null   int64
 #4   total_cases   7996 non-null   int64
 #5   total_deaths  7996 non-null   int64
#dtypes: int64(4), object(2)
#memory usage: 374.9+ KB
print(covid_data.describe())
#This prints descriptive statistics of the numerical columns in the covid_data, such as count, mean, standard deviation, minimum, and maximum.
#         new_cases   new_deaths    total_cases  total_deaths
#count   7996.000000  7996.000000    7996.000000   7996.000000
#mean     194.546773     9.322661    2441.369060     97.977239
#std     2083.395028   108.183439   22375.617031   1023.038977
#min       -9.000000     0.000000       0.000000      0.000000
#25%        0.000000     0.000000       0.000000      0.000000
#50%        0.000000     0.000000       3.000000      0.000000
#75%        8.000000     0.000000      60.000000      0.000000
#max    65162.000000  3698.000000  777798.000000  37272.000000
print(covid_data.iloc[0:1001:100,1])
#This prints the values in the second column of the covid_data DataFrame for every 100th row between row 0 and row 1000.
#0       Afghanistan
#100         Albania
#200         Andorra
#300         Armenia
#400       Australia
#500         Austria
#600      Azerbaijan
#700         Bahrain
#800         Belarus
#900         Belgium
#1000        Bolivia
#Name: location, dtype: object
my_columns = [True, True, False, True, False, False]
print(covid_data.iloc[0:3,my_columns])
#This creates a list of Boolean values to select specific columns of the covid_data and prints the selected columns for the first three rows.
## date     location  new_deaths
#0  2019-12-31  Afghanistan           0
#1  2020-01-01  Afghanistan           0
#2  2020-01-02  Afghanistan           0
print(covid_data.loc[0:81, "total_cases"])
#This prints the values in the "total_cases" column of the covid_data DataFrame for rows 0 to 81.
#0       0
#1       0
#2       0
#3       0
#4       0
#    ...
#77     75
#78     91
#79    106
#80    114
#81    141
#Name: total_cases, Length: 82, dtype: int64
covid_data['afh'] = (covid_data['location'] == 'Afghanistan')
print(covid_data.loc[covid_data['afh'] == True,"total_cases"])
#This prints the values in the "total_cases" column of the covid_data DataFrame for rows named "Afghanistan"
#0       0
#1       0
#2       0
#3       0
#4       0
#    ...
#77     75
#78     91
#79    106
#80    114
#81    141
#Name: total_cases, Length: 82, dtype: int64
covid_data['20200331'] = (covid_data['date'] == '2020-03-31')
new_data = covid_data.loc[covid_data['20200331'] == True,["location","new_cases","new_deaths"]]
a = new_data['new_cases'].values.astype(float)
b = new_data['new_deaths'].values.astype(float)
column_a = np.mean(a)
column_b = np.mean(b)
print(column_a,column_b)
#This creates a new column in the covid_data called "20200331" that contains Boolean values indicating whether the "date" column equals "2020-03-31".
#It then creates a new DataFrame called "new_data" that contains the "location", "new_cases", and "new_deaths" columns for rows where "20200331" is True.
# It calculates the mean of the "new_cases" and "new_deaths" columns in "new_data" and prints the results.
#the mean number are 640.4615384615385 and 37.92820512820513
labels = 'new_cases'
#Assigning the label for the box plot to new_cases.
new_cases20200331 = new_data["new_cases"]
#Creating a new variable new_cases20200331 to store the data for the new_cases column.
plt.boxplot(new_cases20200331)
#Creating a box plot for the new_cases data using Matplotlib's boxplot() function.
plt.show()
#Show the box plot.

labels = 'new_deaths'
#Assigning the label for the box plot to new_deaths.
new_deaths20200331 = new_data["new_deaths"]
#Creating a new variable new_deaths20200331 to store the data for the new_deaths column.
plt.boxplot(new_deaths20200331)
#Creating a box plot for the new_deaths data using Matplotlib's boxplot() function.
plt.show()
#Show the box plot.
world_dates=covid_data['date']
#Assigning the column 'date' from the 'covid_data' dataset to a new variable called 'world_dates'.
world_new_cases=covid_data['new_cases']
#Assigning the column 'new_cases' from the 'covid_data' dataset to a new variable called 'world_new_cases'.
world_new_deaths=covid_data['new_deaths']
#Assigning the column 'new_deaths' from the 'covid_data' dataset to a new variable called 'world_new_deaths'.
plt.plot(world_dates, world_new_cases, 'b+')
# plot a line graph with blue plus markers for the x-values in 'world_dates' and y-values in 'world_new_cases'.
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90,fontsize=4)
#set the x-axis tick labels to occur at every fourth data point, with the labels being rotated -90 degrees and with a font size of 4.
plt.plot(world_dates, world_new_deaths, 'r+')
#plot a line graph with red plus markers for the x-values in 'world_dates' and y-values in 'world_new_deaths'.
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90,fontsize=4)
#set the x-axis tick labels to occur at every fourth data point, with the labels being rotated -90 degrees and with a font size of 4.
plt.show()
#show the final plot


#How have new cases and total cases developed over time in the UK?
covid_data['UK'] = (covid_data['location'] == 'United Kingdom')
#This creates a new column named "UK" in the covid_data, which contains True for rows where the "location" column equals "United Kingdom"
data_UK = covid_data.loc[covid_data['UK'] == True,["date","new_cases","total_cases"]]
#This selects rows from the covid_data where the "UK" column is True, and only keeps the "date", "new_cases", and "total_cases" columns. The resulting DataFrame is assigned to data_UK.
UK_dates=data_UK['date']
#This creates a new variable named UK_dates, which contains the "date" column from the data_UK
UK_new_cases=data_UK['new_cases']
#This creates a new variable named UK_new_cases, which contains the "new_cases" column from the data_UK
UK_total_cases=data_UK['total_cases']
#This creates a new variable named UK_total_cases, which contains the "total_cases" column from the data_UK
plt.plot(UK_dates, UK_new_cases, 'b')
# plot a line graph with blue markers for the x-values in 'UK_dates' and y-values in 'UK_new_cases'.
plt.xticks(UK_dates.iloc[0:len(UK_dates):4],rotation=-90,fontsize=4)
# set the x-axis tick labels to occur at every fourth data point, with the labels being rotated -90 degrees and with a font size of 4.
plt.plot(UK_dates, UK_total_cases, 'r')
# plot a line graph with blue markers for the x-values in 'UK_dates' and y-values in 'UK_total_cases'.
plt.xticks(UK_dates.iloc[0:len(UK_dates):4],rotation=-90,fontsize=4)
# set the x-axis tick labels to occur at every fourth data point, with the labels being rotated -90 degrees and with a font size of 4.
plt.show()
# Show the final plot
