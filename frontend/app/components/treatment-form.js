export default Ember.Component.extend({

    actions: {
        submit: function() {
            this.sendAction('submitAction', this.get('actionParam'));
        }
    }
});
