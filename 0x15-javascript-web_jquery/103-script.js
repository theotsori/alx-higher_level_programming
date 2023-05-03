// script that fetches and prints how to say “Hello” depending on the language
$(document).ready(function () {
  $('#btn_translate').click(function () {
    const langCode = $('#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/?lang=${langCode}`;

    $.get(url, function (data) {
      $('#hello').text(data.hello);
    });
  });

  $('#language_code').keypress(function (event) {
    const keycode = (event.keyCode ? event.keyCode : event.which);
    if (keycode === '13') {
      $('#btn_translate').click();
    }
  });
});
