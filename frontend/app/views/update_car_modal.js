export default Ember.View.extend({
    id: 'updateCarModal',
    templateName: "modal",
    title: "Update Car",
    bodyTemplate: "car/AddUpdate",
    actionHandler: "updateCar",
    actionName: "Update",
});


