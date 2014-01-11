var HandleCRUDPromiseMixin = Ember.Mixin.create({
    needs: 'application',

    addUpdateSucceeded: function(record) {

        $('.modal').modal('hide');  // TODO: View logic, Should be placed elsewhere, where??
        var id = record.get('id');
        this.transitionToRoute(this.transitions.addUpdate, id);
    },
    addUpdateFailed: function(error) {
        if (error.status === 400) {
            this.record.deleteRecord();
            var errors = {};
            var errorsFromAPI = error.responseJSON;
            Ember.$.each(errorsFromAPI, function(key, value){
                var camelCaseKey = Ember.String.camelize(key);
                errors[camelCaseKey] = value[0];
            });
            this.set('errors', errors);
        } else {
            $('.modal').modal('hide');
            this.get('controllers.application').send('error', error);
        }
    },

});

export default HandleCRUDPromiseMixin;
