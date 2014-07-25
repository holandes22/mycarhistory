import Ember from 'ember';

var Error404Route = Ember.Route.extend({
    renderTemplate: function() {
        this.render('404');
    }
});

export default Error404Route;
