import Ember from 'ember';
import Resolver from 'ember/resolver';
import loadInitializers from 'ember/load-initializers';
import determineErrorClass from 'app-kit/helpers/determine-error-class';

Ember.MODEL_FACTORY_INJECTIONS = true;

var App = Ember.Application.extend({
  modulePrefix: 'app-kit', // TODO: loaded via config
  Resolver: Resolver
});

Ember.Handlebars.registerHelper('determine-error-class', determineErrorClass);
loadInitializers(App, 'app-kit');

export default App;
