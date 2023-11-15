import bottle
import json
import os.path

import data 
import processing




def load_data():
  csv_file = 'saved_data.csv'
  if not os.path.isfile(csv_file):
    url = 'https://data.cdc.gov/resource/unsk-b7fc.json?$limit=50000&$where=location!=%27US%27'
    info = data.json_loader(url)
    heads = ['date','location','administered_janssen','administered_moderna','administered_pfizer','administered_unk_manuf','series_complete_pop_pct']
    data.save_data(heads, info, 'saved_data.csv')
load_data()
  
data_dict = data.load_data('saved_data.csv') #converting csv to dictionary
max_date = processing.max_value(data_dict, 'date') # Finding the maximum date
copy_match_date = processing.copy_matching(data_dict, 'date', max_date) #Finding dicts that matches maximum date

@bottle.route('/')
def send_html():
  return bottle.static_file("index.html", root=".")

@bottle.route('/vaccine.js')
def send_FrontEndJS():
  return bottle.static_file("vaccine.js", root=".")

@bottle.route('/ajax.js')
def send_AJAX():
  return bottle.static_file("ajax.js", root=".")

@bottle.route('/barChart')
def bar_chart(): # Organize the x and y values to make the bar graph
  alist = copy_match_date
  dict_ = {}
  x_val = []
  y_val = []
  for datadict in alist:
    num_val = data.make_values_numeric(['series_complete_pop_pct'], datadict) #convert selected values from str to number
    x_val.append(num_val['location'])
    y_val.append(num_val['series_complete_pop_pct'])
    dict_['x'] = x_val
    dict_['y'] = y_val
  file = json.dumps(dict_)
  return file


@bottle.route('/pieChart')
def pie_chart():
  alist = copy_match_date
  dict = {}
  count = 0
  Janssen = 0
  Moderna = 0
  Pfizer = 0
  Other = 0
  val = []
  percent = []
  for datadict in alist:
    num_val = data.make_values_numeric(['administered_janssen', 'administered_moderna', 'administered_pfizer', 'administered_unk_manuf'], datadict)
    count = count + num_val['administered_janssen'] + num_val['administered_moderna'] + num_val['administered_pfizer'] + num_val['administered_unk_manuf']
    Janssen = Janssen + num_val['administered_janssen']
    Moderna = Moderna + num_val['administered_moderna']
    Pfizer = Pfizer + num_val['administered_pfizer']
    Other = Other + num_val['administered_unk_manuf']
  val.append(Janssen)
  val.append(Moderna)
  val.append(Pfizer)
  val.append(Other)
  for num in val:
    per = (num/count*100)
    percent.append(per)
  dict['values'] = percent
  dict['labels'] = [ 'Janssen', 'Moderna', 'Pfizer', 'Other']
  dict['type'] = 'pie'
  file = json.dumps(dict)
  return file

@bottle.post('/lineChart')
def line_chart():
  contentJSON = bottle.request.body.read().decode()
  content = json.loads(contentJSON)
  list = data_dict
  dict = {}
  x_val = []
  y_val = []
  for dicts in list:
    num_val = data.make_values_numeric(['series_complete_pop_pct'], dicts)
    if content['location'] == num_val['location']:
      x_val.append(num_val['date'])
      y_val.append(num_val['series_complete_pop_pct'])
  dict['x'] = x_val
  dict['y'] = y_val
  file = json.dumps(dict)
  return file

bottle.run(host = "0.0.0.0", prt=8080,debug=True)