import GEARBOX_TYPES from 'appkit/definitions/gearbox_types';
import YEAR_LIST from 'appkit/definitions/year_list';

var CarControllerMixin = Ember.Mixin.create({
    gearboxTypes: [
        {label: GEARBOX_TYPES.manual, type: 'manual'},
        {label: GEARBOX_TYPES.automatic, type: 'automatic'}
    ],
    years: YEAR_LIST
});

export default CarControllerMixin;
