import CarControllerMixin from 'appkit/controllers/mixins/car';

var CarsController = Ember.ObjectController.extend(CarControllerMixin, {
    needs: 'application',
    car: null,
    addedCarSucceded: function(newCar) {
        $('.modal').modal('hide');  // TODO: View logic, Should be placed elsewhere, where??
        var newCarId = newCar.get('id');
        this.transitionToRoute('car', newCarId);
    },
    addedCarFailed: function(error) {
        if (error.status === 400) {
            this.car.deleteRecord();
            var errors = {};
            var errorsFromAPI = error.responseJSON;
            Ember.$.each(errorsFromAPI, function(key, value){
                var camelCaseKey = Ember.String.camelize(key);
                errors[camelCaseKey] = value[0];
            });
            this.set('errors', errors);
        } else {
            $('.modal').modal('hide');
            this.get('controllers.application').send('error', error);
        }

    },
    actions: {
        addCar: function(event) {
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
            this.car = car;
            car.save().then(
                this.addedCarSucceded.bind(this),
                this.addedCarFailed.bind(this)
            );

        }

    }

});

export default CarsController;
