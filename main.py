#Loading data from web sources
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.agents import Tool, initialize_agent

# 1. Load environment
load_dotenv()
if "OPENAI_API_KEY" not in os.environ:
    raise ValueError("OPENAI_API_KEY is missing in your .env file.")

# 2. Load documents
urls = [
    "https://lilianweng.github.io/posts/2024-11-28-reward-hacking/",
    "https://lilianweng.github.io/posts/2024-07-07-hallucination/",
    "https://lilianweng.github.io/posts/2024-04-12-diffusion-video/",
]

print("🔄 Loading documents...")
docs = []
for url in urls:
    loader = WebBaseLoader(url)
    docs.extend(loader.load())

# 3. Split documents
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = splitter.split_documents(docs)

# 4. Create vectorstore
print("📦 Creating vectorstore...")
vectorstore = FAISS.from_documents(splits, OpenAIEmbeddings())
retriever = vectorstore.as_retriever()

# 5. Define tool
retriever_tool = Tool(
    name="vectorstore",
    func=retriever.invoke,
    description="Searches and returns documents from the vectorstore.",
)

# 6. Define LLM and agent
llm = ChatOpenAI(temperature=0)
agent = initialize_agent(
    tools=[retriever_tool],
    llm=llm,
    agent="chat-zero-shot-react-description",
    verbose=True,
)

# 7. Run query
print("\n🤖 Agent is running...\n")
response = agent.invoke("What Causes Hallucinations in LLMs?") 
print("\n✅ Final Answer:\n", response)
