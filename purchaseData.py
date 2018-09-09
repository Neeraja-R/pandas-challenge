import os
import pandas as pd
import numpy as np

purchase_data = ('/Users/anirudhrajagopalan/Desktop/DataVizClassRepo/RUTSOM201807DATA5/Tuesday-Thursday/04 - Python Pandas/HW4/HeroesOfPymoli/Resources/purchase_data.csv')

purchaseData = pd.read_csv(purchase_data)

purData = pd.DataFrame(purchaseData)

# purData no errors

#total players
totalPlayers = (purData["SN"].count()).sum()
tp_df = pd.DataFrame({"Total Players": [totalPlayers]})
tp_df

totalPlayers

#purchase analysis
avgPur_price = purData["Price"].mean()

totalPurN = len(purData)

totalRev = purData["Price"].sum()

uniqueI = purData["Item ID"].value_counts()
uIt = [uniqueI]
unique_I = len(uIt[0])

purchA_df = pd.DataFrame({"Total-Unique Items": [unique_I], "Avg-Purchase Price": [avgPur_price], "Total-Number of Purchases": [totalPurN], "Total Revenue": [totalRev]})

purchA_df


# GenderDem()

genData = [purData["Gender"].value_counts()]
print (genData)

genP = [(purData["Gender"].value_counts() / len(purData.Gender))*100]
print(genP)


# purchasing anlysis (gender)

group_gender_df = purData.groupby("Gender")
group_gender_df

group_gender_df.count()

group_gender_df["Purchase ID"].count()

group_gender_df["Price"].mean()

byPerson = purData.groupby("SN")

byPerson.head()

byPerson["Price"].mean()



# AgeDem()

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








def TopSpenders()

#total purchase value
totalPurValue = pd.DataFrame(purData.groupby('SN')['Price'].sum())

sortedPurVal = totalPurValue.sort_values("Price", ascending=False)
sortByTPV = sortedPurVal.head()

print(sortByTPV)

#avg purchace price
avgPurPrice = pd.DataFrame(purData.groupby('SN')['Price'].mean())

sortedPurPrice = avgPurPrice.sort_values("Price", ascending=False)

sortByAPP = sortedPurPrice.head()

print(sortByAPP)

#purchase count

PurCount = pd.DataFrame(purData["SN"].value_counts())

purchCount = PurCount.sort_values("SN", ascending=False)

purCountSN = purchCount.head()

print(purCountSN)



def popItems()

#this gives item ID count of top 5 pop items

itPopu = purData.groupby("Item Name")
itPopuCt = itPopu.count()
itPopuCt_sort = itPopuCt.sort_values("Purchase ID", ascending=False)
listPopu = [itPopuCt_sort.head()]
print(listPopu)


#come back to finish and format this


def MostProf()

#this creates a df with item name and price, sorted

profIt = (purData.groupby("Item Name")["Price"]).sum()
profIt_pd = pd.DataFrame(profIt)
profIt_sorted = profIt_pd.sort_values("Price", ascending=False)
profIt_sorted




















'''get purchase id and age in an i loc, then sort. create a loop by age...assign to every 4 years and create a df of this. merge bins df and looped assignments df'''




    
    '''most popular items: make df of Item Name. Use count, then sort list. Use head to get top 5. '''
        
        '''most profitable items: df by item id, get sum, then sort by price.'''
    
    

