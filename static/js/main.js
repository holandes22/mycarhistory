function addActiveClass(element){
    $(element).parent().siblings().removeClass('active')
    $(element).parent().toggleClass('active')
}

function hideFormFieldTooltips(){
	// Need to be separated and not boud to hide event of modal dialog, since 
	// datepicker hide event would also trigger it and we don't want that.
	$('.form_field').tooltip('hide');
}
function genericLoadDialog(form_selector, dialog_selector, onSuccessHandler, matchString, redirect_to){
	$.ajax({
		url: $(form_selector).attr('action'),
		type: 'POST',
		data:  $(form_selector).serialize(),
		success: function(data, textStatus, jqXHR){
			if(data.match(matchString)){
				// We got errors in form
				$(dialog_selector).html(data).modal('show');
				options = {trigger: 'manual', placement: 'right'}
				$('.form_field').tooltip(options).tooltip('show');
				return false;
			}
			if(onSuccessHandler && typeof onSuccessHandler == 'function'){
				onSuccessHandler();
			}
			hideFormFieldTooltips();
			$(dialog_selector).modal('hide');
			window.location.replace(redirect_to);
		},
	})
}


$(document).ready(function () {
    $('.dropdown-toggle').dropdown();
    $(".collapse").collapse();
    
    $('.mechanic-details, .car-details').click(function (e) {
        addActiveClass(this);

        // Load left panel
        target = $(this).attr('data-target')
        
        $.ajax({
        	url: $(this).attr('url'),
        	success: function(data, textStatus, jqXHR){
        		$(target).html(data);
        	},
        	error: function(jqXHR, textStatus, errorThrown){
        		$(target).html(jqXHR.responseText);
        	}
        })
    })
    

});