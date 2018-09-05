import os
import pandas as pd
import numpy as np

purchase_data = ('/Users/anirudhrajagopalan/Desktop/DataVizClassRepo/RUTSOM201807DATA5/Tuesday-Thursday/04 - Python Pandas/HW4/HeroesOfPymoli/Resources/purchase_data.csv')

purchaseData = pd.read_csv(purchase_data)

purData = pd.DataFrame(purchaseData)

'''purData.head() # no errors'''

u_I = []
for x in purData:
    u_I = purData.append("Item Name").value()
    unique_I = u_I.index.sum()
print(unique_I)

'''totalPlayers = purData["SN"].count()
    t_P = totalPlayers.sum()
    print (t_P)'''

'''avgPur_price = purData["Price"].mean()
    print (avgPur_price)
    
    totalPur = len(purData)
    print (totalPur)
    
    totalRev = purData["Price"].sum()
    print (totalRev)'''



