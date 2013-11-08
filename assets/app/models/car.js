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
        return this.gearboxType === 1 ? 'Manual' : 'Automatic';
    },
    isAutomatic: function() {
        return this.gearboxType === 2;
    }.property('isAutomatic')


});

MyCarHistory.Treatment = DS.Model.extend({
    car: DS.belongsTo('Car'),
    done_by: DS.attr('string'),
    description: DS.attr('string'),
    date: DS.attr('date'),
});
