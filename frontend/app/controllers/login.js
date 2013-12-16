var LoginController = Ember.ObjectController.extend({

    currentUser: null,

    actions: {
        navigatorRequest: function() {
            window.navigator.id.request();

        }
    }
});

export default LoginController;
