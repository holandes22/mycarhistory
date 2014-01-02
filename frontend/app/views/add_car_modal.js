export default Ember.View.extend({
    id: 'addCarModal',
    templateName: "modal",
    title: "Add Car",
    bodyTemplate: "car/AddUpdate",
    actionHandler: "addCar",
    actionName: "Add",
});


