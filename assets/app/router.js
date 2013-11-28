App.Router.map(function() {
    this.resource('cars', function() {
        this.resource('car', { path: ':car_id' }, function() {
            this.resource('treatments', function() {
                this.resource('treatment', { path: ':treatment_id' });
            });
        });
    });
    this.route("error404", { path: '*:' });
    this.route("error", { path: '/error' });
});

App.Error404Route = Ember.Route.extend({
    renderTemplate: function() {
        this.render('404');
    }
});

App.ErrorRoute = Ember.Route.extend({
    renderTemplate: function() {
        this.render('error');
    }
});

App.ApplicationRoute = Ember.Route.extend({
    actions: {
        error: function(error, transition) {
            console.log('Global error catcher:', error.responseText, error.status);
            if (error.status === 404) {
                this.transitionTo('error404');
            }
            else {
                controller = this.controllerFor('error');
                controller.set('status', error.status);
                if (error.responseJSON.detail) {
                    controller.set('message', error.responseJSON.detail);
                } else {
                    controller.set('message', error.responseText);
                }
                this.transitionTo('error');
            }
        }
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
