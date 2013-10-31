jQuery( document ).ready(function( $ ) {

  jQuery(document).ajaxSend(function(event, xhr, settings) {
    if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
      if ( typeof CURRENT_USER_AUTH_TOKEN != 'undefined'){
        var token = 'Token ' + CURRENT_USER_AUTH_TOKEN;
        xhr.setRequestHeader("Authorization", token);
      }
    }
  });
});

MyCarHistory = Ember.Application.create({
  rootElement: '#emberRoot'
});

