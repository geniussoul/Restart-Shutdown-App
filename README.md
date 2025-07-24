🔌💻 Restart & Shutdown App — Because sometimes, even your PC needs a nap 😴💣  
> “Control. Alt. Del? Nah, I wrote my own spell.” – Martand Mishra

---

## 🔍 What Is This?

A **command-line tool** that lets you gracefully *restart* or *shut down* your system — built with **Python’s standard library**.  
No clicky buttons, no laggy UI — just raw, instant action from your terminal.

Great for:
✔️ Lazy wizards 🧙  
✔️ Tinkerers and testers  
✔️ People who *actually* automate their machines

---

## 💡 Why I Built This

Because clicking "Start → Power → Shutdown" felt like trying to shut down a spaceship.  
I wanted **one script** to rule them all — restart, shutdown, cancel if you change your mind — all without touching a mouse.

Also, writing something that interacts with the system is a fun little power trip. 😎

---

## 🔧 Tech Stack

- 🐍 Python 3.x  
- `os`, `platform`, `time` — nothing external  
- Works on both **Windows** & **Linux** (macOS? Not tested yet, brave soul)

---

## ⚙️ How To Use

```bash
# Step 1: Clone the spellbook
git clone https://github.com/geniussoul/Restart-Shutdown-App.git

# Step 2: Open the terminal portal
cd Restart-Shutdown-App

# Step 3: Cast the command
python restart_shutdown.py
📢 You’ll be prompted with menu options like:
1️⃣ Restart
2️⃣ Shutdown
3️⃣ Cancel

Make your pick and let Python take care of the rest.

✨ Features
⚡ Feature	🔍 Description
⏱️ Timed Action	Gives you a few seconds before execution
💥 Restart or Shutdown	Pick your poison
🤹 Cross-Platform	Detects your OS and runs the right commands
🧪 Beginner-Friendly	Teaches os.system() and conditions
🧼 Lightweight & Readable	Under 100 lines, pure Python Zen

🧠 Future-Ready Ideas
GUI version with shutdown timers

Schedule shutdown via datetime

Emergency abort key combo

Logging feature to track system actions

🙋 About Me
Crafted with 🔥 by Martand Mishra
a.k.a. @geniussoul — full-stack of wit, wisdom, and while True loops

“I don’t shut down computers. I whisper them to sleep.”

