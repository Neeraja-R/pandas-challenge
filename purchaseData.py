import os 
import pandas as pd
import numpy as np

purchase_data = "Resources/purchase_data.csv"

purchase_data = pd.read_csv(purchase_data.csv)

purData = pd.Dataframe(purchase_data)

def purchaseStats():
    totalPlayers = purData.groupby(["SN"]).count().sum()
    