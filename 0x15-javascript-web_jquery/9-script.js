// script that fetches from api and displays hello
$(function () {
  // Fetch the data from https://fourtonfish.com/hellosalut/?lang=fr
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    // Get the value of hello from the data
    const hello = data.hello;

    // Set the value of the HTML tag DIV#hello
    $('#hello').text(hello);
  });
});
