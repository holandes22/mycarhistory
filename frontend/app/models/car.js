import DS from "ember-data";
import GEARBOX_TYPES from 'app-kit/definitions/gearbox-types';

var CarModel = DS.Model.extend({
    brand: DS.attr('string'),
    model: DS.attr('string'),
    year: DS.attr('number'),
    gearboxType: DS.attr('string'),
    amountOfOwners: DS.attr('number'),
    treatments: DS.hasMany('treatment', { async: true }),

    fullName: function() {
        return this.get('brand') + ' ' + this.get('model') + ' - ' + this.get('year');
    }.property('brand', 'model', 'year'),

    gearboxTypeName: function() {
        return this.get('gearboxType') === GEARBOX_TYPES.manual.type ? GEARBOX_TYPES.manual.label : GEARBOX_TYPES.automatic.label;
    }.property('gearboxType'),

    isAutomatic: function() {
        return this.get('gearboxType') === GEARBOX_TYPES.automatic.type;
    }.property('gearboxType'),

});

export default CarModel;
