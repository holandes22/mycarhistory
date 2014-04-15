var HandleCRUDPromiseMixin = Ember.Mixin.create({
    record: null,
    needs: 'application',

    addUpdateSucceeded: function(record) {
        var id = record.get('id');
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
            this.get('controllers.application').send('error', error);
        }
    },
    deleteSucceeded: function(record) {
        this.transitionToRoute(this.transitions.delete);
    },
    deleteFailed: function(error) {
        this.get('controllers.application').send('error', error);
    }

});

export default HandleCRUDPromiseMixin;
