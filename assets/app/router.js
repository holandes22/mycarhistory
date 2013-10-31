MyCarHistory.Router.map(function() {
    this.resource('cars', function() {
        this.resource('car', { path: ':car_id' }, function() {
            this.resource('treatments', function() {
                this.resource('treatment', { path: ':treatment_id' });
            });
        });
    });
});

MyCarHistory.CarsRoute = Ember.Route.extend({
    model: function() {
        return this.store.find('car');
    },
})
