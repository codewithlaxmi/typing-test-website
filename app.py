from flask import Flask, render_template

app = Flask(__name__)



tasks = [
    {
        "title": "Basic words",
        "level": "Easy level",
        "textIcon": "ABC",
        "number": "01",
        "bg": "from-slate-900 to-slate-800",
        "levelColor": "bg-green-500/20 text-green-400"
    },

    {
        "title": "Easy sentences",
        "level": "Easy level",
        "icon": 'fa-solid fa-comment-dots',
        "number": "06",
        "bg": "from-slate-500/20 to-slate-800",
        "levelColor": "bg-green-500/20 text-green-400",
        "iconColor": "text-cyan-400"
    },

    {
        "title": "Big words",
        "level": "Easy level",
        "icon": " fa-solid fa-book-open ",
        "number": "08",
        "bg": "from-slate-500/20 to-slate-800",
        "levelColor": "bg-green-500/20 text-green-400",
        "iconColor":"text-orange-400"
    },
    
    {
        "title":"Paragraph",
        "level":"Easy level",
        "icon": "fa-solid fa-file-lines",
        "number":"04",
        "bg": "from-slate-900 to-slate-800",
        "levelColor":"bg-green-500/20 text-green-400",
        "iconColor":"text-pink-400"
    },

    {
        "title":"easy lines",
        "level":"Easy level",
        "icon":"fa-solid fa-file-lines",
        "number":"05" ,
       "bg": "from-slate-900 to-slate-800",
        "levelColor":"bg-green-500/20 text-green-400",
        "iconColor":"text-green-200"
           
   },

      {
        "title":"Speed test",
        "level":"Easy level",
        "icon":"fa-solid fa-gauge-high",
        "number":"06" ,
        "bg": "from-slate-900 to-slate-800",
        "levelColor":"bg-green-500/20 text-green-400",
        "iconColor":"text-sky-500"
           
   },

   {
       "title":"Speed test ",
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

@app.route("/history")
def history():
    return render_template("History.html")

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
    return render_template("howToPlay.html")






if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))