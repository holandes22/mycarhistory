MyCarHistory.CarController = Ember.ObjectController.extend({
    isEditing: false,

    actions: {
        edit: function(){
            this.set('isEditing', true);
        },

        doneEditing: function(event){
            car = this.get('model')
            this.set('isEditing', false);
            this.get('store').find('car', car.id).then(function(car){
                car.save()
            });
        }
    }
});
