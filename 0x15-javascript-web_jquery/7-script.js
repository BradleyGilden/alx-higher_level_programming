$.ajax({
  url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
  method: 'GET',
  dataType: 'json',
  success: (data) => {
    // This function is executed if the request is successful
    $('DIV#character').text(data.name);
  }
});
