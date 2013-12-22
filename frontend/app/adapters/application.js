var ApplicationAdapter = DS.DjangoRESTAdapter.extend({
    namespace: window.ENV.apiNamespace,
    host: window.ENV.apiURL
});

export default ApplicationAdapter;
