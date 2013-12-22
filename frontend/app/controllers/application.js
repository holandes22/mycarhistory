import setAuthHeader from 'appkit/utils/set_auth_headers';

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
                        url: 'http://localhost:8888/api/v1/auth/login/'
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
                    controller.get('controllers.error').set('status', controller.loginError.status);
                    controller.get('controllers.error').set('message', 'Log In failed. Is server up?');
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
