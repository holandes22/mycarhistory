MyCarHistory.Car = DS.Model.extend({
    brand: DS.attr('string'),
    model: DS.attr('string'),
    year: DS.attr('number'),
    gearboxType: DS.attr('number'),
    amountOfOwners: DS.attr('number'),
    treatments: DS.hasMany('treatment', { async: true }),

    fullName: function() {
        return this.get('brand') + ' ' + this.get('model') + ' - ' + this.get('year');
    }.property('brand', 'model', 'year'),

    gearboxTypeName: function() {
        return this.get('gearboxType') === 1 ? 'Manual' : 'Automatic';
    }.property('gearboxType'),

    isAutomatic: function() {
        return this.get('gearboxType') === 2;
    }.property('gearboxType')


});

