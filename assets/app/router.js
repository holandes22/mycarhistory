App.Router.map(function() {
    this.resource('cars', function() {
        this.resource('car', { path: ':car_id' }, function() {
            this.resource('treatments', function() {
                this.resource('treatment', { path: ':treatment_id' });
            });
        });
    });
    this.resource('login');
    this.resource('about');
    this.resource('main');
    this.route('error404', { path: '*:' });
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


App.LoginRoute = Ember.Route.extend({
    setupController: function(controller) {
        Ember.$.get('/browserid/page/').then(function(data) {
            var pageContent = new Ember.Handlebars.SafeString(data);
            controller.set('pageContent', pageContent);
        });
    }
});
