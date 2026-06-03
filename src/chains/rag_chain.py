# Imports
from pydantic import BaseModel, Field
from langchain_core.runnables import RunnableParallel, RunnableLambda, RunnablePassthrough
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from src.config import OPENAI_API_KEY

# Formatting the retrieved documents
def format_docs(docs):
    """
    Convert retrieved documents into context string.
    """

    return "\n\n".join(doc.page_content for doc in docs)

# Structured output schema
class Answer(BaseModel):
    answer: str = Field(
        description = "Answer to the user's question"
    )
  
    confidence: str = Field(
        description="""
        Confidence in the answer based on the retrieved context.

        Use:
        - High: answer directly supported by context
        - Medium: partially supported
        - Low: weakly supported or not found
        """
    )
  
    found_in_video: bool = Field(
        description = "Whether the answer was found in the retrieved context"
    )
  
parser = PydanticOutputParser(pydantic_object = Answer)

# Prompt template for the LLM
prompt = ChatPromptTemplate.from_template("""
    You are a Retrieval-Augmented Generation (RAG) assistant specialized in answering questions about a YouTube video.

    Instructions:

    - Answer only from the provided context.
    - Treat the retrieved context as the sole source of truth.
    - Do not use prior knowledge.
    - Do not invent facts.
    - If the answer is partially available, answer only the supported portion.
    - If the answer is not available, say:
        "I could not find information about that in the video."
    - If the question is unrelated to the video, explain that the video does not contain the requested information.
    - Prefer concise but complete answers.
    - Preserve technical terminology from the context.
    - When listing multiple points, use bullet points.

    {format_instructions}

    Retrieved Context:
    --------------------
    {context}
    --------------------

    Question:
    {question}

    Provide a factual answer based strictly on the retrieved context.
    """)

partial_prompt = prompt.partial(
    format_instructions = parser.get_format_instructions()
)

# Model for generating answers
llm = ChatOpenAI(
    model="gpt-5.4-mini",
    temperature=0.3,
    api_key=OPENAI_API_KEY
)

# RAG Chain implementation
def build_rag_chain(retriever):

    parallel_chain = RunnableParallel(
        {
            "context": retriever | RunnableLambda(format_docs),
            "question": RunnablePassthrough()
        }
    )

    main_chain = parallel_chain | partial_prompt | llm | parser

    return main_chain
