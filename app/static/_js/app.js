$(document).ready(function(){
	setup();
});

function setup() {
    $('.delete-form').on('submit', submitDeleteRequest);
}

function submitDeleteRequest(e) {
    e.preventDefault();
    var endPoint = $(this).attr('action');

    $.ajax(endPoint, {
        type: 'DELETE',
        success: redirectOnSuccess
    });

}

function redirectOnSuccess (response) {
    if (response && response.redirect) {
        window.location = response.redirect_url;
    }
}