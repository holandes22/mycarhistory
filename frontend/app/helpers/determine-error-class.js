export default Ember.Handlebars.makeBoundHelper(function(error) {
    return (error.status === 404) ? 'info' : 'danger';
});

