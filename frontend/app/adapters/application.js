var token = null;
Ember.$.getJSON('http://localhost:8888/api/v1/get-auth-token/').then(
    function(data) {
        token = 'Token ' + data;
    }
);

var ApplicationAdapter = DS.DjangoRESTAdapter.extend({
    namespace: 'api/v1',
    host: 'http://localhost:8888', //TODO: Generate address with Grunt according to dev/prod
    headers: { 'Authorization': token }
});

var ApplicationSerializer = DS.DjangoRESTSerializer.extend();

export default ApplicationAdapter;
export default ApplicationSerializer;

