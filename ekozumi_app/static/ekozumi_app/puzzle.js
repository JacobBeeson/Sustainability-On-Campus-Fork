/** Puzzle logic, for puzzle.html
 *  The puzzle is an anagram decided by the game keeper, if the player gets it correct
 *  they will be given a location hint, where a monster will be located
 * 
 *  Author: Elliot Wride, Christian Wood
 */

var anagram;
function startTime(){
    /* - Logic for the timer that is displayed at the top of the webpage
     * - Shows a countdown until the next puzzle will be displayed
     */
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
    /* - Shuffles the anagram for the day, which is decided by the game keeper
     * - Anagram is inputted from django into puzzle.html to be used
     * - Shuffled anagram is displayed on puzzle.html
     */
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
    /* - Checks if the solution to the anagram entered in the form by the user is correct
     * - If correct the hint is displayed
     */
    answer = (document.f1.nw.value).toUpperCase(); //to ignore case of letters

    if (answer == anagram.toUpperCase()){
        document.getElementById('hint').innerHTML="Hint: " + hint;
    }
}
