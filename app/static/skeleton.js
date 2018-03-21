
$(document).ready(function() {
    $(".delete").click(function(){
        var ThisDestination = ($(this).parent().prevAll('td').eq(2).text())
        console.log(ThisDestination)
        // $(this).parent().parent().remove()
    }); 
});

$(document).ready(function() {
    $('select').material_select();
});

