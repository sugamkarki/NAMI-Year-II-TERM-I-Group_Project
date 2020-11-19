import pandas as p
d1=p.read_csv("http://pythonhow.com/data/sampledata_x_2.txt")
d2=p.read_csv("http://www.pythonhow.com/data/sampledata.txt")
d3=p.concat([d1,d2])
print(d3)
# data
d3.too_csv("74.txt",Index=)
