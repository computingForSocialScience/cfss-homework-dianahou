import csv
import sys

def readCSV(filename):
    '''Reads the CSV file `filename` and returns a list
    with as many items as the CSV has rows. Each list item 
    is a tuple containing the columns in that row as stings.
    Note that if the CSV has a header, it will be the first
    item in the list.'''
    with open(filename,'r') as f:
        rdr = csv.reader(f)
        lines = list(rdr)
    return(lines)



### enter your code below
permitsData = readCSV('permits_hydepark.csv')

def get_avg_latlng(data):
	latitude = []
	for tple in data:
		latitude.append(float(tple[128]))
	longitude = []
	for tple in data:
		longitude.append(float(tple[129]))
	'''Taking averages'''
	x = sum(latitude)/(float(len(latitude)))
	y = sum(longitude)/(float(len(longitude)))
	print x, y
	return x, y
	
#get_avg_latlng(permitsData)

import numpy as np
from pylab import *
from matplotlib.pyplot import plot, hist

def zip_code_barchart(data):
    zipcodeList = []
    for tple in data:
        if tple[28] != '':
            zipcode = tple[28][0:5]
            zipcodeList.append(zipcode)
    zipcodeDict = {}
    for code in zipcodeList:
        if code in zipcodeDict.keys():
            zipcodeDict[code] += 1
        else:
            zipcodeDict[code] = 1
    print zipcodeDict

    x = zipcodeDict.keys()
    y = zipcodeDict.values()
    N = 5
    ind = np.arange(N)
    width = 0.50
    fig, ax = plt.subplots()
    rects = ax.bar([0,1,2,3,4], y, width, color='#6699FF')
    ax.set_xticks(ind+width)
    ax.set_xticklabels(x)
    ax.set_ylabel('Zip Code Count')
    ax.set_title('Zip Code Bar Chart')

    plt.show()

#zip_code_barchart(permitsData)

if __name__ == "__main__":
    permitsData = readCSV('permits_hydepark.csv')
    if len(sys.argv) == 1:
        get_avg_latlng(permitsData)
        zip_code_barchart(permitsData)
    elif sys.argv[1] == 'latlong':
        get_avg_latlng(permitsData)
    elif sys.argv[1] == 'hist':
        zip_code_barchart(permitsData)



