var ApplicationAdapter = DS.DjangoRESTAdapter.extend({
    namespace: 'api/v1',
    host: 'http://localhost:8888' //TODO: Generate with Grunt according to dev/prod
});

export default ApplicationAdapter;
