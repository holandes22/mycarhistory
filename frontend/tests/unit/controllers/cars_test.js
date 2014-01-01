var App;
var controller;


module('Unit - CarController', {
    setup: function(){
        App = startApp();
        controller = App.__container__.lookup('controller:cars');
        controller.set('model', {});
        controller.set('brand', 'fake_brand');
        controller.set('model.model', 'fake_model');
        controller.set('year', '2000');
        controller.set('amountOfOwners', 1);
        controller.set('gearboxType', 1);
    },
    teardown: function() {
        Ember.run(App, 'destroy');
    }
});

test('it creates record using correct attributes', function(){

    Ember.run(function(){
        controller.addEditSucceded.bind = sinon.stub();
        controller.addFailed.bind = sinon.stub();
        var car = sinon.stub();
        var promise = sinon.stub();
        promise.then = sinon.stub();
        car.save = sinon.stub().returns(promise);
        controller.store.createRecord = sinon.stub().returns(car);

        controller.send('addCar');

        ok(
            controller.store.createRecord.calledOnce,
            'createRecord was called more than once by addCar'
        );
        ok(
            controller.store.createRecord.calledWith(
                'car',
                {brand:'fake_brand', model:'fake_model', year:'2000', amountOfOwners: 1, gearboxType: 1}
            ),
            'createRecord was not called with the correct attributes'
        );
    });
});

test('it transitions to new car on add car success', function(){

    controller.transitionToRoute = sinon.stub();
    var car = sinon.stub();
    car.get = sinon.stub().returns(1);
    controller.addEditSucceded(car);
    ok(controller.transitionToRoute.calledWith('car', 1));

});

test('it shows validation errors if response is 400', function(){

    var car = sinon.stub();
    car.deleteRecord = sinon.stub();
    controller.record = car;
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

    controller.addFailed(error);

    deepEqual(expectedErrors, controller.get('errors'));
    ok(car.deleteRecord.calledOnce);
});

test('it fires an error event through ApplicationController', function(){
    var error = sinon.stub();
    error.status = 500;
    var appController = sinon.stub();
    appController.send = sinon.stub();
    controller.get = sinon.stub().returns(appController);
    controller.addFailed(error);
    ok(appController.send.calledWith('error', error));
});
