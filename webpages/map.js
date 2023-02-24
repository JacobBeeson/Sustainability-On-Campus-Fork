


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

    if (X_coordinate > 100) {X_coordinate = 100}
    else if (X_coordinate < 0 ) {X_coordinate = 0}
    if (Y_coordinate > 100) {Y_coordinate = 100}
    else if (Y_coordinate < 0) {Y_coordinate = 0}

    var x = document.getElementById("pet-pos");
    x.style.bottom = Y_coordinate +  "%";
    x.style.left = X_coordinate + "%";
    
}

/* left = 
50.737611, -3.540081

bottom  = 
50.730797, -3.525755

right = 
50.734776, -3.524366

top = 
50.741890, -3.527762

50.741890 - 50.730797 = 0.011093


-3.524366 - -3.540081 = 0.015715




50.740300, -3.529748


50.735953, -3.525891

((position.coords.latitude-50.730797)/0.011093)*100 
((position.coords.longitude + 3.540081)/0.015715)*100 */

