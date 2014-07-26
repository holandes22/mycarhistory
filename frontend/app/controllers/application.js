import Ember from 'ember';
import setAuthHeader from 'app-kit/utils/set-auth-headers';

var ApplicationController = Ember.ObjectController.extend({
    needs: ['logout', 'error'],
    loggedInUser: null,
    loginError: null,
    init: function() {
        this._super();
        var controller = this;
        controller.set('loggedInUser',  window.sessionStorage.getItem('loggedInUser'));
        window.navigator.id.watch({
            // Force Persona to call login by setting loggedInUser: null
            // https://developer.mozilla.org/en-US/docs/Web/API/navigator.id.watch
            loggedInUser: null,
            onlogin: function(assertion) {
                if ( !controller.get('loggedInUser') ) {
                    window.jQuery.ajax({
                        type: 'POST',
                        data: { assertion: assertion },
                        url: window.ENV.apiURL + '/' + window.ENV.apiNamespace + '/auth/login/',
                    }).then(
                        function(data) {
                            controller.set('loggedInUser', data.email);
                            window.sessionStorage.setItem('loggedInUser', data.email);
                            window.sessionStorage.setItem('loggedInUserToken', data.token);
                            setAuthHeader();
                            // TODO: get next from server and redirect to that
                            controller.transitionToRoute('cars');
                        },
                        function(error) {
                            // Probably server down
                            controller.set('loginError', error);
                            window.navigator.id.logout();
                        }
                    );
                }
            },
            onlogout: function() {
                window.sessionStorage.clear();
                if ( controller.loginError ) {
                    var message = 'Log In failed.';
                    var hint = (controller.loginError.status === 0) ? ' Is server up?' : '';

                    controller.get('controllers.error').set('status', controller.loginError.status);
                    controller.get('controllers.error').set('message', message);
                    controller.get('controllers.error').set('hint', hint);

                    controller.transitionToRoute('error');
                } else {
                    window.location.replace('/');
                }
            }
        });
    },

    actions: {
        logout: function() {
            this.get('controllers.logout').send('logout');
        }
    }
});

export default ApplicationController;
