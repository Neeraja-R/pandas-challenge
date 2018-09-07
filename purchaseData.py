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


    
    

