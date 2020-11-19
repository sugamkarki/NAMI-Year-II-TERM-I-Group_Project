import pandas as pd

data = pd.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data_2 = data * 2
print(data_2.to_csv("sampledata_x_2.txt", index=None))