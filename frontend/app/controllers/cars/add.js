import Ember from 'ember';
import HandleCRUDPromiseMixin from 'app-kit/controllers/mixins/handle-crud-promise';
import CarControllerMixin from 'app-kit/controllers/mixins/car';

var CarsAddController = Ember.ObjectController.extend(HandleCRUDPromiseMixin, CarControllerMixin, {
    transitions: { addUpdate: 'car' },
    actions: {
        addCar: function() {
            var brand = this.get('brand');
            var model = this.get('model.model');
            var year = this.get('year');
            var amountOfOwners = this.get('amountOfOwners');
            var gearboxType = this.get('gearboxType');
            var car = this.store.createRecord('car',
                {
                    brand: brand,
                    model: model,
                    year: year,
                    amountOfOwners: amountOfOwners,
                    gearboxType: gearboxType
                }
            );
            this.record = car;
            car.save().then(
                this.addUpdateSucceeded.bind(this),
                this.addUpdateFailed.bind(this)
            );

        }

    }

});

export default CarsAddController;
