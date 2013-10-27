jQuery( document ).ready(function( $ ) {

  jQuery(document).ajaxSend(function(event, xhr, settings) {
    if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
      if ( typeof CURRENT_USER_AUTH_TOKEN != 'undefined'){
        var token = 'Token ' + CURRENT_USER_AUTH_TOKEN;
        xhr.setRequestHeader("Authorization", token);
      }
    }
  });

/*
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

*/
});

var cars = [{brand: 'b', model: 'm'}, {brand: 'bb', model: 'mm'}]
MyCarHistory = Ember.Application.create({
  rootElement: '#ember'
});


MyCarHistory.ApplicationAdapter = DS.DjangoRESTAdapter.extend({
  namespace: 'api/v1'
});

MyCarHistory.Car = DS.Model.extend({
  brand: DS.attr('string'),
  model: DS.attr('string')
});


MyCarHistory.CarsRoute = Ember.Route.extend({
  model: function() {
    return this.store.find('car')
  }
})


 
MyCarHistory.Router.map(function() {
  this.route("cars", { path : "/cars" });
});
