$(document).on('click', '.delete', function() {
	var row = $(this).parent().parent();
	var tripname = row.children()[0].innerHTML;
	// console.log(tripname);
	var destination = row.children()[1].innerHTML;
	// console.log(destination);

	// need to add Ajax call
	row.remove();
});
