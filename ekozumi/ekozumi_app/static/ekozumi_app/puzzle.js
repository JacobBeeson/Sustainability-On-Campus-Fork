/** Puzzle logic, for puzzle.html
 * 
 *  Author: Elliot Wride, Christian Wood
 */

var anagram;
function startTime(){
    var midnight = new Date();
    midnight.setHours( 24 );
    midnight.setMinutes( 0 );
    midnight.setSeconds( 0 );
    midnight.setMilliseconds( 0 );

    var h=Math.floor((midnight.getTime() - new Date().getTime())/(1000*60*60))
    var m=checkTime(Math.floor((midnight.getTime() - new Date().getTime())%(1000*60*60)/(1000*60)));
    var s=checkTime(Math.floor((midnight.getTime() - new Date().getTime())%(1000*60)/(1000)));
    document.getElementById('txt').innerHTML="Daily challenge released in " + h+":"+m+":"+s;
    //updates clock with current time
    t=setTimeout('startTime()',500);
    //timer until time updates again, 500ms keeps time accurate but doesnt call method too often
    document.getElementById('puzzle').style.display = 'block';
}

function puzzle(){
    letters = [];
    for(var i = 0; i<anagram.length; i++){
        letters[i]=anagram.charAt(i);
    }
    letters.sort(function() {return 0.5 - Math.random()});//randomly shuffles array
    
    jumble="";
    for(var i = 0; i<anagram.length; i++){
        jumble += letters[i];
    }//coverts to string
    document.getElementById('anagram').innerHTML = jumble;
    startTime();
}

function checkTime(i){
    //formats single digits
    if (i<10){
            i="0" + i;
        }
    return i;
}

function checkSolve(){
    answer = (document.f1.nw.value).toUpperCase(); //to ignore case of letters

    if (answer == anagram.toUpperCase()){
        document.getElementById('hint').innerHTML="Hint: " + hint;
    }
}
