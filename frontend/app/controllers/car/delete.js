import HandleCRUDPromiseMixin from 'appkit/controllers/mixins/handle_crud_promise';
import CarControllerMixin from 'appkit/controllers/mixins/car';

var CarDeleteController = Ember.ObjectController.extend(HandleCRUDPromiseMixin, CarControllerMixin, {
    record: null,
    errors: null,
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
