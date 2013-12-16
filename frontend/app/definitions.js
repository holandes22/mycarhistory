function getYearList(){
    var currentYear = window.moment().year();
    var startingYear = 1920;
    var years = [];
    for (var i=currentYear; i >= startingYear; i--) {
        years.push(i);
    }
    return years;
}

var GEARBOX_TYPES = {
    1: 'Manual',
    2: 'Automatic'
};

var YEAR_LIST = getYearList();

export default YEAR_LIST;
export default GEARBOX_TYPES;
