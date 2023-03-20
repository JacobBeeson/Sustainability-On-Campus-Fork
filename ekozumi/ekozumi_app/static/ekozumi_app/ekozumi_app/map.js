/** Map logic for map.html
 * 
 *  Author: Lucas Enefer, Christian Wood
 */

function getLocation(){
    document.getElementById('battleButton').style.visibility = 'hidden';
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    }  else {
        var text = document.getElementById("location");
        text.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position){
    /* works out what perecentage from the bottom and the left the user is */
    var x_coordinate =  Math.round(((position.coords.longitude + 3.540081)/0.015715)*100)
    var y_coordinate =  Math.round(((position.coords.latitude-50.731797)/0.011093)*100)

    /* checks if outside bounds of map */ 
    if (x_coordinate > 95) {x_coordinate = 95}
    else if (x_coordinate < 5 ) {x_coordinate = 5}
    if (y_coordinate > 95) {y_coordinate = 95}
    else if (y_coordinate < 0) {y_coordinate = -5}

    /*changes pet position on map */
    var x = document.getElementById("pet-pos");
    x.style.bottom = y_coordinate +  "%";
    x.style.left = x_coordinate + "%";

    min_x = ((minLongitude + 3.540081)/0.015715)*100;
    max_x = ((maxLongitude + 3.540081)/0.015715)*100;
    min_y = ((minLatitude - 50.731797)/0.011093)*100;
    max_y = ((maxLatitude - 50.731797)/0.011093)*100;

    /*checks if Boss in area */
    if (x_coordinate>= min_x && x_coordinate <= max_x && y_coordinate>= min_y && y_coordinate<= max_y){
        var text = document.getElementById("location");
        /* Message based upon if enemy has been defeated for this day */
        if (notFedToday)
        {
            text.innerHTML = "looks like there is something here!";
        }
        else
        {
            text.innerHTML = "You have already defeated this boss!";
        }
        document.getElementById('battleButton').style.visibility = 'visible' ;
    }
}
