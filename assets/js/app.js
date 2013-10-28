jQuery( document ).ready(function( $ ) {

  jQuery(document).ajaxSend(function(event, xhr, settings) {
    if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
      if ( typeof CURRENT_USER_AUTH_TOKEN != 'undefined'){
        var token = 'Token ' + CURRENT_USER_AUTH_TOKEN;
        xhr.setRequestHeader("Authorization", token);
      }
    }
  });
});

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
  this.resource('cars', function() {
    this.resource('car', { path: ':car_id' });
  });
});


MyCarHistory.Router.reopen({
  location: 'history' // Avoid Hash URLs
});
