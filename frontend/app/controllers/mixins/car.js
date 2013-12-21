import GEARBOX_TYPES from 'appkit/definitions/gearbox_types';

var getYearList = function() {
    var currentYear = window.moment().year();
    var startingYear = 1920;
    var years = [];
    for (var i=currentYear; i >= startingYear; i--) {
        years.push(i);
    }
    return years;
};

var CarControllerMixin = Ember.Mixin.create({
    gearboxTypes: [
        {label: GEARBOX_TYPES['1'], type: 1},
        {label: GEARBOX_TYPES['2'], type: 2}
    ],
    years: getYearList()
});

export default CarControllerMixin;
