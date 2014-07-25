import Ember from 'ember';

var LoginController = Ember.ObjectController.extend({

    actions: {
        navigatorRequest: function() {
            var args = {siteName: 'My Car History'};
            window.navigator.id.request(args);
        }
    }
});

export default LoginController;
