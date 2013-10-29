MyCarHistory.Car = DS.Model.extend({
  brand: DS.attr('string'),
  model: DS.attr('string'),
  year: DS.attr('number'),
  fullName: function() {
    return this.get('brand') + ' ' + this.get('model') + ' - ' + this.get('year');
  }.property('brand', 'model', 'year')
});
