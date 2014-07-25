import AuthenticatedRoute from 'app-kit/routes/authenticated';

var CarsRoute = AuthenticatedRoute.extend({
    model: function() {
        return this.store.find('car');
    },
});

export default CarsRoute;

