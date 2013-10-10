jQuery( document ).ready(function( $ ) {

    function showCarList(){
        if ( typeof CURRENT_USER_ID != 'undefined'){
            var url = '/api/v1/users/' + CURRENT_USER_ID + '/cars/'
            $.get(url=url).done(function( data) {
                console.log(data)
                var html = '<ul>';
                $.each(data.results, function(index, value){
                    html += '<li>' + value.brand + '</li>';
                });
                html += '</ul>';
                $('#carList').html(html)
            });
        }
    };

    $('body').on('click', '#showCarListButton', showCarList);

});
