import YEAR_LIST from 'appkit/definitions';
import GEARBOX_TYPES from 'appkit/definitions';
import CarControllerMixin from 'appkit/controllers/mixins';

var CarController = Ember.ObjectController.extend(CarControllerMixin, {

    actions: {
        updateCar: function(car) {
            car.save();
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

export default CarControllerMixin;
