from flask import Flask, render_template 
import os 

app = Flask(__name__)


letterFallCards=[

    {
        "title":"Timer",
         "background":"bg-gradient-to-br from-pink-400 ",
        "icon":"fa-solid fa-clock",
        "boxicon":"fa-solid fa-clock",
        "boxiconColor":"text-cyan-400",
        "content":"Time remaining",
        "iconColor":"text-cyan-400"
        
        
    },
     {
        "title":"Missed",
         "background":"bg-gradient-to-br from-sky-600 ",
        "icon":"fa-solid fa-circle-xmark",
        "boxicon":"fa-solid fa-circle-xmark",
        "content":"Letters you missed",
        "iconColor":"text-red-550",
        "boxiconColor":"text-red-550",
        "class":"missedLetter"
    },
     {
        "title":"Score",
        "background":"bg-gradient-to-br from-blue-500 ",
        "icon":"fa-solid fa-star",
        "boxicon":"fa-solid fa-star",
        "content":"keep it up!",
        "iconColor":"text-yellow-300",
        "boxiconColor":"text-yellow-300",    
        "class":"scoreLetter"
    },
     {
        "title":"letters",
         "background":"bg-gradient-to-br from-pink-700 ",
        "icon":"fa-solid fa-a",
        "boxicon":"fa-solid fa-a",
        "content":"Current letters",
        "class":"currentLetter"
        
    },

]






























overviews=[
    {
        "title":"Word Script Game",
        "color":"text-sky-500",
        "content":"Words will fall from the top of the screen, and your task is to type the same word before it reaches the bottom. Type the correct word in the input box and press Enter to remove it from the screen. Each correct word increases your Score, while words that reach the bottom are counted as Missed. The Timer shows how long you survive in the game. Type fast, avoid mistakes, and try to get the highest score!",
        "link":"/wordScript",
        "button":"wordscript",
        "background":"bg-gradient-to-br from-black to-blue-800"
    },

     {
        "title":"Word Script Game",
        "color":"text-sky-500",
        "content":"Words will fall from the top of the screen, and your task is to type the same word before it reaches the bottom. Type the correct word in the input box and press Enter to remove it from the screen. Each correct word increases your Score, while words that reach the bottom are counted as Missed. The Timer shows how long you survive in the game. Type fast, avoid mistakes, and try to get the highest score!",
        "link":"/wordScript",
        "button":"wordscript",
        "background":"bg-gradient-to-br from-black to-blue-800"
     },

    {
        "title":"Word Script Game",
        "color":"text-sky-500",
        "content":"Words will fall from the top of the screen, and your task is to type the same word before it reaches the bottom. Type the correct word in the input box and press Enter to remove it from the screen. Each correct word increases your Score, while words that reach the bottom are counted as Missed. The Timer shows how long you survive in the game. Type fast, avoid mistakes, and try to get the highest score!",
        "link":"/wordScript",
        "button":"wordscript",
        "background":"bg-gradient-to-br from-black to-blue-800"
     },
      {
        "title":"game Script Game",
        "color":"text-sky-500",
        "content":"Words will fall from the top of the screen, and your task is to type the same word before it reaches the bottom. Type the correct word in the input box and press Enter to remove it from the screen. Each correct word increases your Score, while words that reach the bottom are counted as Missed. The Timer shows how long you survive in the game. Type fast, avoid mistakes, and try to get the highest score!",
        "link":"/wordScript",
        "button":"wordscript",
        "background":"bg-gradient-to-br from-black to-blue-800"
      },
      {
        "title":"game Script Game",
        "color":"text-sky-500",
        "content":"Words will fall from the top of the screen, and your task is to type the same word before it reaches the bottom. Type the correct word in the input box and press Enter to remove it from the screen. Each correct word increases your Score, while words that reach the bottom are counted as Missed. The Timer shows how long you survive in the game. Type fast, avoid mistakes, and try to get the highest score!",
        "link":"/wordScript",
        "button":"wordscript",
        "background":"bg-gradient-to-br from-black to-blue-800"
      },

      {
          "title":"game Script Game",
        "color":"text-sky-500",
        "content":"Words will fall from the top of the screen, and your task is to type the same word before it reaches the bottom. Type the correct word in the input box and press Enter to remove it from the screen. Each correct word increases your Score, while words that reach the bottom are counted as Missed. The Timer shows how long you survive in the game. Type fast, avoid mistakes, and try to get the highest score!",
        "link":"/wordScript",
        "button":"wordscript",
        "background":"bg-gradient-to-br from-black to-blue-800"

      },
      {
          "title":"game Script Game",
        "color":"text-sky-500",
        "content":"Words will fall from the top of the screen, and your task is to type the same word before it reaches the bottom. Type the correct word in the input box and press Enter to remove it from the screen. Each correct word increases your Score, while words that reach the bottom are counted as Missed. The Timer shows how long you survive in the game. Type fast, avoid mistakes, and try to get the highest score!",
        "link":"/wordScript",
        "button":"wordscript",
        "background":"bg-gradient-to-br from-black to-blue-800"
      },
      {
          "title":"game Script Game",
        "color":"text-sky-500",
        "content":"Words will fall from the top of the screen, and your task is to type the same word before it reaches the bottom. Type the correct word in the input box and press Enter to remove it from the screen. Each correct word increases your Score, while words that reach the bottom are counted as Missed. The Timer shows how long you survive in the game. Type fast, avoid mistakes, and try to get the highest score!",
        "link":"/wordScript",
        "button":"wordscript",
        "background":"bg-gradient-to-br from-black to-blue-800"
      },
      {
          "title":"game Script Game",
        "color":"text-sky-500",
        "content":"Words will fall from the top of the screen, and your task is to type the same word before it reaches the bottom. Type the correct word in the input box and press Enter to remove it from the screen. Each correct word increases your Score, while words that reach the bottom are counted as Missed. The Timer shows how long you survive in the game. Type fast, avoid mistakes, and try to get the highest score!",
        "link":"/wordScript",
        "button":"wordscript",
        "background":"bg-gradient-to-br from-black to-blue-800"
      },
      {
          "title":"game Script Game",
        "color":"text-sky-500",
        "content":"Words will fall from the top of the screen, and your task is to type the same word before it reaches the bottom. Type the correct word in the input box and press Enter to remove it from the screen. Each correct word increases your Score, while words that reach the bottom are counted as Missed. The Timer shows how long you survive in the game. Type fast, avoid mistakes, and try to get the highest score!",
        "link":"/wordScript",
        "button":"wordscript",
        "background":"bg-gradient-to-br from-black to-blue-800"
      },


]



































cards=[
    {
        
        "icon":"fa-solid fa-trophy",
        "iconbg":"text-yellow-400",
        "title":"Score",
        "number":"0",
        
    },
        {
        "icon": "fa-solid fa-heart-crack",
        "iconbg":"text-red-800",
        "title":"Missed",
        "number":"0/5",

        },

    {
        "icon":"fa-solid fa-clock",
        "title":"timer",
        "number":"1",
    
    },
    {
        "icon":" fa-solid fa-font",
        "title":"words",
        "number":0,
        
    }
    

]





tasks = [
    {
        "id":0,
        "content":"cat dog moon books pen boy water blue red big small mall pizza bill fill run walk sleep  good morning afternoon eat please sorry nice bad thanks  ",
        "title": "Basic words",
        "level": "Easy level",
        "textIcon": "ABC",
        "number": "01",
        "bg": "from-slate-900 to-slate-800",
        "levelColor": "bg-green-500/20 text-green-400"
    },

    {
        "id":1,
        "content":"i am happy you are nice this is book i like tea she is my friend he is very tall open the door i can run we are students  chose the window i am learning english what is your name my name is cute how are your i am fine    ",
        "title": "Easy sentences",
        "level": "Easy level",
        "icon": 'fa-solid fa-comment-dots',
        "number": "06",
        "bg": "from-slate-500/20 to-slate-800",
        "levelColor": "bg-green-500/20 text-green-400",
        "iconColor": "text-cyan-400"
    },

    {
        "id":2,
        "content":"beautiful wonderful dangerours comfortable intelligent interesting difficult amazing successful expensive delicious adventrues powerful important expensive delicious difficult motivation person communication resposibilties celebration knowledge opportunity creativity friendship conversation development  independence",
        "title": "Big words",
        "level": "Easy level",
        "icon": " fa-solid fa-book-open ",
        "number": "08",
        "bg": "from-slate-500/20 to-slate-800",
        "levelColor": "bg-green-500/20 text-green-400",
        "iconColor":"text-orange-400"
    },
    
    {
        "id":3,
        "content":"my best friend is very kind and funny we go to school together and play games after class she always helps me with homework and makes everyone smile i feel happy when we spend time together i like learning new things every day i practice english and japanese and read small stories in my free time sometimes i watch cartoons and listen to music learning slowly makes me feel confident and excited for the future",
        "title":"Paragraph",
        "level":"Easy level",
        "icon": "fa-solid fa-file-lines",
        "number":"04",
        "bg": "from-slate-900 to-slate-800",
        "levelColor":"bg-green-500/20 text-green-400",
        "iconColor":"text-pink-400"
    },

    {
        "id":4,
        "content":"the silent forest looked mysterious at night cold wind moved through the dark trees and strange sounds came from far away nobody wanted to walk there alone because the place felt deep and endless modern technology changes human life every single day people communicate across the world within seconds and students can learn difficult subjects from their homes knowledge grows quickly when curiosity and discipline work together",
        "title":"easy lines",
        "level":"Easy level",
        "icon":"fa-solid fa-file-lines",
        "number":"05" ,
       "bg": "from-slate-900 to-slate-800",
        "levelColor":"bg-green-500/20 text-green-400",
        "iconColor":"text-green-200"
           
   },

      {
        "id":5,
        "title":"Speed practice",
        "level":"Easy level",
        "icon":"fa-solid fa-gauge-high",
        "number":"06" ,
        "bg": "from-slate-900 to-slate-800",
        "levelColor":"bg-green-500/20 text-green-400",
        "iconColor":"text-sky-500"
           
   },

   {
       "title":"Number practice  ",
       "content":"12345645231526374849505493833635263u4848u7474438373648383",
       "level":"Medium",
       "textIcon":"123",
       "number":"07",
        "bg": "from-slate-900 to-slate-800",
       "levelColor":"bg-orange-500/20 text-orange-400",
       "textColor": "text-green-500"
   },

   {
        "title":"Accuracy",
        "level":"Medium",
         "levelColor": "bg-orange-500/20 text-orange-400",
        "icon": "fa-solid fa-bullseye ",
        "number": "08",
         "bg": "from-slate-900 to-slate-800",
        "levelColor":"bg-orange-300/20 text-orange-400",
        "iconColor":"text-red-400"

   },

   {
       "title":"Symbol Practice",
       "level":"Medium",
       "levelColor":"bg-orange-500/20 text-orange-400",
       "icon":"fa-solid fa-at",
       "number":"09",
       "bg": "from-slate-900 to-slate-800",
       "levelColor":"bg-orange-300/20 text-orange-400",
       "iconColor": "text-yellow-500"
   },

   {
       
       "title":"Capital Letters",
       "level":"Medium",
       "levelColor":"bg-orange-500/20 text-orange-400",
       "icon":"fa-solid fa-arrow-up-a-z",
       "number":"09",
       "bg": "from-slate-900 to-slate-800",
       "levelColor":"bg-orange-300/20 text-orange-400",
       "iconColor": "text-lime-100"
      
   },

   {
        "title":"Quick Fingers",
       "level":"Medium",
       "levelColor":"bg-orange-500/20 text-orange-400",
       "icon":"fa-solid fa-hand-sparkles",
       "number":"09",
       "bg": "from-slate-900 to-slate-800",
       "levelColor":"bg-orange-300/20 text-orange-400",
       "iconColor": "text-fuchsia-200"
       
   },

    {
        "title":"Reaction Test",
       "level":"Medium",
       "levelColor":"bg-orange-500/20 text-orange-400",
       "icon":"fa-solid fa-stopwatch",
       "number":"09",
       "bg": "from-slate-900 to-slate-800",
       "levelColor":"bg-orange-300/20 text-orange-400",
       "iconColor": "text-cyan-300"
    },

    {
        "title":"Speed Burst",
       "level":"Challenge",
       "icon":"fa-solid fa-rocket",
       "number":"09",
       "bg": "from-slate-900 to-slate-800",
       "levelColor":"bg-sky-500/20 text-sky-400",
       "iconColor": "text-orange-300"
    },
    {
        "title":"Blind Typing",
       "level":"challenge",
       "icon":"fa-solid fa-eye-slash",
       "number":"09",
       "bg": "from-slate-900 to-slate-800",
       "levelColor":"bg-sky-300/20 text-sky-400",
       "iconColor": "text-lime-400"
    },

    {
        "title":"Focus Sprint",
       "level":"challenge",
       "icon":"fa-solid fa-person-running",
       "number":"09",
       "bg": "from-slate-900 to-slate-800",
       "levelColor":"bg-violet-300/20 text-violet-400",
       "iconColor": "text-lime-100"
    },
    {
        "title":"Instant Type",
       "level":"challenge",
       "levelColor":"bg-orange-500/20 text-orange-400",
       "icon":"fa-solid fa-zap",
       "number":"09",
       "bg": "from-slate-900 to-slate-800",
       "levelColor":"bg-orange-300/20 text-orange-400",
       "iconColor": "text-sky-400"
    },

    {
         "title":"Smooth Typing",
       "level":"challenge",
       "levelColor":"bg-orange-500/20 text-orange-400",
       "icon":"fa-solid fa-water",
       "number":"09",
       "bg": "from-slate-900 to-slate-800",
       "levelColor":"bg-orange-300/20 text-orange-400",
       "iconColor": "text-sky-100"
    },

    {
         "title":"Mirror Mode",
       "level":"challenge",
       "levelColor":"bg-orange-500/20 text-orange-400",
       "icon":"fa-solid fa-arrows-left-right",
       "number":"09",
       "bg": "from-slate-900 to-slate-800",
       "levelColor":"bg-orange-300/20 text-orange-400",
       "iconColor": "text-sky-400",

    },

    {
      "title":"Ghost Typing",
       "level":"challenge",
       "levelColor":"bg-orange-500/20 text-orange-400",
       "icon":"fa-solid fa-ghost",
       "number":"09",
       "bg": "from-slate-900 to-slate-800",
       "levelColor":"bg-orange-300/20 text-orange-400",
       "iconColor": "text-sky-100"

    },

    {
      "title":"Flash Words",
       "level":"challenge",
       "levelColor":"bg-orange-500/20 text-orange-400",
       "icon":"fa-solid fa-bolt-lightning",
       "number":"09",
       "bg": "from-slate-900 to-slate-800",
       "levelColor":"bg-orange-300/20 text-orange-400",
       "iconColor": "text-yellow-100"

    },

    {
    
      "title":"Spy Mission",
       "level":"challenge",
       "levelColor":"bg-orange-500/20 text-orange-400",
       "icon":"fa-solid fa-user-secret",
       "number":"09",
       "bg": "from-slate-900 to-slate-800",
       "levelColor":"bg-orange-300/20 text-orange-400",
       "iconColor": "text-red-200"

    
    },

    {
      "title":"Lava Floor",
       "level":"challenge",
       "levelColor":"bg-orange-500/20 text-orange-400",
       "icon":"fa-solid fa-fire",
       "number":"09",
       "bg": "from-slate-900 to-slate-800",
       "levelColor":"bg-orange-300/20 text-orange-400",
       "iconColor": "text-orange-500"

    },

    {
      "title":"Ice Mode",
       "level":"challenge",
       "levelColor":"bg-orange-500/20 text-orange-400",
       "icon":"fa-solid fa-snowflake",
       "number":"09",
       "bg": "from-slate-900 to-slate-800",
       "levelColor":"bg-orange-300/20 text-orange-400",
       "iconColor": "text-sky-700"

    },

    {
      "title":"Zombie Keys",
       "level":"challenge",
       "levelColor":"bg-orange-500/20 text-orange-400",
       "icon":"fa-solid fa-skull",
       "number":"09",
       "bg": "from-slate-900 to-slate-800",
       "levelColor":"bg-orange-300/20 text-orange-400",
       "iconColor": "text-white"

    }

]

@app.route("/")
def typing():
    return render_template("index.html")

@app.route("/practice")
def practice():
    return render_template("Practice.html" , tasks=tasks)


@app.route("/practice/<int:task_id>")
def practice_detail(task_id):
    ##now we take a one task in tasks list according to task_id
    if task_id <len(tasks):
        selected_task = tasks[task_id]
        return render_template("practice_detail.html", task=selected_task)
    else:
        return "Task not found!", 404

@app.route("/settings")
def settings():
        return    render_template("settings.html")


@app.route("/history")
def history():
    return render_template("history.html")


@app.route("/games")
def achievements():
    return render_template("Games.html")

@app.route("/stats")
def stats():
    return render_template("stats.html")



  
@app.route("/review")
def review():
    return render_template("review.html")



@app.route("/howToPlay")
def howToPlay():
    return render_template("howToPlay.html",overviews=overviews)

@app.route("/wordScript")
def wordScript():
    return render_template("wordScript.html",cards=cards)


@app.route("/letterfall")
def letterfall():
    return render_template("letterfall.html",letterFallCards=letterFallCards)

@app.route("/spaceRescue")
def spaceRescue():
    return render_template("spaceRescue.html")

@app.route("/speedSentence")
def speedSentence():
    return render_template("speedSentence.html")

@app.route("/numberRush")
def numberRush():
    return render_template("numberRush.html")

@app.route("/wordHunt")
def wordHunt():
    return render_template("wordHunt.html")

@app.route("/timeAttack")
def timeAttack():
    return render_template("timeAttack.html")

@app.route("/findObject")
def findObject():
    return render_template("findObject.html")

@app.route("/codeTyping")
def codeTyping():
    return render_template("codeTyping.html")

@app.route("/sentenceFixer")
def sentenceFixer():
    return render_template("sentenceFixer.html")

@app.route("/zombieTyping")
def zombieTyping():
    return render_template("zombieTyping.html")

@app.route("/beatTyping")
def beatTyping():
    return render_template("beatTyping.html")


@app.route("/waveSurvival")
def waveSurvival():
    return render_template("waveSurvival.html")

@app.route("/wordPuzzle")
def wordPuzzle():
    return render_template("wordPuzzle.html")

@app.route("/bombDefuse")
def bombDefuse():
    return render_template("bombDefuse.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000))
    ,debug=True
            
)