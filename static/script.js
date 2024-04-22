function createMap(center, zoom) {
    let map = L.map('map').setView(center, zoom);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);
    return map
}

function updateMarkers(markerFeatureGroup) {
    fetch("http://127.0.0.1:8000/map2/vehicle-positions/")
      .then(response => response.json())
      .then(data => {
        let prevLatLons = [];

        markerFeatureGroup.eachLayer(layer =>
          layer.hasOwnProperty('_latlng') && prevLatLons.push(layer._latlng)
        );

        markerFeatureGroup.clearLayers();

        data.vehicles.forEach((vehicle, idx) => {
          let prevLatLon = idx < prevLatLons.length ? [prevLatLons[idx].lat, prevLatLons[idx].lng] : null;
          let newLatLon = [vehicle.latitude, vehicle.longitude];

          L.marker(newLatLon).addTo(markerFeatureGroup);

          if (prevLatLon) {
            L.polyline([prevLatLon, newLatLon]).addTo(markerFeatureGroup);
          }
        });
      });
  }