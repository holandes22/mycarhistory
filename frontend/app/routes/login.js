var LoginRoute = Ember.Route.extend({
    setupController: function(controller) {
        Ember.$.get('/browserid/page/').then(function(data) {
            var pageContent = new Ember.Handlebars.SafeString(data);
            controller.set('pageContent', pageContent);
        });
    }
});

export default LoginRoute;
