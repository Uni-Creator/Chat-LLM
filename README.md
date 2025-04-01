# Chat with LLM - Streamlit App

![GitHub Repo stars](https://img.shields.io/github/stars/Uni-Creator/Chat-with-LLM?style=social)  ![GitHub forks](https://img.shields.io/github/forks/Uni-Creator/Chat-with-LLM?style=social)

## 📌 Overview
**Chat with LLM** is a Streamlit-based web application that allows users to interact with large language models (LLMs) through a chat interface. You can choose between various models hosted on Hugging Face and adjust parameters such as temperature and max tokens for personalized responses. This app leverages the Hugging Face API to generate text-based responses and provides a user-friendly chat experience.

## 🚀 Features
- **Multiple Model Support**: Choose between models like Mistral-7B, Gemma-3-1b, and DeepSeek-R1.
- **Dynamic Settings**: Adjust the temperature, model selection, and token limits from the sidebar.
- **Real-Time Chat**: Engage in real-time chat with the selected model.
- **Environment Variable Setup**: Easily connect your Hugging Face account for API key integration.
- **Persistent Chat History**: Maintain conversation history across sessions for a more natural experience.


## 🏗️ Tech Stack
- **Python**
- **Streamlit** (for building the web interface)
- **Hugging Face API** (for model inference)
- **Langchain** (for chat history management)

## 📂 Project Structure
```
Chat-with-LLM/
│── __pycache__/              # Cached Python files
│── main.py                   # Main Streamlit app file
│── Screenshots               # Contains ss fo some chats
│── README.md                 # Project documentation
```

## 📦 Installation & Setup
1. **Prerequisites** - Ensure you have Python 3.8+ installed.

2. **Clone the repository**
   ```sh
   git clone https://github.com/Uni-Creator/Chat-with-LLM.git
   cd Chat-with-LLM
   ```
3. **Install dependencies**
   ```sh
   pip install streamlit langchain huggingface_hub
   ```

4. **Run the app**
   ```sh
   streamlit run main.py
   ```


## Usage
1. **Select Model** - Choose the desired model from the sidebar.
2. **Adjust Settings** - Modify the temperature, token limits, and other settings to fine-tune the responses.
3. **Start Chatting** - Type your message in the text input field and hit enter to chat with the model.

## Example Output
```
User: Hello, how are you today?
Model: I'm doing great, thank you for asking! How about you?
```

## Screenshots
Here are some screenshots showcasing the **Chat with LLM** app in action:

![Screenshot 1](screenshots/1.png)
*First view of the app showing the model selection and settings.*

![Screenshot 2](screenshots/2.png)
*Another screenshot showing the chat interface.*

![Screenshot 3](screenshots/3.png)
*Chat in progress with model responses.*

![Screenshot 4](screenshots/4.png)
*User adjusting settings in the sidebar.*

![Screenshot 5](screenshots/5.png)
*Chat in progress with model responses.*

![Screenshot 6](screenshots/6.png)
*Final view with full chat history.*

## Customization
- Modify `app.py` to change the interface or add new functionality.
- Adjust model settings and parameters in the sidebar for different experiences.

## 📊 How It Works
1. The user interacts with the interface built using **Streamlit**.
2. The app sends requests to Hugging Face's inference API.
3. The selected model generates a response based on the input prompt.
4. The response is displayed in the app's chat interface.

## 🛠️ Future Improvements
- Add more language models for broader usage.
- Create a user authentication system for saving chat history.
- Implement a logging feature for conversation analytics.

## 🤝 Contributing
Contributions are welcome! Feel free to open an **issue** or submit a **pull request**.

## 📄 License
This project is licensed under the **MIT License**.




