import HandleCRUDPromiseMixin from 'appkit/controllers/mixins/handle_crud_promise';
import CarControllerMixin from 'appkit/controllers/mixins/car';

var CarEditController = Ember.ObjectController.extend(HandleCRUDPromiseMixin, CarControllerMixin, {
    transitions: {
        addUpdate: 'car',
    },

    actions: {
        updateCar: function(car) {
            car.save().then(
                this.addUpdateSucceeded.bind(this),
                this.addUpdateFailed.bind(this)
            );
        }
    }
});

export default CarEditController;
