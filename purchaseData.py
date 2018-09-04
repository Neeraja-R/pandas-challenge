import os
import pandas as pd
import numpy as np

purchase_data = ('/Users/anirudhrajagopalan/Desktop/DataVizClassRepo/RUTSOM201807DATA5/Tuesday-Thursday/04 - Python Pandas/HW4/HeroesOfPymoli/Resources/purchase_data.csv')

purchaseData = pd.read_csv(purchase_data)

purData = pd.DataFrame(purchaseData)

def playerCount():
    totalPlayers = purData.groupby(["SN"]).count().sum()

def purchaseAnalys():
    uniqueItems = purData.groupby(["Item Name"]).count().sum()
    avgPurprice = purData.groupby(["Price"]).avg()
    totalPur = purData.groupby((["Purchase ID"]).sum()) + 1
    totalRev = purData.groupby(["Price"]).sum()
print (purchaseAnalys)
    
