MyCarHistory.Treatment = DS.Model.extend({
    car: DS.belongsTo('Car'),
    done_by: DS.attr('string'),
    description: DS.attr('string'),
    date: DS.attr('date'),
    kilometrage: DS.attr('number'),
    reason: DS.attr('number'),
    category: DS.attr('number'),
    partsReplaced: DS.attr('string')
});
