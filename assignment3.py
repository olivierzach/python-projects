# -*- coding: utf-8 -*-
"""
Introduction to Data Science in Python
Assignment 3

This assignment requires more individual learning then the last one did - 
you are encouraged to check out the pandas documentation to find functions or
 methods you might not have used yet,
 or ask questions on Stack Overflow and tag them as pandas and python related.
 And of course, the discussion forums are open for interaction with your peers 
 and the course staff.
 
 https://github.com/MaxPoon/coursera-Applied-Data-Science-with-Python/blob/master/Introduction-to-Data-Science-in-Python/week3/Assignment3.ipynb

"""



'''
Question 1:

Load the energy data from the file Energy Indicators.xls, which is a list of indicators of energy supply and renewable electricity production from the United Nations for the year 2013, and should be put into a DataFrame with the variable name of energy.

Keep in mind that this is an Excel file, and not a comma separated values file. Also, make sure to exclude the footer and header information from the datafile. The first two columns are unneccessary, so you should get rid of them, and you should change the column labels so that the columns are:

['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']

Convert Energy Supply to gigajoules (there are 1,000,000 gigajoules in a petajoule). For all countries which have missing data (e.g. data with "...") make sure this is reflected as np.NaN values.

Rename the following list of countries (for use in later questions):

"Republic of Korea": "South Korea",
"United States of America": "United States",
"United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
"China, Hong Kong Special Administrative Region": "Hong Kong"

There are also several countries with numbers and/or parenthesis in their name. Be sure to remove these,

e.g.

'Bolivia (Plurinational State of)' should be 'Bolivia',

'Switzerland17' should be 'Switzerland'.



Next, load the GDP data from the file world_bank.csv, which is a csv containing countries' GDP from 1960 to 2015 from World Bank. Call this DataFrame GDP.

Make sure to skip the header, and rename the following list of countries:

"Korea, Rep.": "South Korea", 
"Iran, Islamic Rep.": "Iran",
"Hong Kong SAR, China": "Hong Kong"



Finally, load the Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology from the file scimagojr-3.xlsx, which ranks countries based on their journal contributions in the aforementioned area. Call this DataFrame ScimEn.

Join the three datasets: GDP, Energy, and ScimEn into a new dataset (using the intersection of country names). Use only the last 10 years (2006-2015) of GDP data and only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15).

The index of this DataFrame should be the name of the country, and the columns should be ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015'].

This function should return a DataFrame with 20 columns and 15 entries.    
    
'''


def answer_one():
    
    import numpy as np
    import pandas as pd
    
    
    ## read and clean energy dataset
    energy = pd.read_excel(
            'Energy Indicators.xls',
            na_values = ['NA'],
            usecols = [2,3,4,5,6],
            skiprows = 17,
            skipfooter = 38,
            names = ['Country', 
                     'Energy Supply',
                     'Energy Supply per Capita',
                     '% Renewable']
            )
    # rename columns
    energy.rename(columns={
            'Environmental Indicators: Energy': 'Country',
            'Unnamed: 3':'Energy Supply',
            'Unnamed: 4':'Energy Supply per Capita',
            'Unnamed: 5':'% Renewable'},
    inplace=True)
    
    # remove ... and replace with np.nan
    energy.replace('...', np.nan, inplace = True)
    
    # convert column to gigs
    energy['Energy Supply'] *= 1000000
    
    # function to remove subscript and parens
    def remove_sub(data):
        new = ''.join([i for i in data if not i.isdigit()])
        i = new.find('(')
        if i>-1: new = new[:i]
        return new.strip()
    
    # apply to energy df
    energy['Country'] = energy['Country'].apply(remove_sub)
    
    # define name changes in a dictionary
    dict_name = {
            "Republic of Korea": "South Korea",
            "United States of America": "United States",
            "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
            "China, Hong Kong Special Administrative Region": "Hong Kong"
            }
    
    # replace names in actual dataset using dictionary
    energy.replace({'Country':dict_name}, inplace = True)
    
    
    
    
    ## read and clean GDP dataset
    GDP = pd.read_csv(
            "world_bank.csv",
            skiprows = 4
            )
    
    # rename column header
    GDP.rename(columns = {'Country Name':'Country'}, inplace = True)
    
    # define name changes 
    dict_gdp = {
            "Korea, Rep.": "South Korea", 
            "Iran, Islamic Rep.": "Iran",
            "Hong Kong SAR, China": "Hong Kong"
            }
    
    # apply name changes
    GDP.replace({'Country':dict_gdp}, inplace = True)
    
    # select only the needed columns
    GDP = GDP[[
            'Country','2006','2007','2008',
            '2009','2010','2011','2012','2013',
            '2014','2015'
            ]]
    

    ## read and clean the ScimEm dataset
    ScimEn = pd.read_excel('scimagojr-3.xlsx')
    
    
    
    ## join all dataframes together
    merge_df = pd.merge(pd.merge(energy, GDP, on = 'Country'),
                        ScimEn, on = 'Country')
    
    # set country as data frame index
    merge_df.set_index('Country', inplace = True)
    
    # select the needed columns
    df = merge_df[['Rank', 'Documents', 'Citable documents', 'Citations',
              'Self-citations', 'Citations per document', 'H index', 
              'Energy Supply', 'Energy Supply per Capita',
              '% Renewable', '2006', '2007', '2008', '2009',
              '2010', '2011', '2012', '2013', '2014', '2015']]
    
    df.sort_values(by = 'Rank', inplace = True)
    
    ans = df[:15]
    
    
    
    
    return ans



answer_one()



'''
Question 2 (6.6%)
The previous question joined three datasets then reduced this to just the top 15 entries.
 When you joined the datasets, 
 but before you reduced this to the top 15 items, 
 how many entries did you lose?

This function should return a single number.

'''

def answer_two():
    
   
    import numpy as np
    import pandas as pd
    
     ## read and clean energy dataset
    energy = pd.read_excel(
            'Energy Indicators.xls',
            na_values = ['NA'],
            usecols = [2,3,4,5,6],
            skiprows = 17,
            skipfooter = 38,
            names = ['Country', 
                     'Energy Supply',
                     'Energy Supply per Capita',
                     '% Renewable']
            )
    # rename columns
    energy.rename(columns={
            'Environmental Indicators: Energy': 'Country',
            'Unnamed: 3':'Energy Supply',
            'Unnamed: 4':'Energy Supply per Capita',
            'Unnamed: 5':'% Renewable'},
    inplace=True)
    
    # remove ... and replace with np.nan
    energy.replace('...', np.nan, inplace = True)
    
    # convert column to gigs
    energy['Energy Supply'] *= 1000000
    
    # function to remove subscript and parens
    def remove_sub(data):
        new = ''.join([i for i in data if not i.isdigit()])
        i = new.find('(')
        if i>-1: new = new[:i]
        return new.strip()
    
    # apply to energy df
    energy['Country'] = energy['Country'].apply(remove_sub)
    
    # define name changes in a dictionary
    dict_name = {
            "Republic of Korea": "South Korea",
            "United States of America": "United States",
            "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
            "China, Hong Kong Special Administrative Region": "Hong Kong"
            }
    
    # replace names in actual dataset using dictionary
    energy.replace({'Country':dict_name}, inplace = True)
    
    
    
    
    ## read and clean GDP dataset
    GDP = pd.read_csv(
            "world_bank.csv",
            skiprows = 4
            )
    
    # rename column header
    GDP.rename(columns = {'Country Name':'Country'}, inplace = True)
    
    # define name changes 
    dict_gdp = {
            "Korea, Rep.": "South Korea", 
            "Iran, Islamic Rep.": "Iran",
            "Hong Kong SAR, China": "Hong Kong"
            }
    
    # apply name changes
    GDP.replace({'Country':dict_gdp}, inplace = True)
    
    # select only the needed columns
    GDP = GDP[[
            'Country','2006','2007','2008',
            '2009','2010','2011','2012','2013',
            '2014','2015'
            ]]
    

    ## read and clean the ScimEm dataset
    ScimEn = pd.read_excel('scimagojr-3.xlsx')
    
    
    
    ## join all dataframes together
    merge_df = pd.merge(pd.merge(energy, GDP, on = 'Country'),
                        ScimEn, on = 'Country')
    
    # full outer join to keep all possible countries
    outer_df = pd.merge(pd.merge(energy, GDP, on = 'Country', how = 'outer'),
                        ScimEn, on = 'Country', how = 'outer')
    
    # original join from question1 - the countries we ended up with 
    merge_df2 = pd.merge(pd.merge(energy, GDP, on = 'Country'),
                        ScimEn, on = 'Country')
    
    
    # number of rows in the outer join dataset
    l_out = len(outer_df)
    
    # number of rows in the dataset after joining
    l_orig = len(merge_df2)
    
    # subtracting outer from the original gives us the number of drops
    ans = l_out - l_orig
    
    return ans

answer_two()


'''
Question 3 (6.6%)
What is the average GDP over the last 10 years for each country? 
(exclude missing values from this calculation.)

This function should return a Series named avgGDP 
with 15 countries and their average GDP sorted in descending order.


'''

def answer_three():
    Top15 = answer_one()
    Top15['Average GDP'] = Top15.iloc[:,10:20]\
        .mean(axis = 1)
        
    avgGDP = Top15['Average GDP'].sort_values(ascending = False)
    
    
    return avgGDP

answer_three()



'''
Question 4 (6.6%)
By how much had the GDP changed over the 10 year span for the country 
with the 6th largest average GDP?

This function should return a single number.
'''

def answer_four():
    Top15 = answer_one()
    Top15['Average GDP'] = Top15.iloc[:,10:20]\
        .mean(axis = 1)
        
    avgGDP = Top15.iloc[:,10:21].sort_values(by = 'Average GDP',
                       ascending = False)
    
    country = avgGDP.index[5]
    diff_df = Top15.loc[country]
    
    ans = abs(diff_df['2006'] - diff_df['2015'])
    
    
    return ans

answer_four()


'''
Question 5 (6.6%)
What is the mean Energy Supply per Capita?

This function should return a single number.
'''

def answer_five():
    Top15 = answer_one()
    ans = Top15['Energy Supply per Capita']
    ans = ans.mean()
    
    return ans

answer_five()


'''
Question 6 (6.6%)
What country has the maximum % Renewable and what is the percentage?

This function should return a tuple with the name of the
 country and the percentage.
 
'''
def answer_six():
    Top15 = answer_one()
    ans = Top15.sort_values(by = '% Renewable', ascending = False).iloc[0]
    
    return (ans.name, ans['% Renewable'])

answer_six()


'''
Question 7 (6.6%)
Create a new column that is the ratio of Self-Citations to Total Citations. 
What is the maximum value for this new column, and what country has the highest ratio?

This function should return a tuple with the name of the country and the ratio
 
'''

def answer_seven():
    Top15 = answer_one()
    Top15['Ratio'] = Top15['Self-citations'] / Top15['Citations']
    max_citation = Top15['Ratio'].max()
    top_country = Top15[Top15['Ratio'] == max_citation].index[0]
    
    
    return (top_country, max_citation)
answer_seven()

'''
Question 8 (6.6%)

Create a column that estimates the population using Energy Supply and Energy Supply per capita. 
What is the third most populous country according to this estimate?

*This function should return a single string value.*
 
'''

def answer_eight():
    Top15 = answer_one()
    col_index = ['Energy Supply', 'Energy Supply per Capita']
    df = Top15[col_index]
    df['Estimate'] = df['Energy Supply'] / df['Energy Supply per Capita']
    
    ans = df.sort_values(by = 'Estimate', ascending = False).iloc[2].name
    
    return ans

answer_eight()


'''
Question 9 (6.6%)

Create a column that estimates the number of citable documents per person. 
What is the correlation between the number of citable documents per capita and 
the energy supply per capita? Use the .corr() method, (Pearson's correlation).

This function should return a single number.

'''

def answer_nine():
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    corr = Top15['Citable docs per Capita'].corr(Top15['Energy Supply per Capita'])
    
    return corr

answer_nine()

answer_nine()

def plot9():
    import matplotlib as plt
    
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    Top15.plot(x='Citable docs per Capita', y='Energy Supply per Capita', 
               kind='scatter', xlim=[0, 0.0006])

plot9()


'''
Question 10 (6.6%)
Create a new column with a 1 if the country's % Renewable value is at or above 
the median for all countries in the top 15, 
and a 0 if the country's % Renewable value is below the median.

This function should return a series named HighRenew whose index is the 
country name sorted in ascending order of rank.

'''

def answer_ten():
    Top15 = answer_one()
    median_top15 = Top15['% Renewable'].median() 
    
    Top15['HighRenew'] = np.where(Top15['% Renewable'] >= median_top15,
         1,0)
    
    ans = Top15['HighRenew']
    
    return ans


'''
Question 11 (6.6%)
Use the following dictionary to group the Countries by Continent,
 then create a dateframe that displays the sample size 
 (the number of countries in each continent bin),
 and the sum, mean, and std deviation for the estimated population of each country.
 
 ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
 
This function should return a DataFrame with index named Continent 
['Asia', 'Australia', 'Europe', 'North America', 'South America'] 
and columns ['size', 'sum', 'mean', 'std']

'''

def answer_eleven():
    Top15 = answer_one()
    
    ContinentDict = {
             'China':'Asia', 
             'United States':'North America', 
             'Japan':'Asia', 
             'United Kingdom':'Europe', 
             'Russian Federation':'Europe', 
             'Canada':'North America', 
             'Germany':'Europe', 
             'India':'Asia',
             'France':'Europe', 
             'South Korea':'Asia', 
             'Italy':'Europe', 
             'Spain':'Europe', 
             'Iran':'Asia',
             'Australia':'Australia', 
             'Brazil':'South America'}
     
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply Per Capita']
    Top15 = Top15.reset_index()
    Top15['Continent'] = Top15['Country'].map(ContinentDict)
     
    ans = Top15.set_index('Continent').groupby(level = 0)['PopEst']\
        .agg(['size', 'sum', 'mean', 'std'])        
    
    return ans



'''
Question 12 (6.6%)
Cut % Renewable into 5 bins. 
Group Top15 by the Continent, as well as these new % Renewable bins. 
How many countries are in each of these groups?

This function should return a Series with a MultiIndex of Continent, 
then the bins for % Renewable. 

Do not include groups with no countries.

'''

def answer_twelve():

    ContinentDict = {
             'China':'Asia', 
             'United States':'North America', 
             'Japan':'Asia', 
             'United Kingdom':'Europe', 
             'Russian Federation':'Europe', 
             'Canada':'North America', 
             'Germany':'Europe', 
             'India':'Asia',
             'France':'Europe', 
             'South Korea':'Asia', 
             'Italy':'Europe', 
             'Spain':'Europe', 
             'Iran':'Asia',
             'Australia':'Australia', 
             'Brazil':'South America'}
    
    Top15 = answer_one().reset_index()
    Top15['Continent'] = Top15['Country'].map(ContinentDict)
    Top15['Group Bins'] = pd.cut(Top15['% Renewable'], 5)
    
    ans = pd.Series(Top15.groupby(['Continent', 'Group Bins']).size())
    
    return ans


'''
Question 13 (6.6%)
Convert the Population Estimate series to a string with thousands separator (using commas). 
Do not round the results.

e.g. 317615384.61538464 -> 317,615,384.61538464

This function should return a Series PopEst whose index is the country name
 and whose values are the population estimate string.

'''

def answer_thirteen():
    Top15 = answer_one()
    Top15['PopEst'] = (Top15['Energy Supply'] / Top15['Energy Supply per Capita']).astype(float)
    Top15['PopEst'] = Top15['PopEst'].map('{0:,}'.format)
    
    ans = Top15['PopEst']
    
    
    return ans

answer_thirteen()



'''
Optional
Use the built in function plot_optional() to see an example visualization.
https://github.com/MaxPoon/coursera-Applied-Data-Science-with-Python/blob/master/Introduction-to-Data-Science-in-Python/week3/Assignment3.ipynb
'''


def plot_optional():
    Top15 = answer_one()
    ax = Top15.plot(x='Rank', y='% Renewable',
                    kind='scatter', 
                    c=['#e41a1c','#377eb8','#e41a1c',
                       '#4daf4a','#4daf4a','#377eb8','#4daf4a','#e41a1c',
                       '#4daf4a','#e41a1c','#4daf4a','#4daf4a','#e41a1c',
                       '#dede00','#ff7f00'], 
                    xticks=range(1,16),
                    s=6*Top15['2014']/10**10,
                    alpha=.75,
                    figsize=[16,6]);

    for i, txt in enumerate(Top15.index):
        ax.annotate(txt, [Top15['Rank'][i], Top15['% Renewable'][i]],
                    ha='center')

    print("This is an example of a visualization that can be created to help understand the data. \
This is a bubble chart showing % Renewable vs. Rank. The size of the bubble corresponds to the countries' \
2014 GDP, and the color corresponds to the continent.")











