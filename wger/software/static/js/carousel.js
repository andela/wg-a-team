/* Script to animate software features. Needs improvement. */
function animateCarouselItems() {
  var currentItem = 0; // start at the first item
  var containerWidth = $('#carousel_container').width(); // responsive width: viewport width
  var itemList = $('#carousel_container ul'); // item container

  setInterval(function () {
		// console.log(itemList.children());
		// iterate over list of items, sliding the current to the left, by the viewport width
		// hiding it and revealing the next at the end of the animation
    $(itemList.children()[currentItem]).animate({ marginLeft:-containerWidth }, 1000);
		// then add current item to the end of the list for purposes of looping the animation
    itemList.append(itemList.children()[currentItem].outerHTML);
    currentItem++;
	}, 3000);
}

$(document).ready(function () {
  // Start script when document is ready
  animateCarouselItems();
});
