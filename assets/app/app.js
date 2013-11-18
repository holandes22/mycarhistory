if ( typeof CURRENT_USER_AUTH_TOKEN != 'undefined'){
    var token = 'Token ' + CURRENT_USER_AUTH_TOKEN;
    DS.RESTAdapter.reopen({
        headers: { 'Authorization': token }
    });
}

var App = Ember.Application.create({
    rootElement: '#emberRoot',
});
