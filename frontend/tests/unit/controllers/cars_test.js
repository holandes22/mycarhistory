var App;
var carsController;
var carController;


module('Unit - CarController', {
    setup: function(){
        App = startApp();
        carsController = App.__container__.lookup('controller:cars');
        carsController.set('model', {});
        carsController.set('brand', 'fake_brand');
        carsController.set('model.model', 'fake_model');
        carsController.set('year', '2000');
        carsController.set('amountOfOwners', 1);
        carsController.set('gearboxType', 1);

        carController = App.__container__.lookup('controller:car');
    },
    teardown: function() {
        Ember.run(App, 'destroy');
    }
});

test('it creates record using correct attributes', function(){

    Ember.run(function(){
        carsController.addUpdateSucceeded.bind = sinon.stub();
        carsController.addUpdateFailed.bind = sinon.stub();
        var car = sinon.stub();
        var promise = sinon.stub();
        promise.then = sinon.stub();
        car.save = sinon.stub().returns(promise);
        carsController.store.createRecord = sinon.stub().returns(car);

        carsController.send('addCar');

        ok(
            carsController.store.createRecord.calledOnce,
            'createRecord was called more than once by addCar'
        );
        ok(
            carsController.store.createRecord.calledWith(
                'car',
                {brand:'fake_brand', model:'fake_model', year:'2000', amountOfOwners: 1, gearboxType: 1}
            ),
            'createRecord was not called with the correct attributes'
        );
    });
});

test('it transitions to new car on add car success', function(){

    carsController.transitionToRoute = sinon.stub();
    var car = sinon.stub();
    car.get = sinon.stub().returns(1);
    carsController.addUpdateSucceeded(car);
    ok(carsController.transitionToRoute.calledWith('car', 1));

});

test('it shows validation errors if response is 400', function(){

    var car = sinon.stub();
    car.deleteRecord = sinon.stub();
    carsController.record = car;
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

    carsController.addUpdateFailed(error);

    deepEqual(expectedErrors, carsController.get('errors'));
    ok(car.deleteRecord.calledOnce);
});

test('it fires an error event through ApplicationController when updating car fails', function(){
    var error = sinon.stub();
    error.status = 500;
    var appController = sinon.stub();
    appController.send = sinon.stub();
    carsController.get = sinon.stub().returns(appController);
    carsController.addUpdateFailed(error);
    ok(appController.send.calledWith('error', error));
});

test('it transitions to cars on delete car success', function(){
    carController.transitionToRoute = sinon.stub();
    carController.deleteSucceeded(sinon.stub());
    ok(carController.transitionToRoute.calledWith('cars'));
});

test('it fires an error event through ApplicationController when deleting car fails', function(){
    var error = sinon.stub();
    var appController = sinon.stub();
    appController.send = sinon.stub();
    carsController.get = sinon.stub().returns(appController);
    carsController.deleteFailed(error);
    ok(appController.send.calledWith('error', error));
});