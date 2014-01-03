export default Ember.View.extend({
    id: 'updateCarModal',
    templateName: 'modal',
    title: 'Update Car',
    bodyTemplate: 'car/AddUpdate',
    buttonTemplate: 'car/UpdateButton',
    actionName: 'Update'
});


