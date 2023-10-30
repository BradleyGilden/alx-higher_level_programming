$.ajax({
  url: 'https://swapi-api.hbtn.io/api/people/5/?format=json', // URL to send the request
  method: 'GET', // HTTP method (GET, POST, etc.)
  dataType: 'json', // Expected data type
  success: (data) => {
    // This function is executed if the request is successful
    $('DIV#character').text(data.name);
  }
});
