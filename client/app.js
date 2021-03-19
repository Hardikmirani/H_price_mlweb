function getBathValue() {
  var uiBathrooms = document.getElementsByName("uiBathrooms");
  for(var i in uiBathrooms) {
    if(uiBathrooms[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getBedroomsValue() {
  var uiBedrooms = document.getElementsByName("uiBedrooms");
  for(var i in uiBedrooms) {
    if(uiBedrooms[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var sqft_living = document.getElementById("uiSqft_living");
  var bedrooms = getBedroomsValue();
  var bathrooms = getBathroomsValue();
  var city = document.getElementById("uiCity");
  var estPrice = document.getElementById("uiEstimatedPrice");

  var url = "http://127.0.0.1:3000/predict_home_price"; //Use this if you are NOT using nginx which is first 7 tutorials
  //var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

  $.post(url, {
      total_sqft: parseFloat(sqft_living.value),
      bedrooms: bedrooms,
      bathrooms: bathrooms,
      city: city.value
  },function(data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Dollars</h2>";
      console.log(status);
  });
}

function onPageLoad() {
  console.log( "document loaded" );
  var url = "http://127.0.0.1:3000/get_city_names"; // Use this if you are NOT using nginx which is first 7 tutorials
  //var url = "/api/get_city_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  $.get(url,function(data, status) {
      console.log("got response for get_city_names request");
      if(data) {
          var city= data.city;
          var uicity = document.getElementById("uiCity");
          $('#uiCity').empty();
          for(var i in city) {
              var opt = new Option(city[i]);
              $('#uiCity').append(opt);
          }
      }
  });
}