import HandleCRUDPromiseMixin from 'appkit/controllers/mixins/handle-crud-promise';

var TreatmentsAddController = Ember.ObjectController.extend(HandleCRUDPromiseMixin, {
    needs: 'car',
    transitions: { addUpdate: 'treatment' },
    actions: {
        addTreatment: function() {
            var car = this.get('controllers.car').get('model');
            var doneBy = this.get('doneBy');
            var description = this.get('description');
            var date = this.get('date');
            var kilometrage = this.get('kilometrage');
            var reason = this.get('reason');
            var category = this.get('category');
            var partsReplaced = this.get('partsReplaced');
            var treatment = this.store.createRecord('treatment',
                {
                    car: car,
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
