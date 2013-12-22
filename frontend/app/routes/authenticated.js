import setAuthHeader from 'appkit/utils/set_auth_headers';

var AuthenticatedRoute = Ember.Route.extend({
    beforeModel: function(transition) {
        if ( window.sessionStorage.getItem('loggedInUser') ) {
            setAuthHeader();
            this.transitionTo(transition.targetName);
        } else {
            this.transitionTo('login');
        }
    }
});

export default AuthenticatedRoute;
