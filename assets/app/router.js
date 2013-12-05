App.Router.map(function() {
    this.resource('cars', function() {
        this.resource('car', { path: ':car_id' }, function() {
            this.resource('treatments', function() {
                this.resource('treatment', { path: ':treatment_id' });
            });
        });
    });
    this.route("error404", { path: '*:' });
});

App.Error404Route = Ember.Route.extend({
    renderTemplate: function() {
        this.render('404');
    }
});

App.CarsRoute = Ember.Route.extend({
    model: function() {
        return this.store.find('car');
    },
});

App.TreatmentsRoute = Ember.Route.extend({
    model: function(params, transition, queryParams) {
        return this.store.find('treatment',
            { car: transition.params.car_id }
        );
    }
});
