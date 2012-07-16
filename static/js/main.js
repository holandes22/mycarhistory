function addActiveClass(element){
    $(element).parent().siblings().removeClass('active')
    $(element).parent().addClass('active')
}

function hideFormFieldTooltips(){
	// Need to be separated and not boud to hide event of modal dialog, since 
	// datepicker hide event would also trigger it and we don't want that.
	$('.form_field').tooltip('hide');
}

function loadCreateDialog(form_selector, dialog_selector, matchString, class_selector, sidebar_url){
	$.ajax({
		url: $(form_selector).attr('action'),
		type: 'POST',
		data:  $(form_selector).serialize(),
		success: function(data, textStatus, jqXHR){
			hideFormFieldTooltips();
			if(data.match(matchString)){
				// We got errors in form
				$(dialog_selector).html(data).modal('show');
				options = {trigger: 'manual', placement: 'right'}
				$('.form_field').tooltip(options).tooltip('show');
				return false;
			}
			$(dialog_selector).modal('hide');
			$('#sidebar').load(sidebar_url, function(){
				// Show the last adition
				$(class_selector + ":last").trigger('click');
			});
		},
	})
}

function loadUpdateDialog(form_selector, dialog_selector, matchString, entry_selector){
	$.ajax({
		url: $(form_selector).attr('action'),
		type: 'POST',
		data:  $(form_selector).serialize(),
		success: function(data, textStatus, jqXHR){
			hideFormFieldTooltips();
			if(data.match(matchString)){
				// We got errors in form
				$(dialog_selector).html(data).modal('show');
				options = {trigger: 'manual', placement: 'right'}
				$('.form_field').tooltip(options).tooltip('show');
				return false;
			}
			$(dialog_selector).modal('hide');
			$(entry_selector).trigger('click');
		},
	})	
}

function loadDeleteConfirmDialog(form_selector, dialog_selector, redirect_to){
	$.ajax({
		url: $(form_selector).attr('action'),
		type: 'POST',
		data:  $(form_selector).serialize(),
		success: function(data, textStatus, jqXHR){
			$(dialog_selector).modal('hide');
			window.location.replace(redirect_to);
		},
	    error: function(jqXHR, textStatus, errorThrown){
	    	$(dialog_selector).modal('hide');
    		$('#body-content').html(jqXHR.responseText);
    	}
	})	
}

$(document).ready(function () {
    $('.dropdown-toggle').dropdown();
    $(".collapse").collapse();
    
    $('.mechanic-details, .car-details').live('click', function (e) {
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