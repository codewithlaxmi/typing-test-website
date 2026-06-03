
const words=[
    "dream",
    "simple",
    "confident",
    "color",
    "game",
    "you",
    "are",
    "beautifull",
    "sweet",
    "cute",
    "handsome",
    "winner",
    "happy",
    "coding",
    "speed",
    "future",
    "believe",
    "focus",
    "success",
    
]

const gameOverScreen = document.getElementById("game-over-screen");

const finalScoreText= document.getElementById("final-score");

const restartBtn = document.getElementById("restart-btn");

const gameArea = document.getElementById("game-area");

const input = document.getElementById("input");

const scoreBox = document.getElementById("score");

const missedBox = document.getElementById("missed");

const timerBox = document.getElementById("timer");

let score = 0;

let missed = 0;

let isgameOver= false;

const lanes =["35%","50%","65%"];

let gameInterval = setInterval(createWord,1000);

//CREATE WORD==============
function createWord(){

    if(isgameOver) return;  

    const word = words[Math.floor(Math.random()* words.length)];

    const wordDiv = document.createElement("div");

    wordDiv.classList.add("word");
    
    wordDiv.innerText = word;

    //random lane   

    const lane = lanes[Math.floor(Math.random()*lanes.length)];

    wordDiv.style.left= lane;

    gameArea.appendChild(wordDiv);

    //END LOGIC==============

    wordDiv.addEventListener("animationend",()=>{

        if (gameArea.contains(wordDiv)){

            wordDiv.remove();
            
            missed++;

            missedBox.innerText=missed+"/5";

            
            //GAME OVER=================

            if(missed >=5){

                isgameOver=true;
                
                gameOverScreen.style.display="flex";

                //show score

                finalScoreText.innerText = score;

                clearInterval(gameInterval);

                ///old words remove
                const remainingWords = document.querySelectorAll(".word");

                remainingWords.forEach(w => w.remove());

               
                restartBtn.addEventListener("click",()=>{
                    location.reload();
                })
            }
        }
    });
}



//USER TYPING=======


 input.addEventListener("input", () => {

    if(isgameOver) return; 

    const typed =
        input.value.trim().toLowerCase();

    const allWords =
        document.querySelectorAll(".word");

    let matched = false;

    allWords.forEach(word => {

        const currentWord =
            word.innerText.toLowerCase();

        // FULL MATCH
        if(currentWord === typed){

            word.remove();

            score += 10;

            scoreBox.innerText = score;

            input.value = "";

            matched = true;
        }

        // PARTIAL MATCH
        else if(currentWord.startsWith(typed)){

            matched = true;
        }
    });

    // WRONG LETTER
    if(!matched){

        input.value = "";
    }
});

//AUTO FOCUS INPUT
document.addEventListener("click",()=>{
    input.focus();

});

input.focus();



/// LETTER FALL JS LOGIC ===========================================================================

const letterGameStart = document.getElementById("lettergame-start");

const startBtn = document.getElementById("start-btn");

let letterStart = false;


window.addEventListener("load",()=>{
    letterGameStart.style.display="flex";

});

startBtn.addEventListener("click", () => {
  letterStart = true;

  letterGameStart.style.display = "none";
});




