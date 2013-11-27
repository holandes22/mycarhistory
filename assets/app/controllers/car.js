App.CarControllerMixin = Ember.Mixin.create({
    gearboxTypes: [
        {label: GEARBOX_TYPES['1'] , type: 1},
        {label: GEARBOX_TYPES['2'], type: 2}
    ],
    years: YEAR_LIST
});

App.CarsController = Ember.ObjectController.extend(App.CarControllerMixin, {
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
                    var newCarId = newCar.get('id');
                    self.transitionTo('car', newCarId);
                },
                function(error) {
                    car.deleteRecord();
                    var errors = {};
                    var errorsFromAPI = error.responseJSON;
                    jQuery.each(errorsFromAPI, function(key, value){
                        var camelCaseKey = Ember.String.camelize(key);
                        errors[camelCaseKey] = value[0];
                    });
                    self.set('errors', errors);
                }
            );
        }

    }

});

App.CarController = Ember.ObjectController.extend(App.CarControllerMixin, {

    actions: {
        updateCar: function(car) {
            car.save();
        },

        deleteCar: function(car) {
            car.deleteRecord();
            car.save();
        }
    }
});
