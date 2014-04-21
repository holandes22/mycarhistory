import GEARBOX_TYPES from 'appkit/definitions/gearbox-types';
import YEAR_LIST from 'appkit/definitions/year-list';
import getTypeLabelMap from 'appkit/utils/get-type-label-map';


var CarControllerMixin = Ember.Mixin.create({
    gearboxTypes: getTypeLabelMap(GEARBOX_TYPES),
    years: YEAR_LIST
});

export default CarControllerMixin;
