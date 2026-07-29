from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load API keys from .env
load_dotenv()

# Create the prompt
prompt = ChatPromptTemplate.from_template(
    "Answer the following question:\n{question}"
)

# Create the OpenAI model
model = ChatOpenAI(
    model="gpt-4.1-nano"
)

# Create the output parser
parser = StrOutputParser()

# Create the LangChain chain
chain = prompt | model | parser

# Get user input
question = input("Ask a question: ")

# Generate the response
response = chain.invoke(
    {"question": question}
)

# Display the answer
print("\nAI Answer:")
print(response)