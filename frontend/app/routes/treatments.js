var TreatmentsRoute = Ember.Route.extend({
    model: function(queryParams, transition) {
        return this.store.find('treatment',
            { car: transition.params.car.car_id }
        );
    }
});

export default TreatmentsRoute;

