


function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    }  else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position) {
    /* works out what perecentage from the bottom and the left the user is */
    var Y_coordinate =  Math.round(((position.coords.latitude-50.731797)/0.011093)*100 )  
    var X_coordinate =  Math.round(((position.coords.longitude + 3.540081)/0.015715)*100 )  

    /* checks if outside bounds of map */ 
    if (X_coordinate > 95) {X_coordinate = 95}
    else if (X_coordinate < 5 ) {X_coordinate = 5}
    if (Y_coordinate > 95) {Y_coordinate = 95}
    else if (Y_coordinate < 5) {Y_coordinate = 5}

    /*changes pet position on map */
    var x = document.getElementById("pet-pos");
    x.style.bottom = Y_coordinate +  "%";
    x.style.left = X_coordinate + "%";
    
}


