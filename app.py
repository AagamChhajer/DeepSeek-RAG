import streamlit as st
from dotenv import load_dotenv
from llama_index.core import Settings
from llama_index.llms.ollama import Ollama
from llama_index.core import PromptTemplate
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import VectorStoreIndex, ServiceContext, SimpleDirectoryReader

# Page configuration
st.set_page_config(
    page_title="DeepSeek RAG Chat",
    page_icon="🤖",
    layout="centered"
)

# Add title and description
st.title("📚 DeepSeek RAG Chat")
st.markdown("""
This application allows you to chat with your PDF documents using DeepSeek LLM and RAG.
""")

# Initialize session state for storing the query engine
if 'query_engine' not in st.session_state:
    st.session_state.query_engine = None

# Sidebar for PDF upload and model initialization
with st.sidebar:
    st.header("Configuration")
    pdf_dir = st.text_input("Enter PDF Directory Path:", 
                           value="/Users/aagamchhajer/Desktop/aagam-projects/DeepSeek-RAG/pdf_dir")
    
    if st.button("Initialize Model"):
        with st.spinner("Loading documents and initializing models..."):
            try:
                # Load documents
                loader = SimpleDirectoryReader(
                    input_dir=pdf_dir,
                    required_exts=[".pdf"],
                    recursive=True
                )
                docs = loader.load_data()
                
                # Initialize embedding model
                embed_model = HuggingFaceEmbedding(
                    model_name="BAAI/bge-large-en-v1.5",
                    trust_remote_code=True
                )
                
                # Initialize LLM
                llm = Ollama(model="deepseek-r1:8b", request_timeout=120.0)
                
                # Configure settings and create index
                Settings.embed_model = embed_model
                Settings.llm = llm
                
                index = VectorStoreIndex.from_documents(docs)
                
                # Create query engine with custom prompt
                query_engine = index.as_query_engine()
                
                qa_prompt_tmpl_str = (
                    "Context information is below.\n"
                    "---------------------\n"
                    "{context_str}\n"
                    "---------------------\n"
                    "Given the context information above I want you to think step by step to answer the query in a crisp manner, "
                    "incase case you don't know the answer say 'I don't know!'.\n"
                    "Query: {query_str}\n"
                    "Answer: "
                )
                qa_prompt_tmpl = PromptTemplate(qa_prompt_tmpl_str)
                
                query_engine.update_prompts(
                    {"response_synthesizer:text_qa_template": qa_prompt_tmpl}
                )
                
                st.session_state.query_engine = query_engine
                st.success("✅ Models initialized successfully!")
                
            except Exception as e:
                st.error(f"Error initializing models: {str(e)}")

# Main chat interface
st.header("Chat with your PDFs")

# Query input
query = st.text_input("Enter your question:")

if st.button("Ask"):
    if st.session_state.query_engine is None:
        st.warning("Please initialize the model first using the sidebar!")
    else:
        if query:
            with st.spinner("Generating response..."):
                try:
                    response = st.session_state.query_engine.query(query)
                    st.markdown("### Answer:")
                    st.markdown(response.response)
                except Exception as e:
                    st.error(f"Error generating response: {str(e)}")
        else:
            st.warning("Please enter a question!")

# Footer
st.markdown("---")
st.markdown("Built with Streamlit, LlamaIndex, and DeepSeek LLM") 