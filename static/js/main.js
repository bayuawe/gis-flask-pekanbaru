// static/js/main.js
var map = L.map("map").setView([0.507, 101.447], 13);

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: "© OpenStreetMap contributors",
}).addTo(map);

// Contoh marker untuk coffee shop
var coffeeShops = [
    {
        name: "Coffee House 1",
        location: [0.507, 101.448],
        address: "Jl. Coffee Street 1, Pekanbaru",
    },
    {
        name: "Espresso Haven",
        location: [0.509, 101.446],
        address: "Jl. Espresso Avenue 2, Pekanbaru",
    },
    {
        name: "Java Dreams",
        location: [0.505, 101.445],
        address: "Jl. Java Lane 3, Pekanbaru",
    },
];

coffeeShops.forEach(function (shop) {
    L.marker(shop.location)
        .bindPopup("<b>" + shop.name + "</b><br>" + "Address: " + shop.address)
        .addTo(map);
});
