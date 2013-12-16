import CarControllerMixin from 'appkit/controllers/mixins';

var CarsController = Ember.ObjectController.extend(CarControllerMixin, {
    needs: 'application',
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
            var self = this; // CarsController
            car.save().then(
                function(newCar) {
                    $('.modal').modal('hide');  // TODO: View logic, Should be placed elsewhere, where??
                    var newCarId = newCar.get('id');
                    self.transitionToRoute('car', newCarId);
                },
                function(error) {
                    if (error.status === 400) {
                        car.deleteRecord();
                        var errors = {};
                        var errorsFromAPI = error.responseJSON;
                        Ember.$.each(errorsFromAPI, function(key, value){
                            var camelCaseKey = Ember.String.camelize(key);
                            errors[camelCaseKey] = value[0];
                        });
                        self.set('errors', errors);
                    } else {
                        $('.modal').modal('hide');
                        self.get('controllers.application').send('error', error);
                    }
                }
            );
        }

    }

});

export default CarsController;
