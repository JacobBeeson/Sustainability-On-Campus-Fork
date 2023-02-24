


function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    }  else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position) {
    /* works out what perecentage from the bottom and the left the user is */
    var Y_coordinate =  Math.round(((position.coords.latitude - 50.726705)/0.015542)*100 )  
    var X_coordinate =  Math.round(((position.coords.longitude + 3.546502)/0.022987)*100 )  

    var x = document.getElementById("pet-pos");
    x.style.bottom = Y_coordinate +  "%";
    x.style.left = X_coordinate + "%";
    
}

/* top left = 
lat 50.742247, long -3.546502

bottom of page = 
50.726705, -3.543878

far right of page = 
50.736281, -3.523515

bottom right = 
50.726705 -3.523515

50.742247-50.726705 = 0.015542


-3.523515 - -3.546502 = 0.022987

((lat-50.726705)/0.015542)*100 
((long + 3.546502)/0.022987)*100 */

