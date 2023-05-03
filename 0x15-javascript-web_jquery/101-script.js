/* JavaScript script that adds, removes and clears LI 
   elements from a list when the user clicks */
$(document).ready(function () {
  $('#add_item').click(function () {
    $('.my_list').append('<li>Item</li>');
  });

  $('#remove_item').click(function () {
    const items = $('.my_list li');
    if (items.length > 0) {
      items[items.length - 1].remove();
    }
  });

  $('#clear_list').click(function () {
    $('.my_list').empty();
  });
});
