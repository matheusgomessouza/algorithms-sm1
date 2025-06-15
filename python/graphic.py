import csv
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

f = open("./assets/amazon.csv", "r", encoding="ISO-8859-1", newline="")

years = [1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
fires = [0] * len(years)

reader = csv.reader(f)
next(reader)  # Skip the header

for linha in f:
      data = linha.strip().split(",")
      yearConvertedToInt = int(data[0])

      if yearConvertedToInt in years:
          index = years.index(yearConvertedToInt)
          fires[index] += int(float(data[3]))

plt.scatter(years, fires)
plt.savefig("firesGraphic.png")
