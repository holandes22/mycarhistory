var App;

module('Acceptances - Index', {
    setup: function(){
        fakehr.start();
        App = startApp();
    },
    teardown: function() {
        fakehr.reset();
        Ember.run(App, 'destroy');
    }
});

test('index renders', function(){
  visit('/').then(function(){
    var title = find('a.navbar-brand:first');
    equal(title.text(), 'My Car History');
  });
});
