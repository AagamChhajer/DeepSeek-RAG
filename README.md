# DeepSeek RAG Chat 📚

A Streamlit-based application that enables users to have interactive conversations with their PDF documents using DeepSeek LLM and RAG (Retrieval-Augmented Generation) technology.

![DeepSeek RAG Chat Interface](assets/home_page.png)

## Features

- 📄 PDF Document Processing: Load and process multiple PDF files
- 🔍 Advanced RAG Implementation: Uses LlamaIndex for efficient document retrieval
- 🤖 DeepSeek LLM Integration: Powered by DeepSeek-r1 8B model
- 💪 High-Quality Embeddings: Uses BAAI/bge-large-en-v1.5 for document embeddings
- 🎯 Step-by-Step Reasoning: Structured response generation with detailed explanations
- 🖥️ User-Friendly Interface: Clean and intuitive Streamlit-based UI

## Sample Output

The application provides detailed, context-aware responses to user queries:

![Output Example 1](assets/output_sec1.png)
![Output Example 2](assets/output_sec2.png)

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd deepseek-rag-chat
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Make sure you have Ollama installed on your system.

```bash
ollama run deepseek-r1
```

4. Run the application:

```bash
streamlit run app.py
```

## Configure the application:
- Enter the PDF directory path in the sidebar
- Click "Initialize Model" to load documents and set up the system
- Start asking questions about your PDFs

## Requirements

Key dependencies include:
- llama-index==0.12.12
- streamlit==1.41.1
- python-dotenv==1.0.1
- sentence-transformers==2.7.0
- torch>=2.1.2
- And more (see requirements.txt for full list)

## Project Structure

```bash
deepseek-rag-chat/
├── app.py              # Main Streamlit application
├── requirements.txt    # Project dependencies
├── assets/            # Screenshots and images
│   ├── home_page.png
│   ├── output_sec1.png
│   └── output_sec2.png
└── pdf_dir/           # Directory for PDF documents
```

## Features in Detail

- **Document Loading**: Supports recursive PDF loading from specified directories
- **Embedding Generation**: Uses BAAI/bge-large-en-v1.5 for high-quality document embeddings
- **Query Processing**: Custom prompt template for structured and detailed responses
- **Session Management**: Maintains conversation context using Streamlit session state
- **Error Handling**: Robust error handling for model initialization and query processing

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Add your license information here]

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [LlamaIndex](https://www.llamaindex.ai/)
- Uses [DeepSeek LLM](https://github.com/deepseek-ai/DeepSeek-LLM)
