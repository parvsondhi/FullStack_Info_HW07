

$(document).on('click', '.delete', function() {
	var row = $(this).parent().parent();
	var tripname = row.children()[0].innerHTML;
	// console.log(tripname);
	var destination = row.children()[1].innerHTML;
	// console.log(destination);
    $.post('delete-trip', {tripname:tripname, destination:destination})
    .done(function() {})
    .fail(function() { alert("error"); })
	row.remove();
});
