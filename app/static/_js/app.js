$(document).ready(function(){
	setup();
	setup_did_finish();
});

function setup() {
	$('.not-implemented').on('click', handle_missing_functionality); 
}

function setup_did_finish() {
	$('.cloak').removeClass('cloak');
}

function handle_missing_functionality() {
	alert('NOT IMPLEMENTED\n\n' + $(this).attr('msg'))
}