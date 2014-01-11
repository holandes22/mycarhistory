import HandleCRUDPromiseMixin from 'appkit/controllers/mixins/handle_crud_promise';
import CarControllerMixin from 'appkit/controllers/mixins/car';

var CarController = Ember.ObjectController.extend(HandleCRUDPromiseMixin, CarControllerMixin, {
    record: null,
    errors: null,
    transitions: {
        addUpdate: 'car',
        delete: 'cars'
    },

    actions: {
        updateCar: function(car) {
            car.save().then(
                this.addUpdateSucceeded.bind(this),
                this.addUpdateFailed.bind(this)
            );
        },

        deleteCar: function(car) {
            car.deleteRecord();
            var self = this;
            car.save().then(
                this.deleteSucceeded.bind(this),
                this.deleteFailed.bind(this)
            );
        }
    }
});

export default CarController;
