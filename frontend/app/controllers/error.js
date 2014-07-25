import Ember from 'ember';

var ErrorController = Ember.ObjectController.extend({
    status: null,
    message: null,
    hint: null,
    responseJSON: null
});

export default ErrorController;
