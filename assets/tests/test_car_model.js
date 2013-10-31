test("Car fullName include brand, model and year", function() {
    var store = MyCarHistory.__container__.lookup('store:main');

    var car = store.createRecord(MyCarHistory.Car, {brand: 'fake_b', model: 'fake_m', year: 2000});
    equal('fake_b fake_m - 2000', car.get('fullName'), 'fullName should be composed by brand, model and year');
});
