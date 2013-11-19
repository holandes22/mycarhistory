module.exports = function(config) {
  config.set({

    basePath: 'assets',
    frameworks: ['qunit'],
    // list of files / patterns to load in the browser
    files: [
      'libs/js/jquery-2.0.3.min.js',
      'libs/js/handlebars-1.0.0.js',
      'libs/js/ember.js',
      'libs/js/ember-data.js',
      'libs/js/bootstrap.min.js',
      'libs/js/ember-data-django-rest-adapter.js',
      'libs/js/moment.min.js',

      'app/*.js',
      'app/adapters/*.js',
      'app/controllers/*.js',
      'app/views/*.js',
      'app/models/*.js',
      'tests/*.js'
    ],
    // list of files to exclude
    exclude: [],
    reporters: ['progress'],
    port: 9876,
    colors: true,
    logLevel: config.LOG_INFO,
    autoWatch: true,
    browsers: ['PhantomJS'],
    captureTimeout: 60000,
    singleRun: false
  });
};
