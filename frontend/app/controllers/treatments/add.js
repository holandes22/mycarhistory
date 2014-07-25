import HandleCRUDPromiseMixin from 'app-kit/controllers/mixins/handle-crud-promise';
import TreatmentControllerMixin from 'app-kit/controllers/mixins/treatment';

var TreatmentsAddController = Ember.ObjectController.extend(HandleCRUDPromiseMixin, TreatmentControllerMixin, {
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
            this.recordParent = car;
            treatment.save().then(
                this.addUpdateSucceeded.bind(this),
                this.addUpdateFailed.bind(this)
            );
        }
    }

});

export default TreatmentsAddController;
