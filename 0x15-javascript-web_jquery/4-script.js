// Script that toggles the class of the header
$(document).ready(function () {
  const header = $('#header');

  const toggleHeader = $('#toggle_header');

  toggleHeader.on('click', function () {
    const currentClass = header.attr('class');

    if (currentClass === 'green') {
      header.attr('class', 'red');
    } else {
      header.attr('class', 'green');
    }
  });
});
