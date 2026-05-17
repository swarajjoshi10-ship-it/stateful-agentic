from src.langgraphagenticai.state.state import State

class BasicChatbotNode:
    """
    Basic ChatBot login implementation
    """
    def __init__(self,llm):
        self.llm=llm

    def process(self,state)->dict:
        """
        This method processes the input state and generates a response using the provided language model (LLM).
        """
        return {"messages": self.llm.invoke(state["messages"])}