var App;
var carsAddController;
var carEditController;
var carDeleteController;


module('Unit - Cars CRUD Controller', {
    setup: function(){
        App = startApp();
        carsAddController = App.__container__.lookup('controller:cars/add');
        carsAddController.set('model', {});
        carsAddController.set('brand', 'fake_brand');
        carsAddController.set('model.model', 'fake_model');
        carsAddController.set('year', '2000');
        carsAddController.set('amountOfOwners', 1);
        carsAddController.set('gearboxType', 1);

        carEditController = App.__container__.lookup('controller:car/edit');
        carDeleteController = App.__container__.lookup('controller:car/delete');
    },
    teardown: function() {
        Ember.run(App, 'destroy');
    }
});

test('it creates record using correct attributes', function(){

    Ember.run(function(){
        carsAddController.addUpdateSucceeded.bind = sinon.stub();
        carsAddController.addUpdateFailed.bind = sinon.stub();
        var car = sinon.stub();
        var promise = sinon.stub();
        promise.then = sinon.stub();
        car.save = sinon.stub().returns(promise);
        carsAddController.store.createRecord = sinon.stub().returns(car);

        carsAddController.send('addCar');

        ok(
            carsAddController.store.createRecord.calledOnce,
            'createRecord was called more than once by addCar'
        );
        ok(
            carsAddController.store.createRecord.calledWith(
                'car',
                {brand:'fake_brand', model:'fake_model', year:'2000', amountOfOwners: 1, gearboxType: 1}
            ),
            'createRecord was not called with the correct attributes'
        );
    });
});

test('it transitions to new car on add car success', function(){

    carsAddController.transitionToRoute = sinon.stub();
    var car = sinon.stub();
    car.get = sinon.stub().returns(1);
    carsAddController.addUpdateSucceeded(car);
    ok(carsAddController.transitionToRoute.calledWith('car', 1));

});

test('it shows validation errors if response is 400', function(){

    var car = sinon.stub();
    car.deleteRecord = sinon.stub();
    carsAddController.record = car;
    var error = sinon.stub();
    error.status = 400;
    error.responseJSON = {
        amount_of_owners: ['This field is required.'],
        year: ['Select a valid choice. 2014 is not one of the available choices.']
    };
    var expectedErrors = {
        amountOfOwners: 'This field is required.',
        year: 'Select a valid choice. 2014 is not one of the available choices.'
    };

    carsAddController.addUpdateFailed(error);

    deepEqual(expectedErrors, carsAddController.get('errors'));
    ok(car.deleteRecord.calledOnce);
});

test('it transitions to cars on delete car success', function(){
    carDeleteController.transitionToRoute = sinon.stub();
    carDeleteController.deleteSucceeded(sinon.stub());
    ok(carDeleteController.transitionToRoute.calledWith('cars'));
});

