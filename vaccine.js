'use strict'
function showBar(response) {
  // Data is always sent in JSON, so we must first convert it 
  let data = JSON.parse(response);
  let layout = {
  title:'Vaccination Percent by Location'
  };
  // Now write the code that uses data to create the scatter plot
  
  //let graph = Plotly.newPlot("bar",response);
  let div = document.getElementById("bar");
  Plotly.newPlot(div,[{"x":data['x'],"y":data['y'], type:'bar'}],layout);
}
function getbar(){
  ajaxGetRequest('/barChart', showBar);
}


function showPie(response) {
  // Data is always sent in JSON, so we must first convert it 
  let data = JSON.parse(response);
  let layout = {
  title:'Vaccine Distribution by Manufacture'
  };
  // Now write the code that uses data to create the scatter plot
  let div = document.getElementById('pie');
  Plotly.newPlot(div,[{"values":data["values"],"labels":data["labels"], type:'pie'}],layout);
}
function getpie(){
  ajaxGetRequest('/pieChart', showPie);
}

function showline(response){
  // Data is always sent in JSON, so we must first convert it 
  let data = JSON.parse(response);
  // Now write the code that uses data to create the scatter plot
  let layout = {
  title:'% of State Fully Vaccined by Date'
  };
  let div = document.getElementById('line');
  let graph = Plotly.newPlot(div,[{"x":data['x'],"y":data['y'], type:'scatter'}],layout);
  
}

function getLocData(){
  // extract contents of texttbox
  let textbox = document.getElementById("locText");
  let locationText = textbox.value;
  console.log(locationText);
  // clear texttbox
  locText.value = "";
  //package textbox content JSON
  let data = {'location':locationText};
  let dataJSON = JSON.stringify(data);
  //sent POST request with that JSON to server
  ajaxPostRequest('/lineChart',dataJSON, showline)
}

