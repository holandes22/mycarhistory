import YEAR_LIST from 'appkit/definitions';
import GEARBOX_TYPES from 'appkit/definitions';

var CarControllerMixin = Ember.Mixin.create({
    gearboxTypes: [
        {label: GEARBOX_TYPES['1'], type: 1},
        {label: GEARBOX_TYPES['2'], type: 2}
    ],
    years: YEAR_LIST
});

export default CarControllerMixin;
