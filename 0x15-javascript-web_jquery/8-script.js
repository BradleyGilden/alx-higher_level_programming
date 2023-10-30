$.ajax({
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  method: 'GET',
  dataType: 'json',
  success: (filmData) => {
    for (let entry of filmData.results) {
      $('UL#list_movies').append(`<li>${entry.title}</li>`);
    }
  }
});
