module.exports = function(server) {

    server.namespace('/api', function() {

        server.post('/cars', function(req, res) {
            var car = {
                amount_of_owners: 2,
                brand: "2",
                gearbox_type: 1,
                id: 35,
                model: "2",
                treatments: [],
                user: 3,
                year: 2013
            };
            res.send(car);
        });
        server.get('/cars', function(req, res) {
            var cars = [
                {
                    amount_of_owners: 2,
                    brand: "1",
                    gearbox_type: 1,
                    id: 1,
                    model: "1",
                    treatments: [],
                    user: 3,
                    year: 2013
                },
                {
                    amount_of_owners: 2,
                    brand: "2",
                    gearbox_type: 1,
                    id: 2,
                    model: "2",
                    treatments: [],
                    user: 3,
                    year: 2013
                }
            ];
            res.send(cars);

        });
    });
};
