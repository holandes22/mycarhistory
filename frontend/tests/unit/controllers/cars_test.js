var App;
var controller;


module('Unit - CarController', {
    setup: function(){
        fakehr.start();
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
        fakehr.reset();
        Ember.run(App, 'destroy');
    }
});

test('it creates record using correct attributes', function(){

    Ember.run(function(){
        controller.addedCarSucceded.bind = window.sinon.stub();
        controller.addedCarFailed.bind = window.sinon.stub();
        var car = window.sinon.stub();
        var promise = window.sinon.stub();
        promise.then = window.sinon.stub();
        car.save = window.sinon.stub().returns(promise);
        controller.store.createRecord = window.sinon.stub().returns(car);

        controller.send('addCar');

        ok(controller.store.createRecord.calledOnce, 'createRecord was called more than once by addCar');
        ok(
            controller.store.createRecord.calledWith(
                'car',
                {brand:'fake_brand', model:'fake_model', year:'2000', amountOfOwners: 1, gearboxType: 1}
            ),
            'createRecord was not called with the correct attributes'
        );

    });
});
