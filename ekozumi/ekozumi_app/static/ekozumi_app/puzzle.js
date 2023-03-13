/** Puzzle logic, for puzzle.html
 * 
 *  Author: Elliot Wride, Christian Wood
 */

var anagram;
function startTime()
{
    var today=new Date();
    var h=today.getHours();
    var m=today.getMinutes();
    var s=today.getSeconds();
    // add a zero in front of numbers<10
    m=checkTime(m);
    s=checkTime(s);
    document.getElementById('txt').innerHTML=h+":"+m+":"+s;
    //updates clock with current time
    t=setTimeout('startTime()',500);
    //timer until time updates again, 500ms keeps time accurate but doesnt call method too often

    if(true){//change to check if time and if puzzle done - puzzle appears when display is set to block
        document.getElementById('puzzle').style.display = 'block';
    }else{
        document.getElementById('puzzle').style.display = 'none';
    }
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

function checkTime(i) 
{
    //formats single digits
    if (i<10)
        {
            i="0" + i;
        }
    return i;
}

function checkSolve(){
    answer = (document.f1.nw.value).toUpperCase(); //to ignore case of letters

    if (answer == anagram.toUpperCase()){
        alert("You did it!")
        document.getElementById('hint').innerHTML=hint;
    }
}
