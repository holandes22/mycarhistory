import CarsRoute from 'appkit/routes/cars';


var route;
module('Unit - CarsRoute', {
    setup: function(){
        var container = isolatedContainer([
          'route:cars'
        ]);

        route = container.lookup('route:cars');
    },
});

test("it exists", function(){
    ok(route);
    ok(route instanceof CarsRoute);
});
