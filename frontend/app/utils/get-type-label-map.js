export default function(obj) {
    var types = [];
    for (var key in obj) {
        types.push({type: obj[key].type, label: obj[key].label});
    }
    return types;
}
