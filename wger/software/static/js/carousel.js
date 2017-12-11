/* Script to animate software features. Needs improvement. */
$( document ).ready( function() {
  // Start script when document is ready
	animateCarouselItems();
});

function animateCarouselItems() {

	var current_item = 0; // start at the first item
	var container_width = $('#carousel_container').width(); // responsive width: viewport width
	var item_list = $('#carousel_container ul'); // item container

	setInterval( function() {

		// console.log(item_list.children());

		// iterate over list of items, sliding the current to the left, by the viewport width
		// hiding it and revealing the next at the end of the animation
		$(item_list.children()[current_item]).animate({marginLeft: - container_width}, 1000);
		// then add current item to the end of the list for purposes of looping the animation
		item_list.append(item_list.children()[current_item].outerHTML);
		current_item ++;


	}, 3000 );
}
