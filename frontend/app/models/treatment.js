import DS from "ember-data";

var TreatmentModel = DS.Model.extend({
    car: DS.belongsTo('Car'),
    doneBy: DS.attr('string'),
    description: DS.attr('string'),
    date: DS.attr('date'),
    kilometrage: DS.attr('number'),
    reason: DS.attr('string'),
    category: DS.attr('string'),
    partsReplaced: DS.attr('string')
});

export default TreatmentModel;
