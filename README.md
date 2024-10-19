# ChatLlama-Chatbot-based-on-Llama-3.1-70b
# ChatLlama 🦙

ChatLlama is an interactive chatbot application built using Streamlit and powered by the Llama 3.1-70b model. This chatbot is designed to provide helpful responses to user queries in a conversational format.

## Features

- Interactive chat interface using Streamlit
- Memory of conversation history
- Simple and user-friendly design
- Powered by the Llama 3.1-70b language model

## Requirements

- Python 3.8 or higher
- Streamlit
- Groq SDK

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Akiffazal/chatllama.git
   cd chatllama
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `config.json` file in the root directory with your Groq API key:

   ```json
   {
       "GROQ_API_KEY": "your_groq_api_key_here"
   }
   ```

## Usage

1. Start the Streamlit app:

   ```bash
   streamlit run main.py
   ```

2. Open your web browser and navigate to `http://localhost:8501` to interact with the chatbot.

3. Type your questions in the input field, and ChatLlama will provide responses powered by the Llama 3.1-70b model.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please feel free to create a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

- [Streamlit](https://streamlit.io/) - for creating an easy-to-use framework for building web apps
- [Groq](https://www.groq.com/) - for providing the powerful Llama language model
