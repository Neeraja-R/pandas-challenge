import os
import pandas as pd
import numpy as np

purchase_data = ('/Users/anirudhrajagopalan/Desktop/DataVizClassRepo/RUTSOM201807DATA5/Tuesday-Thursday/04 - Python Pandas/HW4/HeroesOfPymoli/Resources/purchase_data.csv')

purchaseData = pd.read_csv(purchase_data)

purData = pd.DataFrame(purchaseData)

'''purData.head() # no errors'''



totalPlayers = purData.groupby(["SN"]).count().sum()

uniqueItems = purData.groupby(["Item Name"]).count().sum()
avgPurprice = purData.groupby(["Price"]).mean()
totalPur = purData.len()
totalRev = purData.groupby(["Price"]).sum()

return (totalPlayers)




def add_numbers(a,b):
    output = a+b
    return(output)


output = add_numbers(5,4)
print(output)
    
