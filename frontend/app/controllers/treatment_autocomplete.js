var TreatmentAutocompleteController = Ember.Controller.extend({
    searchText: null,

    searchResults: function() {
        var searchText = this.get('searchText');
        if (!searchText) {
            return this.get('store').all('treatment');
        }
        return this.get('store').filter('treatment', function(record){
            return record.get('doneBy').match(searchText);
        });
    }.property('searchText')
});

export default TreatmentAutocompleteController;
