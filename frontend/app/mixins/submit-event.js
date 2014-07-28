import Ember from 'ember';

export default Ember.Mixin.create({
    actions: {
        submit: function() {
            this.sendAction('submitAction', this.get('actionParam'));
        }
    }
});
