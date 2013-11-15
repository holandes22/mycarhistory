App.CarsController = Ember.ObjectController.extend({

    actions: {
        addCar: function(event) {
            var brand = this.get('brand');
            var model = this.get('model.model');
            var kilometrage = this.get('kilometrage');
            var year = this.get('year');
            var amountOfOwners = this.get('amountOfOwners');
            var gearboxType = this.get('gearboxType');
            var car = this.store.createRecord('car',
                {
                    brand: brand,
                    model: model,
                    kilometrage: kilometrage,
                    year: 1979,
                    amountOfOwners: amountOfOwners,
                    gearboxType: gearboxType
                }
            );
            car.save();
        },

        deleteCar: function(car) {
            car.deleteRecord();
            car.save()
        }
    }

});

App.CarController = Ember.ObjectController.extend({

    actions: {
        updateCar: function(event) {
            car = this.get('model')
            this.get('store').find('car', car.id).then(function(car){
                car.save()
            });
        }
    }
});
