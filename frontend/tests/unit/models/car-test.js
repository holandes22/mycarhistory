import GEARBOX_TYPES from 'appkit/definitions/gearbox-types';

var App, store;

module('Unit - CarModel', {
    setup: function(){
        App = startApp();
        store = App.__container__.lookup('store:main');
    },
    teardown: function() {
        Ember.run(App, 'destroy');
    }
});


var createCar = function(data) {
    var car;
    Ember.run(function(){
        car = store.createRecord('car', data);
    });
    return car;
};

test("Car fullName include brand, model and year", function() {
    var car = createCar({ brand: 'fake_b', model: 'fake_m', year: 2000 });
    equal(
        'fake_b fake_m - 2000',
        car.get('fullName'),
        'fullName should be composed by brand, model and year'
    );

});

test("Car gearboxType should either be manual or automatic", function() {
    expect(0);
});

test("Car gearboxType raises error if value not manual nor automatic", function() {
    expect(0);
});

test("Car isAutomatic is true when gearboxType is 'automatic'", function() {
    var car = createCar({ gearboxType: GEARBOX_TYPES.automatic.type });
    ok(
        car.get('isAutomatic'),
        'isAutomatic should return true if gearboxType is automatic'
    );
});

test("Car isAutomatic is false when gearboxType is 'manual'", function() {
    var car = createCar({ gearboxType: GEARBOX_TYPES.manual.type });
    equal(
        false,
        car.get('isAutomatic'),
        'isAutomatic should return false if gearboxType is manual'
    );
});

test("Car gearboxTypeName is Manual when gearboxType is 'manual'", function() {
    var car = createCar({ gearboxType: GEARBOX_TYPES.manual.type });
    equal(
        'Manual',
        car.get('gearboxTypeName'),
        'gearboxTypeName should return Manual if gearboxType is manual'
    );
});

test("Car gearboxTypeName is Automatic when gearboxType is 'automatic'", function() {
    var car = createCar({ gearboxType: GEARBOX_TYPES.automatic.type });
    equal(
        'Automatic',
        car.get('gearboxTypeName'),
        'gearboxTypeName should return Automatic if gearboxType is automatic'
    );
});
