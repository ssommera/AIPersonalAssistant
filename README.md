# 🥒 Hey Pickles: A Modular Voice Assistant for AI Research

**Hey Pickles** is a voice-activated assistant built in Python, designed as a sandbox for AI researchers exploring speech interfaces, LLM integration, and human–AI interaction. It combines speech recognition, natural language understanding via OpenAI’s GPT models, and text-to-speech with modular components that support rapid prototyping and experimentation.

---

## 🧠 Research Motivation

Voice interfaces are a frontier in AI research involving challenges like:

- Robust wake-word detection in noisy environments
- Contextual speech recognition and disambiguation
- Natural, human-like language generation
- Emotionally adaptive and personalized voice synthesis
- Multi-turn dialogue management

**Hey Pickles** serves as a testbed for these research domains by offering:

- 🔌 **Pluggable architecture**: swap out modules (e.g., ASR, LLM, TTS) with minimal effort
- 🧪 **Experimentation-ready**: clean, reproducible setup for testing new models or algorithms
- 🔊 **Interactive UX**: voice I/O loop for real-time experimentation
- 📚 **Open and extensible**: ideal for academic projects or research prototypes

## 🚀 How It Works

1. The script continuously listens through your microphone.
2. When the user says **"Hey Pickles ..."**, it:
   - Extracts the command following the wake word.
   - Sends the full speech input to OpenAI's GPT-3.5 Turbo via API.
   - Converts the AI's response into audio using gTTS (British accent).
   - Plays the response using `playsound`.
3. If the user says **"stop"**, the assistant terminates.

---

## 🔧 Configuration

Edit the following variables in the script:

- `api_key`: Your OpenAI API key
- `lang`: Language code for gTTS (default is `'en'`)
- `device_index`: Microphone index used by `speech_recognition` (check your system's index)

---

## 🧠 Example Usage

```plaintext
You: Hey Pickles, what’s the capital of France?
Pickles: The capital of France is Paris.
