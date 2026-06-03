// ELEMENTS SELECT=================

const startBtn = document.getElementById("startBtn");

const text = document.getElementById("text");

const timeText = document.getElementById("timeText");

const wpmText = document.getElementById("wpmText");

const errorText = document.getElementById("errorText");

const accuracyText = document.getElementById("accuracyText");

const refreshBtn = document.getElementById("refreshBtn");

const reviewBtn = document.getElementById("reviewBtn");

const howToPlay = document.getElementById("howToPlay");

const saveBtn = document.getElementById("saveBtn");

const inputBtn = document.getElementById("inputBtn");

const popup = document.getElementById("popup");

const openTimer = document.getElementById("openTimer");

const showTimer = document.getElementById("showTimer");


// VARIABLES=============

//accuracy 
let accuracy=0;

//wrong letters
let errors = 0;

//correct letters
let correct = 0;

//typed letters
let typedChars = 0;

// typing start time
let startTime;

let gameStart = false;

let index = 0;

let timer;

let time = parseInt(timeText.innerText);

// PARAGRAPH SETUP================

const para = `Technology has changed the way people learn, communicate, and work in everyday life. Typing is now an important skill for students, developers, writers, and office workers around the world. Improving typing speed requires regular practice, focus, and patience. A good typing habit can help reduce mistakes and increase productivity while working on computers. Many people start slowly, but with consistent effort they become faster and more accurate over time. In coding carrer typing is very the important part because of speed  keep learning`;
text.innerHTML = "";

para.split("").forEach(function (char) {
  text.innerHTML += `<span class="text-gray-500">${char}</span>`;
});

// ALL SPANS===================

const span = text.querySelectorAll("span");

// FIRST CURSOR=================

span[index].classList.add("border-b-2", "border-yellow-400");


// OPEN POPUP LOGIC ================
openTimer.addEventListener("click", function () {

  popup.classList.remove("hidden");

});


// SAVE TIMER
saveBtn.addEventListener("click", function () {

  let customTime = parseInt(inputBtn.value);

  // invalid value check
  if (customTime <= 0 || isNaN(customTime)) {
    alert("Enter valid seconds");
    return;
  }

  // update timer
  time = customTime;

  // show on screen
  timeText.innerText = time + "s";

  // close popup
  popup.classList.add("hidden");

});


//SHOW TIMER LOGIC=========

showTimer.addEventListener("click",function(){
  showTimer.innerText=timeText.innerText;
 

})


// START BUTTON LOGIC==========

startBtn.addEventListener("click", function () {
  gameStart = true;

  //save start time
  startTime = new Date().getTime();

  startBtn.style.display = "none";

  // TIMER START=============

  timer = setInterval(function () {
    time--;

    timeText.innerText = time + "s";

    // time over

    if (time <= 0) {
      clearInterval(timer);

      gameStart = false;
    }
  }, 1000);
});

// TYPING EVENT=========

document.addEventListener("keydown", function (e) {
  // game start check
  if (gameStart === false) {
    return;
  }

  // ignore special keys

  if (
    e.key === "Shift" ||
    e.key === "Ctrl" ||
    e.key === "Alt" ||
    e.key === "Tab" ||
    e.key === "CapsLock" ||
    e.key === "Control"
  ) {
    return;
  }

  // stop page scroll on space

  if (e.key === " ") {
    e.preventDefault();
  }

  // stop when complete

  if (index >= span.length) {
    clearInterval(timer);

    return;
  }

  //BACKSPACE LOGIC ===============
  if (e.key === "Backspace") {
    if (index > 0) {
      // remove old cursor
      span[index].classList.remove("border-b-2", "border-yellow-400");

      // move back
      index--;

     typedChars--;


      // check wrong letter
      if (span[index].classList.contains("text-red-500")) {
        errors--;

        errorText.innerText = errors;
      }

      // reset color
      span[index].classList.remove("text-white", "text-red-500");

      // gray color
      span[index].classList.add("text-gray-500");

      // cursor back
      span[index].classList.add("border-b-2", "border-yellow-400");
    }

    return;
  }

  
typedChars++;


 
  // CORRECT / WRONG TYPING=======

  if (e.key === span[index].innerText) {
    //increase correct letters
    correct++;

    span[index].classList.remove("text-gray-500");

    span[index].classList.add("text-white");
  } else {
    // wrong
    errors++;

    //show errors box update
    errorText.innerText = errors;

    span[index].classList.remove("text-gray-500");

    span[index].classList.add("text-red-500");
  }

  // remove old cursor

  span[index].classList.remove("border-b-2", "border-yellow-400");

  // next letter

  index++;

  // next cursor

  if (index < span.length) {
    span[index].classList.add("border-b-2", "border-yellow-400");
  }

  //WPM LOGIC=================

  let correctTime = new Date().getTime();

  //total time in minutes
  let minutes = (correctTime - startTime) / 1000 / 60;

  //total words
  let words = correct / 5;

  //final wpm
  let finalWpm = Math.round(words / minutes);

  //avoid infinity
  if (minutes > 0) {
    wpmText.innerText = finalWpm;
  }


  //ACCURACY LOGIC===================
  accuracy = Math.round((correct/typedChars)*100);

  //avoid NaN
  if(typedChars > 0){

    accuracyText.innerText= accuracy + "%";
  }

});

//REFRESH BUTTON LOGIC==================
  refreshBtn.addEventListener("click", function(){
    location.reload();
  });

  //REVIEW BUTTON LOGIC====================
  reviewBtn.addEventListener("click",function(){
    window.location.href="/review";
  })

 