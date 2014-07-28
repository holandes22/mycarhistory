import Ember from 'ember';
import TREATMENT_CATEGORIES from 'app-kit/definitions/treatment-categories';
import TREATMENT_REASONS from 'app-kit/definitions/treatment-reasons';
import getTypeLabelMap from 'app-kit/utils/get-type-label-map';


var TreatmentControllerMixin = Ember.Mixin.create({
    treatmentCategories: getTypeLabelMap(TREATMENT_CATEGORIES),
    treatmentReasons: getTypeLabelMap(TREATMENT_REASONS),
});

export default TreatmentControllerMixin;
