import HandleCRUDPromiseMixin from 'appkit/controllers/mixins/handle_crud_promise';

var TreatmentsAddController = Ember.ObjectController.extend(HandleCRUDPromiseMixin, {
    needs: 'application',
    transitions: { addUpdate: 'treatment' },
    actions: {
        addTreatment: function(params) {
            window.console.log(params);
            var doneBy = this.get('doneBy');
            var description = this.get('description');
            var date = this.get('date');
            var kilometrage = this.get('kilometrage');
            var reason = this.get('reason');
            var category = this.get('category');
            var partsReplaced = this.get('partsReplaced');
            var treatment = this.store.createRecord('treatment',
                {
                    doneBy: doneBy,
                    description: description,
                    date: date,
                    kilometrage: kilometrage,
                    reason: reason,
                    category: category,
                    partsReplaced: partsReplaced
                }
            );
            this.record = treatment;
            treatment.save().then(
                this.addUpdateSucceeded.bind(this),
                this.addUpdateFailed.bind(this)
            );

        }

    }

});

export default TreatmentsAddController;
