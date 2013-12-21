export default Ember.Route.extend({

    init: function() {
        this._super();
        if ( window.sessionStorage.getItem('loggedInUser') ) {
            this.setAuthHeader();
        }
    },
    setAuthHeader: function() {
        var token = window.sessionStorage.getItem('loggedInUserToken');
        DS.RESTAdapter.reopen({
            headers: { 'Authorization': 'Token ' + token }
        });

    }
});
