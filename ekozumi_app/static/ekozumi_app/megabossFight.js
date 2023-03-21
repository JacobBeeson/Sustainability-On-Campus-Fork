/** Megaboss logic for megabossFight.html
 * 
 *  Author: Lucas Enefer, Christian Wood
 */

var score = 0;
var round = 1;
var attempts = 1;
var seconds = 0;
var countdown

function loadQuiz(){
    /* - Displays the megaboss quiz on the fight page
     * - User will have to answer 4 quiz questions
     */
    var normalBoss=normalBoss;
    var angryBoss=angryBoss;
    // sets colour and boss back to default
    document.getElementById("box-header").style.backgroundColor = "#665851"

    //checks which round it is and displays appropriate questions and answers 
    switch(round){
        case 1:
            startTimer();
            document.getElementById('Question').innerHTML = Q1;
            // randomly generates which pos correct answer is in 
            Q1Correct = Math.floor(Math.random() * 4)+1;
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
            Q2Correct = Math.floor(Math.random() * 4)+1;
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
            Q3Correct = Math.floor(Math.random() * 4)+1;
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
            Q4Correct = Math.floor(Math.random() * 4)+1;
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
            console.log(score);
            console.log("calling send data")
            clearInterval(countdown);
            sendDataToDjango(score, seconds);
            //hidea form and displaya nav bar 
            document.getElementById('Question').innerHTML = outroText;
            document.getElementById('form').style.display = "none";
            document.getElementById("footer").style.display = "block"           
    }   
}

function getCheckedRadioValue() {
    /* Checks which check box the user selected for a quiz section
     */
    var rads = document.getElementById('form'),
        i;
    for (i=0; i < rads.length; i++)
       if (rads[i].checked)
           return rads[i].value;
    return null; 
 }

function checkAnswer(){
    /* When the user clicks the submit button, a check is performed to see
     * if the user got the correct answer
     */
    var checkedValue = getCheckedRadioValue();
    //checks if answer was selected 
    if (checkedValue == null){
        alert("please choose an answer");
    } else {
        //checks if answer is correct for round 
        switch(round){
            case 1:
                if (checkedValue==Q1Correct){
                    // changes header colour to green and boss to angry
                    document.getElementById("box-header").style.backgroundColor = "#33ff33"
                    document.getElementById("character").src = angryBoss; 
                    //runs calulate score after 1.5 seconds 
                    setTimeout(calScore,1500); 
                } else {
                    document.getElementById("box-header").style.backgroundColor = "#ff0000"
                    attempts++
                }
                break;
            case 2:
                if (checkedValue==Q2Correct){
                    // changes header colour to green and boss to angry
                    document.getElementById("box-header").style.backgroundColor = "#33ff33"
                    console.log(angryBoss);
                    document.getElementById("character").src = angryBoss; 
                    //runs calulate score after 1.5 seconds 
                    setTimeout(calScore,1500); 
                } else {
                    // changes header colour to red 
                    document.getElementById("box-header").style.backgroundColor = "#ff0000"
                    attempts++
                }
                break;
            case 3:
                if (checkedValue==Q3Correct){
                    // changes header colour to green and boss to angry
                    document.getElementById("box-header").style.backgroundColor = "#33ff33"
                    document.getElementById("character").src = angryBoss; 
                    //runs calulate score after 1.5 seconds 
                    setTimeout(calScore,1500); 
                } else {
                    // changes header colour to red
                    document.getElementById("box-header").style.backgroundColor = "#ff0000"
                    attempts++
                }
                break;
             case 4:
                if (checkedValue==Q4Correct){
                    // changes header colour to green and boss to angry 
                    document.getElementById("box-header").style.backgroundColor = "#33ff33"
                    document.getElementById("character").src = angryBoss; 
                    //runs calulate score after 1.5 seconds 
                    setTimeout(calScore,1500); 
                } else {
                    // changes header colour to red
                    document.getElementById("box-header").style.backgroundColor = "#ff0000"
                    attempts++
                }
                break;
        }
    }
}

function calScore(){
    /* Calculates how many points the user got
     */
    // gives appropriate points based on number of attempts 
    switch(attempts){
        case 1:
            score += 300;
            break;
        case 2:
            score += 200;
            break;
        case 3:
            score += 100;
            break;
    }
    // resets attempts and incriments round 
    document.getElementById("character").src = normalBoss;
    round++
    loadQuiz();
}

function startTimer() {
    countdown = setInterval(function() {
        seconds++;
    }, 1000);
}

function sendDataToDjango(score, seconds) {
    /* Uses JQuery to make a post request to django with the users score
     */
    console.log("Data sending");
    $.ajax({
        type: 'POST',
        url: '../upload_megaboss_data/',
        data: {
            'score' : score,
            'attempts' : attempts,
            'seconds' : seconds,
            'csrfmiddlewaretoken': csrf_token // include CSRF token in request
        },
        success: function(response) {
            console.log(response);
        },
        error: function(response) {
            console.log('Error:', response);
        }
    });
}
