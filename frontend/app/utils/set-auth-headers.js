import DS from "ember-data";

export default function() {
    var token = window.sessionStorage.getItem('loggedInUserToken');
    DS.RESTAdapter.reopen({
        headers: { 'Authorization': 'Token ' + token }
    });

}
