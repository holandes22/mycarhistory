MyCarHistory.Router.map(function() {
  this.resource('cars', function() {
    this.resource('car', { path: ':car_id' });
  });
});

MyCarHistory.CarsRoute = Ember.Route.extend({
  model: function() {
    return this.store.find('car')
  }
})

