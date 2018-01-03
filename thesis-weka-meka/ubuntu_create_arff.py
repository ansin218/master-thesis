from pandas2arff import *
import pandas as pd

df = pd.read_csv("b_ubuntu_results.csv")
pandas2arff(df,"ubuntu_finegrained.arff", cleanstringdata=True, cleannan=True)
