import GEARBOX_TYPES from 'app-kit/definitions/gearbox-types';
import YEAR_LIST from 'app-kit/definitions/year-list';
import getTypeLabelMap from 'app-kit/utils/get-type-label-map';


var CarControllerMixin = Ember.Mixin.create({
    gearboxTypes: getTypeLabelMap(GEARBOX_TYPES),
    years: YEAR_LIST
});

export default CarControllerMixin;
