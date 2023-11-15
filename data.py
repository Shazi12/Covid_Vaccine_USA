'use strict'
import json
import csv
import urllib.request

#art 2
############################## *dic_list_gen* ###############################
def dic_list_gen(sList, lList):
    aList = []
    for m in lList: #List
      dict = {}
      for o in range(len(m)):
        dict[sList[o]] = m[o]
      aList.append(dict)
    return aList


############################# *read_values* ################################
def read_values(filename):
    with open(filename, 'r') as f:
        read = csv.reader(f)
        next(read)
        aList = []
        for n in read:
          tempList = []
          for x in range(len(n)): 
            tempList.append(n[x])
          aList.append(tempList)
    return aList

################################ *make_lists* ############################## 
def make_lists(sList, dList):
    aList = [] 
    for m in dList:
      tempList =[]
      for n in sList:
        tempList.append(m[n])
      aList.append(tempList)
    return aList


############################## *write_values* ###############################

def write_values(filename, lList):
    with open(filename, 'a') as f:
      writer = csv.writer(f)
      for m in lList:
        writer.writerow(m)

# Part 3
############################### *json_loader* ##############################
def json_loader (string):
  response = urllib.request.urlopen(string)
  content = response.read().decode()
  return json.loads(content)

######################### *make_values_numeric* #############################

def make_values_numeric(slist, dict):
  for string in slist:
    dict [string] = float(dict[string])
  return dict

############################## *save_data* #################################

def save_data(sList, dList,filename):
  with open(filename,'w') as f:
    writer = csv.writer(f)
    writer.writerow(sList)
    aList = [] 
    for m in dList:
      tempList =[]
      for n in sList:
        tempList.append(m[n])
      aList.append(tempList)
    for list in aList:
      writer.writerow(list)

############################### *load_data* ################################

def load_data(filename):
  with open(filename, 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    content = []
    for rows in reader:
      content.append(rows) 
    aList = []
    for m in content: #List
      dict = {}
      for o in range(len(m)):
        dict[header[o]] = m[o]
      aList.append(dict)
    return aList