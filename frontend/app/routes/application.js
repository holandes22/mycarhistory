export default Ember.Route.extend({
    init: function() {
        this._super();
        var token = window.sessionStorage.getItem('loggedInUserToken');
        if ( token) {
            DS.RESTAdapter.reopen({
                headers: { 'Authorization': 'Token ' + token }
            });
        } else {
            this.transitionTo('index');
        }
    }
});
