import HandleCRUDPromiseMixin from 'app-kit/controllers/mixins/handle-crud-promise';
import CarControllerMixin from 'app-kit/controllers/mixins/car';

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
