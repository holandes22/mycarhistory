var TreatmentsRoute = Ember.Route.extend({
    model: function(params, transition, queryParams) {
        return this.store.find('treatment',
            { car: transition.params.car_id }
        );
    }
});

export default TreatmentsRoute;

