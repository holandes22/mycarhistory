jQuery( document ).ready(function( $ ) {

    function showCarList(){
        var url = '/api/v1/cars/';
        var headers = {};
        if ( typeof CURRENT_USER_AUTH_TOKEN != 'undefined'){
            headers = { Authorization: 'Token ' + CURRENT_USER_AUTH_TOKEN };
        }
        $.ajax({
            url: url, 
            headers: headers
        })
        .done(function( data, textStatus, jqXHR ){
            var html = '<ul>';
            $.each(data.results, function(index, value){
                html += '<li>' + value.brand + '</li>';
            });
            html += '</ul>';
            $('#carList').html(html);
        })
        .fail(function( jqXHR, textStatus, errorThrown ){
            $('#carList').text(jqXHR.responseJSON.detail);
        });
    };

    $('body').on('click', '#showCarListButton', showCarList);

});
