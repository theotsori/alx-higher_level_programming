// Script that add <li> element when div is clicked
$(document).ready(function() {
  const addItemButton = $('#add_item');
  const list = $('.my_list');
  addItemButton.on("click", function() {
    const newItem = $("<li>Item<li>");
    list.append(newItem);
  });
});
