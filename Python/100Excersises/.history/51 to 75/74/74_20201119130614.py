import pandas as p
d1=p.read_csv("http://pythonhow.com/data/sampledata_x_2.txt")
d2=p.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data12 = p.concat([data1, data2])
data12.to_csv("sampledata12.txt", index=None)