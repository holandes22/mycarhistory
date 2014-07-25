import Ember from 'ember';
var Router = Ember.Router.extend(); // ensure we don't share routes between all Router instances

Router.map(function() {
    this.resource('cars', function() {
        this.route('add');
        this.resource('car', { path: ':car_id' }, function() {
            this.route('edit');
            this.route('delete');
            this.resource('treatments', function() {
                this.route('add');
                this.resource('treatment', { path: ':treatment_id' });
            });
        });
    });
    this.route('user', { path: '/user/profile' });
    this.route('login');
    this.route('logout');
    this.route('about');
    this.route('error');
    this.route('error404', { path: '*:' });
});

export default Router;
