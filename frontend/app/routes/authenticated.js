import setAuthHeader from 'app-kit/utils/set-auth-headers';

var AuthenticatedRoute = Ember.Route.extend({
    beforeModel: function(transition) {
        if ( window.sessionStorage.getItem('loggedInUser') ) {
            setAuthHeader();
            this.intermediateTransitionTo(transition.targetName);
        } else {
            this.transitionTo('login');
        }
    }
});

export default AuthenticatedRoute;
