# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 13:00:32 2019

@authors: aqueel,harsh,towfik
"""

import tabula
import pandas as pd

#Defining path and file names
path = 'C:/Users/user/Desktop/BI/Project/B.I_Group4_Project/'
url_firearm_2014= 'https://www.atf.gov/resource-center/docs/firearmscommerceannualstatisticalreport2014pdf/download'
url_firearm_2015= 'https://www.atf.gov/file/89561/download/firearms_commerce_annual_statistical_report_2015-revised_3_15_16_0.pdf'
url_firearm_2016= 'https://www.atf.gov/file/108316/download/firearms_commerce_2016_508_8-16-16a_0.pdf'
url_firearm_2017= 'https://www.atf.gov/file/118216/download/firearms_commerce_in_the_united_states_annual_statistical_update_2017-5_0.pdf'
frearm_2014 = 'firearm2014.xlsx'
frearm_2014_test = 'firearm_2014.xlsx'
frearm_2015 = 'firearm2015.xlsx'
frearm_2015_test = 'firearm_2015.xlsx'
frearm_2016 = 'firearm2016.xlsx'
frearm_2016_test = 'firearm_2016.xlsx'
frearm_2017 = 'firearm2017.xlsx'
frearm_2017_test = 'firearm_2017.xlsx'
firearm_final ='firearm.xlsx'
unemployment_2014 = 'Unemployment 14.csv'
unemployment_2015 = 'Unemployment 15.csv'
unemployment_2016 = 'Unemployment 16.csv'
unemployment_2017 = 'Unemployment 17.csv'
unemployment_final = 'Unemployment.xlsx'
estimated_crime = 'estimated_crimes.xlsx'
merge_first = 'firstmerge.xlsx'
mortality_firearm = 'Firearm Mortality by State.csv'
Dataset_final = 'FinalDataset.xlsx'

##Firearms Data 2014
#fetching table from page 16 from link of ATF, which gives us data for 2014
firearm_14 = tabula.read_pdf(url_firearm_2014, pages=16)

#writing it to excel to check
firearm2014=firearm_14.to_excel(path + frearm_2014_test, engine='xlsxwriter')
#reading the excel
read2014=pd.read_excel(path + frearm_2014_test)


read2014.keys()
#converting it to dataframe and putting on a variable
df1_2014= pd.DataFrame(read2014)
df1_2014.head()
#dropping unwanted rows and columns
df2_2014=df1_2014.drop(0)
df2_2014=df2_2014.drop(53)
df2_2014=df2_2014.drop(52)

df2_2014.columns
#adding a column named year with a value of 2014
df2_2014['year'] = 2014
#df2_2014
#df2_2014.to_csv('C:/Users/user/Desktop/test.csv')
#Renaming the column names for the benefit for our merging and calculation
df2_2014.columns= ['State','Any Other Weapon','Destructive Device','Machine Gun', 'Silencer', 'Short Barreled Rifle','Short Barreled Shotgun', 'Total', 'Year']

#writing the outcome to excel
firearm_updated2014=df2_2014.to_excel(path + frearm_2014,engine='xlsxwriter', index=False)

##Firearms Data 2015
#fetching table from page 16 from link of ATF, which gives us data for 2015
firearm_15 = tabula.read_pdf(url_firearm_2015, pages=16)
firearm_15
#writing it to excel to check
firearm2015=firearm_15.to_excel(path + frearm_2015_test, engine='xlsxwriter')
#reading the excel
read2015=pd.read_excel(path + frearm_2015_test)
read2015.keys()
#converting it to dataframe and putting on a variable
df1_2015= pd.DataFrame(read2015)
#dropping unwanted rows and columns
df2_2015=df1_2015.drop(0)
df2_2015=df2_2015.drop(53)
df2_2015=df2_2015.drop(52)

df2_2015.columns
#adding a column named year with a value of 2015
df2_2015['year'] = 2015
#Renaming the column names for the benefit for our merging and calculation
df2_2015.columns= ['State','Any Other Weapon','Destructive Device','Machine Gun', 'Silencer', 'Short Barreled Rifle','Short Barreled Shotgun', 'Total', 'Year']

#writing the outcome to excel
firearm_updated2015=df2_2015.to_excel(path + frearm_2015, engine='xlsxwriter', index=False)

##Firearms Data 2016
#fetching table from page 16 from link of ATF, which gives us data for 2016
firearm_16 = tabula.read_pdf(url_firearm_2016, pages=16)
firearm_16
#writing it to excel to check
firearm2016=firearm_16.to_excel(path + frearm_2016_test, engine='xlsxwriter')
#reading the excel
read2016=pd.read_excel(path + frearm_2016_test)

read2016.keys()
#converting it to dataframe and putting on a variable
df1_2016= pd.DataFrame(read2016)
#dropping unwanted rows and columns
df2_2016=df1_2016.drop(0)
df2_2016=df2_2016.drop(53)
df2_2016=df2_2016.drop(52)

df2_2016.columns
#adding a column named year with a value of 2016
df2_2016['year'] = 2016
#Renaming the column names for the benefit for our merging and calculation
df2_2016.columns= ['State','Any Other Weapon','Destructive Device','Machine Gun', 'Silencer', 'Short Barreled Rifle','Short Barreled Shotgun', 'Total', 'Year']

#writing the outcome to excel
firearm_updated2016=df2_2016.to_excel(path + frearm_2016, engine='xlsxwriter', index=False)

##Firearms Data 2017
#fetching table from page 16 from link of ATF, which gives us data for 2017
firearm_17 = tabula.read_pdf(url_firearm_2017, pages=16)
firearm_17
#writing it to excel to check
firearm2017=firearm_17.to_excel(path + frearm_2017_test, engine='xlsxwriter')
#reading the excel
read2017=pd.read_excel(path + frearm_2017_test)
read2017.keys()
#converting it to dataframe and putting on a variable
df1_2017= pd.DataFrame(read2017)
#dropping unwanted rows and columns
df2_2017=df1_2017.drop(0)
df2_2017=df2_2017.drop(53)
df2_2017=df2_2017.drop(52)

df2_2017.columns
#adding a column named year with a value of 2017
df2_2017['year'] = 2017
#Renaming the column names for the benefit for our merging and calculation
df2_2017.columns= ['State','Any Other Weapon','Destructive Device','Machine Gun', 'Silencer', 'Short Barreled Rifle','Short Barreled Shotgun', 'Total', 'Year']

#writing the outcome to excel
firearm_updated2017=df2_2017.to_excel(path + frearm_2017, engine='xlsxwriter', index=False)

##Merging all firearm Data
#Reading excel files

df1 = pd.read_excel(path + frearm_2014)
df2 = pd.read_excel(path + frearm_2015)
df3 = pd.read_excel(path + frearm_2016)
df4 = pd.read_excel(path + frearm_2017)
df1
df1_append=df1.append(df2, ignore_index = True)
df1_append
df2_append=df1_append.append(df3, ignore_index = True)
df_append=df2_append.append(df4, ignore_index = True)
df_append
df_append.to_excel(path + firearm_final, index=False)



##Unemployment Data
##Reading excel files

u14=pd.read_csv(path + unemployment_2014)
u15=pd.read_csv(path + unemployment_2015)
u16=pd.read_csv(path + unemployment_2016)
u17=pd.read_csv(path + unemployment_2017)

#Drop empty rowa
u14=u14.dropna()
u15=u15.dropna()
u16=u16.dropna()
u17=u17.dropna()

#Rename columns for Rate and create Year column
u14.rename(columns={'2014':'Rate'},inplace=True)
u14['Year']=2014
u15.rename(columns={'2015':'Rate'},inplace=True)
u15['Year']=2015
u16.rename(columns={'2016':'Rate'},inplace=True)
u16['Year']=2016
u17.rename(columns={'2017':'Rate'},inplace=True)
u17['Year']=2017

#Check dataframes
u14.head()
u15.head()
u16.head()
u17.head()

#Append all the year dataframes
un=u14.append(u15)
un=un.append(u16)
un=un.append(u17)
#un=un['Year'].value_counts

un.head()

un.groupby('Year').count()

#create excel output file
un.to_excel(path + unemployment_final,engine='xlsxwriter')


##Crime Data
crime = pd.read_excel (path+estimated_crime)
print (crime)
##Rename the required columns
crime.rename(columns={"state_name": "state"},inplace = True)
crime.rename(columns={"rape_revised": "rape"},inplace = True)

##Removing not required column
crime.drop('caveats', inplace=True, axis=1)

##REmoving the rows with null values.
crime.iloc[[19,20,21,22]]
crime.drop(crime.index[[19,20,21,22]],inplace=True)
crime.drop(['rape_legacy'],axis=1, inplace= True)
crime.reset_index(drop=True, inplace=True)

crime.columns = map(str.lower, crime.columns)
crime.columns

##Code to merge other data frames
unemployment = pd.read_excel (path + unemployment_final)
firearm = pd.read_excel (path + firearm_final) 
print (unemployment)
print (firearm)

unemployment.columns = map(str.lower, unemployment.columns)
firearm.columns = map(str.lower, firearm.columns)


Merge1= unemployment.merge(firearm, how='inner', on=['state', 'year'])
Merge1
Merge2= crime.merge(Merge1, how='inner', on=['state','year'])
Merge2

Merge2.to_excel(path + merge_first,engine='xlsxwriter')

##Mortality Data
df=pd.read_excel(path + merge_first,thousands=',')
df.head()
df.columns

mort17=pd.read_csv(path + mortality_firearm,thousands=',')
mort17.columns
#Drop URL column
mort17.drop(columns=['URL'],inplace=True)
#Rename columns for uniformity
mort17.rename(columns={'YEAR':'year','STATE':'state_abbr','RATE':'death_rate','DEATHS':'deaths'},inplace=True)
mort17.dtypes
mort17.tail()
#Check null values
mort17.isna().sum()
#Drop blank rows
mort17.dropna(inplace=True)
#Change data types
mort=mort17.astype({'year':'int64','deaths':'int32'})

#Merge files
DS=df.merge(mort,how='inner',on=['state_abbr','year'])

DS.rename(columns={'rate':'unemployment_rate','rank':'unemployment_year_rank','total':'total_firearms'},inplace=True)
DS.dtypes

#Change data types
DS=DS.astype({'any other weapon':'int64','destructive device':'int64','machine gun':'int64',
            'silencer':'int64','short barreled rifle':'int64','short barreled shotgun':'int64',
            'total_firearms':'int64'})

DS.tail()
DS.rename(columns={'deaths':'death_by_firearms'},inplace=True)
DS.to_excel(path + Dataset_final,engine = 'xlsxwriter')
#Describe, correlation and coveriance
print(DS.describe())
print(DS.corr())
print(DS.cov())
# creating correlation output in excel
corr=DS.corr()
corr.to_csv('C:/Users/user/Desktop/correlation.csv')




