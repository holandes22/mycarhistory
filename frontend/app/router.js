var Router = Ember.Router.extend(); // ensure we don't share routes between all Router instances

Router.map(function() {
    this.resource('cars', function() {
        this.resource('car', { path: ':car_id' }, function() {
            this.resource('treatments', function() {
                this.resource('treatment', { path: ':treatment_id' });
            });
        });
    });
    this.route('user', { path: '/user/profile' });
    this.route('login');
    this.route('logout');
    this.route('about');
    this.route('main');
    this.route('error');
    this.route('error404', { path: '*:' });
});

export default Router;
