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
    
def PurGen()

genData = purData["Gender"].value_counts()
print (genData)

purData["Gender"].value_counts() / len(purData.Gender)

#compiled no errors

group_gender_df = purData.groupby("Gender")
print(group_gender_df)

group_gender_df.count()

'''purchase count = count of item ids per gender
avg purchase price = take a single column of the table and divide it by the len
total purchase price =
avg purchase total per perosn = take a new df per person and take priece and get avg by dividing by len'''

group_gender_df["Purchase ID"].count()

group_gender_df["Price"].mean()

group_gender_df["Price"].sum()


grouped_vehicles_df["Fuel Economy (mpg)"].mean()

    
    

