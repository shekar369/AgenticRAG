import streamlit as st
import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.agents import Tool, initialize_agent

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    st.error("OPENAI_API_KEY not found in .env")
    st.stop()

st.title("🧠 AgenticRAG: Streamlit Demo")
st.markdown("Ask questions based on recent blog posts by Lilian Weng!")

user_input = st.text_input("Ask your question:", "What is reward hacking?")

if user_input:
    with st.spinner("Loading documents and initializing agent..."):

        urls = [
            "https://lilianweng.github.io/posts/2024-11-28-reward-hacking/",
            "https://lilianweng.github.io/posts/2024-07-07-hallucination/",
            "https://lilianweng.github.io/posts/2024-04-12-diffusion-video/",
        ]

        docs = []
        for url in urls:
            loader = WebBaseLoader(url)
            docs.extend(loader.load())

        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        splits = splitter.split_documents(docs)

        vectorstore = FAISS.from_documents(splits, OpenAIEmbeddings())
        retriever = vectorstore.as_retriever()

        retriever_tool = Tool(
            name="vectorstore",
            func=retriever.invoke,
            description="Searches and returns documents from the vectorstore.",
        )

        llm = ChatOpenAI(temperature=0)
        agent = initialize_agent(
            tools=[retriever_tool],
            llm=llm,
            agent="chat-zero-shot-react-description",
            verbose=True,
        )

        response = agent.invoke(user_input)

    st.subheader("✅ Agent Response")
    st.markdown(response)
