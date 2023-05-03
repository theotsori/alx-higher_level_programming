// script that fetches and lists the title fo all movies
$(document).ready(function () {
  // Get the list_movies element
  const listMovies = $('#list_movies');

  // Make the API call to fetch the list of movies
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    // Loop through the movie results and add each title to the list_movies element
    $.each(data.results, function (index, movie) {
      listMovies.append('<li>' + movie.title + '</li>');
    });
  });
});
