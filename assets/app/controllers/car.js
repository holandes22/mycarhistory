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
            car.save().then(
                function() {
                    self.transitionToRoute('cars', car.id);
                },
                function(error) {
                    console.log(error.status);
                    var errors = error.responseJSON;
                    for (var key in errors) {
                        console.log(key, errors[key]);
                    }
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
