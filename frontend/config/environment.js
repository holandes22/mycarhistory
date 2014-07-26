/* jshint node: true */

module.exports = function(environment) {
  var ENV = {
    environment: environment,
    baseURL: '/',
    locationType: 'auto',
    EmberENV: {
      FEATURES: {
        // Here you can enable experimental features on an ember canary build
        // e.g. 'with-controller': true
      }
    },

    APP: {
      // Here you can pass flags/options to your application instance
      // when it is created
    }
  };

  if (environment === 'development') {
    // ENV.APP.LOG_RESOLVER = true;
    ENV.APP.LOG_ACTIVE_GENERATION = true;
    // ENV.APP.LOG_TRANSITIONS = true;
    // ENV.APP.LOG_TRANSITIONS_INTERNAL = true;
    ENV.APP.LOG_VIEW_LOOKUPS = true;

    ENV.APP.API_HOST = 'http://localhost:8888/api/v1';

    // TODO: Use API_NAMESPACE once ember-django-adapter 0.0.3 is released
    // ENV.APP.API_HOST = 'http://localhost:8888';
    // ENV.APP.API_NAMESPACE = 'api/v1';
  }

  if (environment === 'test') {
    ENV.APP.API_HOST = 'http://localhost:8000';
    ENV.APP.API_NAMESPACE = 'api/v1';
  }

  if (environment === 'production') {
    ENV.APP.API_HOST = 'https://api.mycarhistory.com';
    ENV.APP.API_NAMESPACE = 'v1';
  }

  return ENV;
};
