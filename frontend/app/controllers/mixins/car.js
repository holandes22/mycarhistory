import GEARBOX_TYPES from 'appkit/definitions/gearbox-types';
import YEAR_LIST from 'appkit/definitions/year-list';

var CarControllerMixin = Ember.Mixin.create({
    gearboxTypes: [
        {type: GEARBOX_TYPES.manual.type, label: GEARBOX_TYPES.manual.label},
        {type: GEARBOX_TYPES.automatic.type, label: GEARBOX_TYPES.automatic.label},
    ],
    years: YEAR_LIST
});

export default CarControllerMixin;
