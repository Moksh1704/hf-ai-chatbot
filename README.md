# Multi-Interface AI Chatbot (Llama 3.1 & Qwen 2.5)

A robust AI chatbot application built with Python, utilizing the Hugging Face Inference API. This project demonstrates how to integrate Large Language Models (LLMs) into both a CLI environment and a modern Web UI.

##  Features
- **Dual Interface**: Includes a Command Line Interface (CLI) for lightweight testing and a Streamlit-based Web UI for a better user experience.
- **State-of-the-Art Models**: Configured to use Qwen 2.5 and Llama 3.1 via Hugging Face's serverless inference.
- **Session Management**: Implements Streamlit `session_state` to maintain conversation history in the web browser.
- **Secure Configuration**: Uses `.env` files and environment variables to protect sensitive API credentials.

##  Tech Stack
- **Language**: Python 3.x
- **API**: Hugging Face Inference API (`huggingface_hub`)
- **Frontend**: Streamlit
- **Environment**: Dotenv for secret management

##  Installation & Setup
1. **Clone the Repository**:
   ```bash
   git clone [https://github.com/Moksh1704/hf-ai-chatbot.git](https://github.com/Moksh1704/hf-ai-chatbot.git)
   cd hf-ai-chatbot
   ```
2. **Install Dependencies:**
```bash
pip install -r requirements.txt
```
3. **Configure API Token:**
- Create a .env file in the root directory.
- Add your token: HF_API_TOKEN=your_huggingface_token_here

## Usage

- To run the Web UI: streamlit run app.py
- To run the CLI version: python basic_chatbot.py
