var handlers = {};
window.navigator.id = {
    watch: function(obj) { handlers = obj; },
    request: function() { handlers.onlogin("faux-assertion"); },
    logout: function() { handlers.onlogout(); }
};
