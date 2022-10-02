function showEventInformation(latitude, longitude) {
    const infoDiv = document.getElementById('event-information');
    infoDiv.removeAttribute('hidden');

    const title = document.querySelector('#event-information h2');

    title.innerHTML = `A Single-Event Upset (SEU) occured here (${latitude}, ${longitude})`;
}

function hideEventInformation() {
    const infoDiv = document.getElementById('event-information');
    infoDiv.setAttribute('hidden', true);
}