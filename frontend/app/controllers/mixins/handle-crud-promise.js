import Ember from 'ember';

var HandleCRUDPromiseMixin = Ember.Mixin.create({
    record: null,
    recordParent: null,
    errors: null,
    needs: 'error',

    genericErrorHandler: function(error) {
        this.get('controllers.error').set('status', error.status);
        this.get('controllers.error').set('responseJSON', error.responseJSON);
        this.transitionToRoute('error');
    },

    addUpdateSucceeded: function(record) {
        var id = record.get('id');
        if (this.recordParent) {
            this.recordParent.reload();
        }
        this.transitionToRoute(this.transitions.addUpdate, id);
    },
    addUpdateFailed: function(error) {
        this.record.deleteRecord();
        if (error.status === 400) {
            var errors = {};
            var errorsFromAPI = error.responseJSON;
            Ember.$.each(errorsFromAPI, function(key, value){
                var camelCaseKey = Ember.String.camelize(key);
                errors[camelCaseKey] = value[0];
            });
            this.set('errors', errors);
        } else {
            this.genericErrorHandler(error);
        }
    },
    deleteSucceeded: function(record) {
        this.transitionToRoute(this.transitions.delete);
    },
    deleteFailed: function(error) {
        this.genericErrorHandler(error);
    }

});

export default HandleCRUDPromiseMixin;
