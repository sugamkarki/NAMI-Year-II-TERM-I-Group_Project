import pandas as p
d1=p.read_csv("http://pythonhow.com/data/sampledata_x_2.txt")
d2=p.read_csv("http://www.pythonhow.com/data/sampledata.txt")
d3=d1.concat(d2)