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


#Purchasing Analysis(Gender)

group_gender = purData.groupby("Gender")

genderlist = group_gender.count()     #give by gender: pur count(ID), needs title
glist = pd.DataFrame(genderlist.iloc[: , 0:1])
print(glist)

grgnd = group_gender["Price"].mean()    #gives avg pur price by gender
print(grgnd)

totpv = group_gender["Price"].sum() #gives total pur value by gender
print(totpv)
#totpv.columns = ["Total Purchase Price"]

profIt = (purData.groupby("Item Name")["Price"]).sum()
profIt_pd = pd.DataFrame(profIt)
profIt_sorted = profIt_pd.sort_values("Price", ascending=False)
profIt_sorted.head()

profip_df = pd.DataFrame{"Final Critic": 4.88, "Oathbreaker, Last Hope of the Breaking Storm": 4.88, "Final Critic": 4.88"}
profip_df   # item name and price




# AgeDem()

my_list_age = purData["Age"].tolist() #age cat. turned into list

maxAge = max(my_list_age)
minAge = min(my_list_age)


bins = [0, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46]
group_labels = ["<10 y/o", "10-14 y/o", "14-18 y/o", "18-22 y/o", "22-26 y/o", "26-30 y/o", "30-34 y/o", "34-38 y/o", "38-42 y/o", "42-46 y/o"]

binning = pd.cut(purData["Age"], bins, labels=group_labels).head()

purData["Age Group"] = pd.cut(purData["Age"], bins, labels=group_labels)

purData.head()

#bins created, added as "age group" new column
df = pd.DataFrame({"A": [1,2,3],
                  "B": [2,4,8]})
new_column = pd.Series([1,2,3])
df = pd.concat([df, new_column.rename("C")], axis=1)
df

ageGroup = purData.groupby("Age Group")

df_pc = ageGroup["Purchase ID"].count() #purchase count
df_pc


df_app = ageGroup["Price"].mean() #avg purchase price
df_app

df_tp = ageGroup["Price"].sum() #total purchase value
df_tp


pd.merge(left_frame, right_frame, on='key', how='inner')
#this is avg mean price for all divided by average mean price per person
avgPerson = purData.groupby("SN")
totalPer_Pur = (avgPerson["Price"].mean()/purData["Price"].mean())
print(totalPer_Pur)


#need to merge all the values here





# TopSpenders()

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



# popItems()

#this gives item ID count of top 5 pop items

itPopu = purData.groupby("Item Name")
itPopuCt = itPopu.count()
itPopuCt_sort = itPopuCt.sort_values("Purchase ID", ascending=False)
listPopu = [itPopuCt_sort.head()]
print(listPopu)

itmid = [92, 178, 141, 82, 108]
itpr = [$4.88, $4.43, $3.19, $4.9, $3.53]
Totpc = [$448.9, $752.9, $449.8, $401.8, $381.2]


# MostProf()

#this creates a df with item name and price, sorted

profIt = (purData.groupby("Item Name")["Price"]).sum()
profIt_pd = pd.DataFrame(profIt)
profIt_sorted = profIt_pd.sort_values("Price", ascending=False)
profIt_sorted.head()

itmidprof = [92, 178, 82, 145, 103]
itprprof = [4.88, 4.43, 4.90, 4.58, 4.35]
purcoutprof = [13, 12, 9, 9, 8]

