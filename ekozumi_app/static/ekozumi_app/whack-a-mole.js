/** Whack a mole fight script
 * 
 *  Author: Jacob Beeson
 */

const cursor = document.querySelector('.cursor')
const holes = [...document.querySelectorAll('.holes')]

const health1 = document.querySelector('.health span')
let health = 100

const whack = new Audio("../../static/Sounds/whack.mp3")
const music = new Audio("../../static/Sounds/background-tune.mp3")

var seconds = 60;

function startTimer() {
  /* Starts the timer once user has clicked start game.
   * Once time runs out they are redirected to the home page
   */
  var countdown = setInterval(function() {
    seconds--;
    document.getElementById("seconds").textContent = pad(seconds);
    if (seconds == 0) {
      clearInterval(countdown);
      window.location = "../lose"
    }
  }, 1000);
}

function pad(num) {
  return ("0" + num).slice(-2);
}
//game code
function run(){
    /* Main driver for the whack a mole game,
     * accesses whack-a-mole.html and moves the mole around
     * the screen, when a user hits a mole the health goes down
     */
    //music 
    //gets the index of a random hole 
    const i = Math.floor(Math.random() * holes.length)
    const hole = holes[i]
    const img = document.createElement('img')
    //adds the image of 'mole' to the 
    img.classList.add('mole')
    // make variable
    img.src = moleImage

    img.addEventListener('click', () => {
        health -= 10
        whack.play()
        img.src = whackedMoleImage
        health1.textContent = health
        if(health!=0){
            clearTimeout(timer)
            setTimeout(() => {
                hole.removeChild(img)
                run()
            }, 500)
        }else{
            hole.removeChild(img)
            sendDataToDjango(seconds);
            window.location = "../fight_outro";
        }
    })

    hole.appendChild(img)

    timer = setTimeout(() => {
        hole.removeChild(img)
        run()
    }, 800)
}
// Event listeners, for when player is using the mouse
window.addEventListener('mousemove', e =>{
    cursor.style.top = e.pageY + 'px'
    cursor.style.left = e.pageX + 'px'
})

window.addEventListener('mousedown', () => {
    cursor.classList.add('active')
})

window.addEventListener('mouseup', () => {
    cursor.classList.remove('active')
})  

function startGame(i1,i2){
    /** Launches the whack-a-mole game
     */
    moleImage = i1
    whackedMoleImage = i2
    music.volume = 0.2;
    music.play()
    var elem = document.getElementById("startButton");
    elem.parentNode.removeChild(elem);
    startTimer()
    run();
}

function sendDataToDjango(seconds) {
    console.log("Data sending");
    $.ajax({
        type: 'POST',
        url: '../upload_monster_data/',
        data: {
            'score': seconds,
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