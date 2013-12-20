import GEARBOX_TYPES from 'appkit/definitions/gearbox_types';

var CarModel = DS.Model.extend({
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
        return this.get('gearboxType') === 1 ? GEARBOX_TYPES['1'] : GEARBOX_TYPES['2'];
    }.property('gearboxType'),

    isAutomatic: function() {
        return this.get('gearboxType') === 2;
    }.property('gearboxType'),

});

export default CarModel;
