test("Car fullName include brand, model and year", function() {
  console.log(MyCarHistory.Car)
  var car = DS.store.createRecord('car', {brand: 'fake_b', model: 'fake_m', year: 2001});
  equal('fake_b fake_m - 2000', car.get('fullName'));
});
