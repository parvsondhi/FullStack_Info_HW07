$(document).ready(function(){
	$(document).on('click', 'button.remove-btn', function(){
		var trip = $(this).attr('id');
		$(this).parent().parent().remove();
		$.post('/delete', {
			'trip': trip
		});
	});
});