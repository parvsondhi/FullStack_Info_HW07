$('#login').on('click', function login() {
	var user_name = $("input[name=user_name]").val();
	var password = $("input[name=password]").val();
		$.post("login", {user_name: user_name, 
		password: password},
		function(response) {
			$(document.body.parentNode).html(response)
		});
});

$('#create_trip').on('click', function createTrip() {
	var trip_name = $("input[name=trip_name]").val();
	var destination = $("input[name=destination]").val();
		$.post("create_trip", {trip_name: trip_name, 
		destination: destination},
		function(response) {
			$(document.body.parentNode).html(response)
		});
});

$("#site-title-wrapper").on('click', function goHome() {
	window.location.href = '/';
});

// $(document).ready(function applySliderLabels() {
// 	var currentValue = $("#fe-before").val();
// 	$("#fe-before").next().html(currentValue);

// 	currentValue = $("#fe-after").val();
// 	$("#fe-after").next().html(currentValue);
// });

$("input[type='range']").on('change', function updateLabel() {
	var currentValue = $(this).val();
	$(this).next().html(currentValue);
});
