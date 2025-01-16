
# Jarvis Virtual Assistant

**Jarvis** is a Python-based voice assistant that can perform various tasks like searching Wikipedia, opening websites, telling the time, and sending emails. It uses speech recognition and text-to-speech technologies to interact with the user. The project also features a graphical user interface (GUI) built with Tkinter.

---

## **Features**

- **Speech-to-Text**: Recognizes user commands from speech using the `speech_recognition` library.
- **Text-to-Speech**: Responds to user queries using the `pyttsx3` library.
- **Task Automation**: Can perform tasks like:
  - Search Wikipedia.
  - Open websites (YouTube, Google, Stack Overflow).
  - Play music.
  - Tell the current time.
  - Open Visual Studio Code.
  - Send emails (requires configuration).
- **GUI Interface**: A user-friendly interface built with `tkinter` and `PIL` for background image support.

---

## **Requirements**

- Python 3.x
- Install the required libraries using pip:

  ```bash
  pip install pyttsx3
  pip install SpeechRecognition
  pip install wikipedia
  pip install pillow
