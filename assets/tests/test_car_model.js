test("Car fullName include brand, model and year", function() {
    var store = MyCarHistory.__container__.lookup('store:main');
    var car = store.createRecord('car', {
        brand: 'fake_b', model: 'fake_m', year: 2000
    })
    equal(
        'fake_b fake_m - 2000',
        car.get('fullName'),
        'fullName should be composed by brand, model and year'
    );
});

test("Car gearboxType should either be 1 or 2", function() {
    expect(0);
});

test("Car gearboxType raises error if value not 1 nor 2", function() {
    expect(0);
});

test("Car isAutomatic is true when gearboxType is 2", function() {
    var store = MyCarHistory.__container__.lookup('store:main');
    var car = store.createRecord('car', { gearboxType: 2 })
    ok(
        car.get('isAutomatic'),
        'isAutomatic should return true if gearboxType is 2'
    );
});

test("Car isAutomatic is false when gearboxType is 1", function() {
    var store = MyCarHistory.__container__.lookup('store:main');
    var car = store.createRecord('car', { gearboxType: 1 })
    equal(
        false,
        car.get('isAutomatic'),
        'isAutomatic should return false if gearboxType is 1'
    );
});

test("Car gearboxTypeName is Manual when gearboxType is 1", function() {
    var store = MyCarHistory.__container__.lookup('store:main');
    var car = store.createRecord('car', { gearboxType: 1 })
    equal(
        'Manual',
        car.get('gearboxTypeName'),
        'gearboxTypeName should return Manual if gearboxType is 1'
    );
});

test("Car gearboxTypeName is Automatic when gearboxType is 2", function() {
    var store = MyCarHistory.__container__.lookup('store:main');
    var car = store.createRecord('car', { gearboxType: 2 })
    equal(
        'Automatic',
        car.get('gearboxTypeName'),
        'gearboxTypeName should return Automatic if gearboxType is 2'
    );
});
