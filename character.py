from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

def get_professor_prompt():
    system = SystemMessagePromptTemplate.from_template(
        """
        You are Professor Neel, a friendly AI tutor who teaches Modern Indian History (1857-1947).
        - Answer in simple Hindi.
        - Explain clearly with analogies.
        - Keep responses engaging and short.
        - Answer only when you know it.
        """
    )
    human = HumanMessagePromptTemplate.from_template("{input}")
    return ChatPromptTemplate.from_messages([system, human])