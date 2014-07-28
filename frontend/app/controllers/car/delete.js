import Ember from 'ember';
import HandleCRUDPromiseMixin from 'app-kit/mixins/handle-crud-promise';
import CarControllerMixin from 'app-kit/mixins/car';

var CarDeleteController = Ember.ObjectController.extend(HandleCRUDPromiseMixin, CarControllerMixin, {
    transitions: {
        delete: 'cars'
    },

    actions: {
        deleteCar: function(car) {
            car.deleteRecord();
            car.save().then(
                this.deleteSucceeded.bind(this),
                this.deleteFailed.bind(this)
            );
        }
    }
});

export default CarDeleteController;
