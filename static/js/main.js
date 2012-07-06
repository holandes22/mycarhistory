function addActiveClass(element){
    $(element).parent().siblings().removeClass('active')
    $(element).parent().toggleClass('active')
}

$(document).ready(function () {
    $('.dropdown-toggle').dropdown();
    $(".collapse").collapse();
    
    $('.mechanic-details, .car-details').click(function (e) {
        addActiveClass(this);

        // Load left panel
        target = $(this).attr('data-target')
        url = $(this).attr('url')
        $(target).load(url);
    })
    
	$('#editor-dialog').bind('click-save-button', function () {
		$.ajax({
			url: $('#editor_form').attr('action'),
			type: 'POST',
			data:  $('#editor_form').serialize(),
			success: function(data, textStatus, jqXHR){
				if(data.match('invalid_form')){
					$('#editor-dialog').html(data).modal('show');
					$('.field_error').effect("highlight", { times: 3 }, 1200);
				}
			},
		})
	})
});