# 🤖 JARVIS – Your Personal Voice Assistant

JARVIS is a Python-based voice assistant that listens to your voice commands and performs a variety of tasks like searching Wikipedia, opening websites, checking the time, launching apps, and defining words — all through natural language interaction.

> Inspired by Iron Man's J.A.R.V.I.S., this project is your very own virtual helper for multitasking and automation on your system.

---

## ✨ Features

✅ **Voice Interaction** — Uses speech recognition and text-to-speech to listen and respond
✅ **Wikipedia Search** — Quickly fetch summaries from Wikipedia
✅ **Website Launcher** — Opens popular websites like YouTube, Google, Gmail, LeetCode, Stack Overflow, and more
✅ **Time Telling** — Announces the current system time
✅ **App Launcher** — Opens Brave browser or other apps with voice
✅ **Word Definition** — Defines words and opens dictionary sites
✅ **Custom Greetings** — Greets you based on the time of day
✅ **Repeat Function** — Repeats anything you say with "repeat after me"

---

## 🧠 Tech Stack

* `Python 3.x`
* `pyttsx3` — Text-to-speech conversion
* `SpeechRecognition` — For capturing voice input
* `Wikipedia` — For fetching content
* `Webbrowser` — To launch websites
* `PyDictionary` — Optional definition support
* `datetime`, `os` — For system utilities

---

## 🧩 How to Use JARVIS Locally

Follow these steps to download, install, and run JARVIS on your system.

### 1. 🔁 Clone the Repository

```bash
git clone https://github.com/<your-username>/jarvis-voice-assistant.git
cd jarvis-voice-assistant
```

> Replace `<your-username>` with your GitHub username.

### 2. 🛠️ Install the Requirements

Make sure Python 3.x is installed. Then install the dependencies:

```bash
pip install pyttsx3 SpeechRecognition wikipedia PyDictionary
```

> If `pyaudio` causes installation issues, use:

```bash
pip install pipwin
pipwin install pyaudio
```

### 3. 🚀 Run the Assistant

```bash
python jarvis.py
```

Once launched, JARVIS will greet you and begin listening to your voice commands!

---

## 🧪 Sample Commands

* **"Wikipedia Elon Musk"** – Searches Wikipedia
* **"Open YouTube"** – Launches YouTube
* **"What is the time?"** – Tells the current time
* **"Define machine learning"** – Gives a short definition and opens a dictionary page
* **"Open Brave"** – Launches Brave browser (edit the path if needed)
* **"Repeat after me I love Python!"** – Makes JARVIS repeat your words

---

## ⚙️ Customization

* Want to open a different browser or app?
  Just update the path in this section of `jarvis.py`:

```python
b_path="C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
os.startfile(b_path)
```

* Add more websites to the `elif` chain for personalized commands!

---

## 📌 Notes

* Works best with a stable mic setup and internet connection (for speech-to-text and Wikipedia).
* Currently designed for **Windows** (due to `sapi5` TTS engine and `.exe` paths).
* You can easily port it to Linux/Mac by changing the text-to-speech engine and app paths.

---

## 🙌 Credits

Developed by Archit Sharma
Inspired by Iron Man’s JARVIS and built with ❤️ using Python.

