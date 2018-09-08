import os
import pandas as pd
import numpy as np

purchase_data = ('/Users/anirudhrajagopalan/Desktop/DataVizClassRepo/RUTSOM201807DATA5/Tuesday-Thursday/04 - Python Pandas/HW4/HeroesOfPymoli/Resources/purchase_data.csv')

purchaseData = pd.read_csv(purchase_data)

purData = pd.DataFrame(purchaseData)

'''purData.head() # no errors'''


def prchAnlys()
totalPlayers = purData["SN"].count()
    t_P = totalPlayers.sum()
    print (t_P)'''

avgPur_price = purData["Price"].mean()
    print (avgPur_price)

totalPur = len(purData)
    print (totalPur)
        
totalRev = purData["Price"].sum()
    print (totalRev)
        
    print(purData["Item Name"].value_counts())
    
def GenderDem()

genData = purData["Gender"].value_counts()
print (genData)

purData["Gender"].value_counts() / len(purData.Gender)

#compiled no errors

group_gender_df = purData.groupby("Gender")
print(group_gender_df)

group_gender_df.count()

group_gender_df["Purchase ID"].count()

group_gender_df["Price"].mean()

byPerson = purData.groupby("SN")

byPerson.head()

byPerson["Price"].mean()

def AgeDem()

my_list_age = purData["Age"].tolist() #age cat. turned into list

maxAge = max(my_list_age)
minAge = min(my_list_age)

# min/max to help make bins [(0, 4] < (4, 8] < (8, 12] < (12, 16] ... (28, 32] < (32, 36] < (36, 40] < (40, 44]]

bins = [0, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46]
group_labels = ["<10 y/o", "10-14 y/o", "14-18 y/o", "18-22 y/o", "22-26 y/o", "26-30 y/o", "30-34 y/o", "34-38 y/o", "38-42 y/o", "42-46 y/o"]

binning = pd.cut(purData["Age"], bins, labels=group_labels).head()

purData["Age Group"] = pd.cut(purData["Age"], bins, labels=group_labels)

purData.head()

#bins created, added as "age group" new column

ageGroup = purData.groupby("Age Group")

print(ageGroup["Purchase ID"].count()) #purchase count

print(ageGroup["Price"].mean()) #avg purchase price

print(ageGroup["Price"].sum()) #total purchase value

#this is avg mean price for all divided by average mean price per person
avgPerson = purData.groupby("SN")
totalPer_Pur = (avgPerson["Price"].mean()/purData["Price"].mean())
print(totalPer_Pur)

#need to merge all the values here 








'''get purchase id and age in an i loc, then sort. create a loop by age...assign to every 4 years and create a df of this. merge bins df and looped assignments df'''



'''top spenders: df by SN, count to get every name. This should give you item id sorted by name...that is purchase count. Then take price from this df and get mean for avg. For total use sum'''
    
    '''most popular items: make df of Item Name. Use count, then sort list. Use head to get top 5. '''
        
        '''most profitable items: df by item id, get sum, then sort by price.'''
    
    

