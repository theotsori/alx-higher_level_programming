// script that fetches a char name from api
$(document).ready(function() {
  var characterDiv = $('#character');

  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
    characterDiv.text(data.name);
  });
});
