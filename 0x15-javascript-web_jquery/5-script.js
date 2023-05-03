// Script that add <li> element when div is clicked
$(document).ready(function () {
  $('#add_item').click(function () {
    $('.my_list').append('<li>Item</li>');
  });
});
