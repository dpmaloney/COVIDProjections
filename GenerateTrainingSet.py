import numpy as np
import pandas as pd

def loadData():
    countryData = pd.read_csv("countries.csv")
    caseData = pd.read_csv("cases.csv")

    print(countryData.describe)
    print(caseData.describe)

