$(document).ready(function(){
	// Remove the clicked song
	$(document).on('click', 'button.remove-btn', function(){
		$(this).parent().parent().remove();
	})
});