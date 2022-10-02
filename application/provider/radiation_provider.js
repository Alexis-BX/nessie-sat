let radiationCache = new Map();

async function getRadiationAt(latitude, longitude) {
    const providerUrl = `http://localhost:8308/radiations/${latitude}/${longitude}`;
    const response = await fetch(providerUrl);

    const measurements = await response.json();
    const averageMeasurement = measurements.map(m => m.value).reduce((m1, m2) => m1 + m2, 0) / measurements.length;

    return averageMeasurement;
}

async function getRadiations(area, latitudeStep, longitudeStep) {
    const latitudeStart = Math.min(area.topLeft.latitude, area.bottomRight.latitude);
    const latitudeStop = Math.max(area.topLeft.latitude, area.bottomRight.latitude);

    const longitudeStart = Math.min(area.topLeft.longitude, area.bottomRight.longitude);
    const longitudeStop = Math.max(area.topLeft.longitude, area.bottomRight.longitude);

    let radiationValues = [];

    for (let latitude = latitudeStart; latitude <= latitudeStop; latitude += latitudeStep) {
        for (let longitude = longitudeStart; longitude <= longitudeStop; longitude += longitudeStep) {
            radiationValues.push({
                latitude,
                longitude,
                value: await _getRadiationCached(latitude, longitude)
            });
        }
    }

    return radiationValues;
}

async function _getRadiationCached(latitude, longitude) {
    const key = { latitude, longitude };

    if (!radiationCache.has(key))
        radiationCache.set(key, await getRadiationAt(latitude, longitude));

    return radiationCache.get(key);
}