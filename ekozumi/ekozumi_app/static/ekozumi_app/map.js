/** Map logic for map.html
 * 
 *  Author: Lucas Enefer
 */
function getLocation() {
    document.getElementById('battleButton').style.visibility = 'hidden';
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    }  else {
        var text = document.getElementById("location");
        text.innerHTML = "Geolocation is not supported by this browser.";
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
    else if (Y_coordinate < 0) {Y_coordinate = -5}

    /*changes pet position on map */
    var x = document.getElementById("pet-pos");
    x.style.bottom = Y_coordinate +  "%";
    x.style.left = X_coordinate + "%";

    /*demo boss*/
    min_X = 40;
    max_X = 50;
    min_Y = 45;
    max_Y = 75;

    /*checks if Boss in area */
    if (X_coordinate>= min_X && X_coordinate <= max_X && Y_coordinate>= min_Y && Y_coordinate<= max_Y){
        var text = document.getElementById("location");
        text.innerHTML = "looks like there is something here!";
        document.getElementById('battleButton').style.visibility = 'visible' ;
    }
}

/* duck pond: bottom=20-25% left=10-15% 
    east park bridge: bottom=55-60% left=65-70%
    exeter nature reserve: bottom=60-70% left=5-15%*/
