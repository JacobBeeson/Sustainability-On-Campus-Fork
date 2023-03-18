var score = 0;
var round = 1;
var attempts = 0;

function loadQuiz(){
    // sets colour back to defualt 
    document.getElementById("box-header").style.backgroundColor = "#665851"

    //checks which round it is and displays appropriate questions and answers 
    switch(round){
        case 1:
            document.getElementById('Question').innerHTML = Q1;
            // randomly generates which pos correct answer is in 
            Q1Correct = Math.floor(Math.random() * 3)+1;
            switch(Q1Correct){
                case 1:
                    document.getElementById('A1-label').innerHTML = Q1A1;
                    document.getElementById('A2-label').innerHTML = Q1A2;
                    document.getElementById('A3-label').innerHTML = Q1A3;
                    document.getElementById('A4-label').innerHTML = Q1A4;
                    break;
                case 2:
                    document.getElementById('A1-label').innerHTML = Q1A2;
                    document.getElementById('A2-label').innerHTML = Q1A1;
                    document.getElementById('A3-label').innerHTML = Q1A3;
                    document.getElementById('A4-label').innerHTML = Q1A4;
                    break;
                case 3:
                    document.getElementById('A1-label').innerHTML = Q1A3;
                    document.getElementById('A2-label').innerHTML = Q1A2;
                    document.getElementById('A3-label').innerHTML = Q1A1;
                    document.getElementById('A4-label').innerHTML = Q1A4;
                    break;
                case 4:
                    document.getElementById('A1-label').innerHTML = Q1A4;
                    document.getElementById('A2-label').innerHTML = Q1A2;
                    document.getElementById('A3-label').innerHTML = Q1A3;
                    document.getElementById('A4-label').innerHTML = Q1A1;
                    break;
            }
            break;
        case 2:
            document.getElementById('Question').innerHTML = Q2;
            Q2Correct = Math.floor(Math.random() * 3)+1;
            switch(Q2Correct){
                case 1:
                    document.getElementById('A1-label').innerHTML = Q2A1;
                    document.getElementById('A2-label').innerHTML = Q2A2;
                    document.getElementById('A3-label').innerHTML = Q2A3;
                    document.getElementById('A4-label').innerHTML = Q2A4;
                    break;
                case 2:
                    document.getElementById('A1-label').innerHTML = Q2A2;
                    document.getElementById('A2-label').innerHTML = Q2A1;
                    document.getElementById('A3-label').innerHTML = Q2A3;
                    document.getElementById('A4-label').innerHTML = Q2A4;
                    break;
                case 3:
                    document.getElementById('A1-label').innerHTML = Q2A3;
                    document.getElementById('A2-label').innerHTML = Q2A2;
                    document.getElementById('A3-label').innerHTML = Q2A1;
                    document.getElementById('A4-label').innerHTML = Q2A4;
                    break;
                case 4:
                    document.getElementById('A1-label').innerHTML = Q2A4;
                    document.getElementById('A2-label').innerHTML = Q2A2;
                    document.getElementById('A3-label').innerHTML = Q2A3;
                    document.getElementById('A4-label').innerHTML = Q2A1;
                    break;
            }
            break;
        case 3:
            document.getElementById('Question').innerHTML = Q3;
            Q3Correct = Math.floor(Math.random() * 3)+1;
            switch(Q3Correct){
                case 1:
                    document.getElementById('A1-label').innerHTML = Q3A1;
                    document.getElementById('A2-label').innerHTML = Q3A2;
                    document.getElementById('A3-label').innerHTML = Q3A3;
                    document.getElementById('A4-label').innerHTML = Q3A4;
                    break;
                case 2:
                    document.getElementById('A1-label').innerHTML = Q3A2;
                    document.getElementById('A2-label').innerHTML = Q3A1;
                    document.getElementById('A3-label').innerHTML = Q3A3;
                    document.getElementById('A4-label').innerHTML = Q3A4;
                    break;
                case 3:
                    document.getElementById('A1-label').innerHTML = Q3A3;
                    document.getElementById('A2-label').innerHTML = Q3A2;
                    document.getElementById('A3-label').innerHTML = Q3A1;
                    document.getElementById('A4-label').innerHTML = Q3A4;
                    break;
                case 4:
                    document.getElementById('A1-label').innerHTML = Q3A4;
                    document.getElementById('A2-label').innerHTML = Q3A2;
                    document.getElementById('A3-label').innerHTML = Q3A3;
                    document.getElementById('A4-label').innerHTML = Q3A1;
                    break;
            }
            break;
        case 4:
            document.getElementById('Question').innerHTML = Q4;
            Q4Correct = Math.floor(Math.random() * 3)+1;
            switch(Q4Correct){
                case 1:
                    document.getElementById('A1-label').innerHTML = Q4A1;
                    document.getElementById('A2-label').innerHTML = Q4A2;
                    document.getElementById('A3-label').innerHTML = Q4A3;
                    document.getElementById('A4-label').innerHTML = Q4A4;
                    break;
                case 2:
                    document.getElementById('A1-label').innerHTML = Q4A2;
                    document.getElementById('A2-label').innerHTML = Q4A1;
                    document.getElementById('A3-label').innerHTML = Q4A3;
                    document.getElementById('A4-label').innerHTML = Q4A4;
                    break;
                case 3:
                    document.getElementById('A1-label').innerHTML = Q4A3;
                    document.getElementById('A2-label').innerHTML = Q4A2;
                    document.getElementById('A3-label').innerHTML = Q4A1;
                    document.getElementById('A4-label').innerHTML = Q4A4;
                    break;
                case 4:
                    document.getElementById('A1-label').innerHTML = Q4A4;
                    document.getElementById('A2-label').innerHTML = Q4A2;
                    document.getElementById('A3-label').innerHTML = Q4A3;
                    document.getElementById('A4-label').innerHTML = Q4A1;
                    break;
            }
            break;
        default:
            //save score to database 

            //hidea form and displaya nav bar 
            document.getElementById('Question').innerHTML = "ahh i can't beleive you defeated me!!!";
            document.getElementById('form').style.display = "none";
            document.getElementById("footer").style.display = "block"           
    }   
}

function getCheckedRadioValue() {
    // returns which value selected 
    var rads = document.getElementById('form'),
        i;
    for (i=0; i < rads.length; i++)
       if (rads[i].checked)
           return rads[i].value;
    return null; 
 }

function checkAnswer(){
    var checkedValue = getCheckedRadioValue();
    //checks if answer was selected 
    if (checkedValue == null){
        alert("please choose an answer");
    } else {
        attempts++
        //checks if answer is correct for round 
        switch(round){
            case 1:
                if (checkedValue==Q1Correct){
                    // changes header colour to green
                    document.getElementById("box-header").style.backgroundColor = "#33ff33"
                    //runs calulate score after 2 seconds 
                    setTimeout(calScore,2000); 
                } else {
                    document.getElementById("box-header").style.backgroundColor = "#ff0000"
                }
                break;
            case 2:
                if (checkedValue==Q2Correct){
                    // changes header colour to green
                    document.getElementById("box-header").style.backgroundColor = "#33ff33"
                    //runs calulate score after 2 seconds 
                    setTimeout(calScore,3000); 
                } else {
                    // changes header colour to red 
                    document.getElementById("box-header").style.backgroundColor = "#ff0000"
                }
                break;
            case 3:
                if (checkedValue==Q3Correct){
                    // changes header colour to green
                    document.getElementById("box-header").style.backgroundColor = "#33ff33"
                    //runs calulate score after 2 seconds 
                    setTimeout(calScore,3000); 
                } else {
                    // changes header colour to red
                    document.getElementById("box-header").style.backgroundColor = "#ff0000"
                }
                break;
             case 4:
                if (checkedValue==Q4Correct){
                    // changes header colour to green
                    document.getElementById("box-header").style.backgroundColor = "#33ff33"
                    //runs calulate score after 2 seconds 
                    setTimeout(calScore,3000); 
                } else {
                    // changes header colour to red
                    document.getElementById("box-header").style.backgroundColor = "#ff0000"
                }
                break;
        }
    }
}

function calScore(attempts){
    // gives appropriate points based on number of attempts 
    switch(attempts){
        case 1:
            score += 10;
            break;
        case 2:
            score += 5;
            break;
        case 3:
            score += 2
            break;
    }
    // resets attempts and incriments round 
    attempts = 0
    round++
    loadQuiz();
}