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
