import pandas as p
d1=p.read_csv("http://pythonhow.com/data/sampledata.txt")
d2=p.read_csv("sampledata_x_2.txt")
data12 = p.concat([d1, d2])
data12.to_csv("sampledata12.txt", index=None)