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
                this.addUpdateSucceded.bind(this),
                this.addUpdateFailed.bind(this)
            );
        },

        deleteCar: function(car) {
            car.deleteRecord();
            var self = this;
            car.save().then(
                function() {
                    self.transitionToRoute('cars');
                },
                function(error) {
                    window.alert(error);
                }
            );
        }
    }
});

export default CarController;
