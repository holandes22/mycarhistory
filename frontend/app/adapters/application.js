var ApplicationAdapter = DS.DjangoRESTAdapter.extend({
    namespace: 'api/v1',
    host: 'http://localhost:8888' //TODO: Generate address with Grunt according to dev/prod
});

var ApplicationSerializer = DS.DjangoRESTSerializer.extend();

export default ApplicationAdapter;
export default ApplicationSerializer;

