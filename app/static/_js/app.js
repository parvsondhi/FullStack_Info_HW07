$(document).ready(function(){
	setup();
});

function setup() {
    $('.delete-form').on('submit', submitDeleteRequest);
    $('.invite-user').on('click', submitInviteUserRequest);
}

function submitDeleteRequest(e) {
    e.preventDefault();
    var endPoint = $(this).attr('action');

    $.ajax(endPoint, {
        type: 'DELETE',
        success: redirectOnSuccess
    });

}

function submitInviteUserRequest(e) {
    e.preventDefault();
    var endPoint = $(this).attr('href');

    $.ajax(endPoint, {
        type: 'POST',
        success: redirectOnSuccess
    });

}

function redirectOnSuccess (response) {
    if (response && response.redirect) {
        window.location = response.redirect_url;
    }
}