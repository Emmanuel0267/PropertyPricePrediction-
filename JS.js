function getBathValue() 
{
  var uiBathrooms = document.getElementsByName("uiBathrooms");
  for(var i in uiBathrooms) 
  {
    if(uiBathrooms[i].checked) 
    {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getBHKValue() 
{
  var uiBHK = document.getElementsByName("uiBHK");
  for(var i in uiBHK) 
  {
    if(uiBHK[i].checked)
     {
        return parseInt(i)+1;
     }
  }
  return -1; // Invalid Value
}

function onClickedEstimatePrice()
 {
  console.log("Estimate price button clicked");
  var total_sqft = document.getElementById("uiSqft");
  var bhk = getBHKValue();
  var bathrooms = getBathValue();
  var area = document.getElementById("uiarea");
  var estPrice = document.getElementById("uiEstimatedPrice");

  var url = "http://127.0.0.1:5000/predict_home_price"; //Use this if you are NOT using nginx which is first 7 tutorials
 // var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

  $.post(url, 
  {
      total_sqft: parseFloat(total_sqft.value),
      bhk: bhk,
      bath: bathrooms,
      area: area.value

  },function(data, status) 
  {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + "  Ksh</h2>";
      console.log(status);
  })
}


function onPageLoad() {
  console.log( "document loaded" );
   var url = "http://127.0.0.1:5000/get_area_names"; // Use this if you are NOT using nginx which is first 7 tutorials
  //var url = "/api/get_area_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  $.get(url,function(data, status)
   {
      console.log("got response for get_area_names request");
      if(data)
       {
          var area = data.area;
          var uiarea = document.getElementById("uiarea");
          $('#uiarea').empty();
          for(var i in area)
           {
              var opt = new Option(area[i]);
              $('#uiarea').append(opt);
          }
      }
  });
}
window.onload = onPageLoad;


