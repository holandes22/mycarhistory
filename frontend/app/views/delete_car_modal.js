export default Ember.View.extend({
    id: 'deleteCarModal',
    templateName: "modal",
    title: "Delete Car",
    bodyTemplate: "car/delete",
    actionHandler: "deleteCar",
    actionName: "Delete",
});


