import TREATMENT_CATEGORIES from 'appkit/definitions/treatment-categories';
import TREATMENT_REASONS from 'appkit/definitions/treatment-reasons';
import getTypeLabelMap from 'appkit/utils/get-type-label-map';


var TreatmentControllerMixin = Ember.Mixin.create({
    treatmentCategories: getTypeLabelMap(TREATMENT_CATEGORIES),
    treatmentReasons: getTypeLabelMap(TREATMENT_REASONS),
});

export default TreatmentControllerMixin;
