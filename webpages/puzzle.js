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
    t=setTimeout('startTime()',500);
    
    
    if(true){//change to check if time and if puzzle done
        document.getElementById('puzzle').style.display = 'block';
    }else{
        document.getElementById('puzzle').style.display = 'none';
    }
}

function puzzle(){
    anagrams = ["RECYCLE"];
    anagram = anagrams[0]; //to be decided by date maybe linked list struct
    letters = [];
    for(var i = 0; i<anagram.length; i++){
        letters[i]=anagram.charAt(i);
    }
    letters.sort(function() {return 0.5 - Math.random()});
    
    jumble="";
    for(var i = 0; i<anagram.length; i++){
        jumble += letters[i];
    }
    document.getElementById('anagram').innerHTML = jumble;
    startTime();
}

function checkTime(i)
{
    if (i<10)
        {
            i="0" + i;
        }
    return i;
}

function checkSolve(){
    answer = (document.f1.nw.value).toUpperCase();

    if (answer == anagram){
        alert("You did it!")
        document.getElementById('hint').innerHTML="i am the hint";
    }
}