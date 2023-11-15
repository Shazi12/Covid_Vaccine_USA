#max_value

def max_value(data,key):
  values = []
  accumulator = ""
  for index in data:
    values.append(index[key])
    accumulator = values [0]
  for x in range(len(values)):
    if values[x] > accumulator:
      accumulator = values[x]
  result = str(accumulator)
  return result

#init_dictionary

def init_dictionary(data, key):
  accumulator = {}
  v = 0
  for index in data:
    if key in index:
      accumulator [index[key]] = v
  return accumulator


#sum_matches

def sum_matches (lod,k,v,tgt):
  accumulator = 0
  values = []
  for index in lod:
    if index[k] == v:
      values.append(index[tgt])
  for num in values:
    accumulator += num
  return accumulator


#copy_matching

def  copy_matching(lod,k,v):
  accumulator = []
  for index in lod:
    if index[k] == v:
      accumulator.append(index)
  return accumulator

