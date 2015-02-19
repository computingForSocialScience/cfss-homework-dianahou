import sys
import requests
import csv
import pandas as pd
import numpy as np
import networkx as nx

def readEdgeList(filename):
    edgeList = pd.read_csv(filename)
    if len(edgeList.columns) > 2:
        print Warning('CSV contains more than 2 columns')
        two_columns = pd.read_csv(filename, usecols=[0,1])
        return pd.DataFrame(two_columns)
    else:
        return pd.DataFrame(edgeList)

#print readEdgeList('filename.csv')

def degree(edgeList, in_or_out):
    if in_or_out == 'out':
        return edgeList['artist1'].value_counts()
    elif in_or_out == 'in':
        return edgeList['artist2'].value_counts()

#print degree(readEdgeList('filename.csv'), 'in')

def combineEdgelists(edgeList1, edgeList2):
    combined_list = pd.concat([edgeList1, edgeList2])
    final_list = combined_list.drop_duplicates()
    return final_list

def pandasToNetworkX(edgeList):
    tple_list = edgeList.to_records(index=False)
    g = nx.DiGraph()
    for artist1,artist2 in tple_list:
        g.add_edge(artist1,artist2)
    return g

#pandasToNetworkX(readEdgeList('filename.csv'))

def randomCentralNode(inputDiGraph):
    ec_dict = nx.eigenvector_centrality(inputDiGraph)
    for key in ec_dict:
        nc_dict[key] = ec_dict[key]/float(sum(ec_dict.values()))  #each value from old dict is divided by sum of original values
    randomNode = np.random.choice(nc_dict.keys(), p=nc_dict.values())
    return randomNode




