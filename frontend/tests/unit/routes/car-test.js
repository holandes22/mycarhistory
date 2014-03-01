import CarRoute from 'appkit/routes/cars';


var route;
module('Unit - CarRoute', {
  setup: function(){
    var container = isolatedContainer([
      'route:cars:car'
    ]);
    route = container.lookup('route:cars:car');
  }
});

test("it exists", function(){
    ok(route);
    ok(route instanceof CarRoute);
});
