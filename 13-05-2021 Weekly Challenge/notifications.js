Notification.requestPermission(function() {
    if (Notification.permission === 'granted') {

    } else if (Notification.permission === 'denied') {

    } else {
    }
});