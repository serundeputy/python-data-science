import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd


df = pd.read_csv(
    'Refactored_Py_DS_ML_Bootcamp-master/10-Data-Capstone-Projects/911.csv')

# print(df.info())

# Basic questions

## What are the top five zipcodes for 911 calls?
print(df['zip'].value_counts().head(5))

## What are the top 5 townshops for 911 calls?
print(df['twp'].value_counts().head(5))

## How many unique title codes are there?
print(len(df['title'].unique()))

## Create a new feature on df called 'Reason'
print(df['title'].head(1))
df['Reason'] = df['title'].apply(
        lambda this: this.split(':')[0]
        )
print(df['Reason'].head(4))

## What is the most common reason for a 911 call?
print(df['Reason'].value_counts().head(3))

## Create a countplot of 911 calls by reason.
# sns.countplot(x = 'Reason', data = df)
# plt.show()
# exit()

## What is the data type of the objects in the timeStamp column?
print(type(df['timeStamp'].head(1)[0]))

## Convert timeStamp col to date_times.
df['Date'] = pd.to_datetime(df['timeStamp'])

## Create 3 new cols called Hour, Month, and Day of Week.
df['Hour'] = df['Date'].apply(
        lambda this: this.hour)

df['Month'] = df['Date'].apply(
        lambda this: this.month)

df['Day of Week'] = df['Date'].apply(
        lambda this: this.dayofweek)
## This is how I did it.
# def mapDayNumsToNames(num):
#     dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
#     return dmap[num]
# df['Day of Week'] = list(
#         map(
#             mapDayNumsToNames,
#             df['Day of Week'])
#         )
## From solutions.
dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['Day of Week'] = df['Day of Week'].map(dmap)
# print(df.head())
# exit()

## Create a countplot of the Day of the Week with hue based on Reason col.
# sns.countplot(x = 'Day of Week', data = df, hue = 'Reason', palette = 'viridis')
# plt.legend(bbox_to_anchor = (1.05, 1), loc = 2, borderaxespad = 0)
# plt.show()
# exit()

# sns.countplot(x = 'Month', data = df, hue = 'Reason', palette = 'viridis')
# plt.legend(bbox_to_anchor = (1.05, 1), loc = 2, borderaxespad = 0)
# plt.show()
# exit()

byMonth = df.groupby(['Month']).count()
# sns.lineplot(x = 'Month', y = 'e', data = byMonth) 
# plt.show()
# exit()

## Create a linear fit.
# byMonth['Month'] = byMonth.index
# print(byMonth.info())
# sns.lmplot(x = 'Month', y = 'e', data = byMonth)
# plt.show()
# exit()

df['Date'] = df['Date'].apply(
        lambda this: this.date())
# print(df['Date'].head())
# exit()
byDate = df.groupby(['Date']).count()
byDate['Date'] = byDate.index
byDate = byDate.sort_values('timeStamp')
# print(byDate.head())
# exit()
# g = sns.lineplot(x = 'Date', y = 'e', data = byDate)
# g.set_title('911 Calls by Date')
# g.set_ylabel('Count')
# for item in g.get_xticklabels():
#     item.set_rotation(45)
# plt.tight_layout()
# plt.show()
# exit()

# Reasons.
traffic = df[df['Reason'] == 'Traffic']
trafficByDate = traffic.groupby(['Date']).count()
trafficByDate['Date'] = trafficByDate.index
trafficByDate = trafficByDate.sort_values('timeStamp')

fire = df[df['Reason'] == 'Fire']
fireByDate = fire.groupby(['Date']).count()
fireByDate['Date'] = fireByDate.index
fireByDate = fireByDate.sort_values('timeStamp')

ems = df[df['Reason'] == 'EMS']
emsByDate = ems.groupby(['Date']).count()
emsByDate['Date'] = emsByDate.index
emsByDate = emsByDate.sort_values('timeStamp')

t = sns.lineplot(x = 'Date', y = 'e', data = trafficByDate)
t.set_title('Traffic 911 Calls by Date')
t.set_ylabel('Count')
for item in t.get_xticklabels():
    item.set_rotation(45)
plt.tight_layout()
plt.show()
exit()

#f = sns.lineplot(x = 'Date', y = 'e', data = fireByDate)
#plt.show()
#e = sns.lineplot(x = 'Date', y = 'e', data = emsByDate)
#plt.show()
#plt.tight_layout()

