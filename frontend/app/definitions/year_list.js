var getYearList = function() {
    var currentYear = window.moment().year();
    var startingYear = 1920;
    var years = [];
    for (var i=currentYear; i >= startingYear; i--) {
        years.push(i);
    }
    return years;
};

var YEAR_LIST = getYearList();

export default YEAR_LIST;
