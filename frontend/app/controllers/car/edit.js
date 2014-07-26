import Ember from 'ember';
import HandleCRUDPromiseMixin from 'app-kit/controllers/mixins/handle-crud-promise';
import CarControllerMixin from 'app-kit/controllers/mixins/car';

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
