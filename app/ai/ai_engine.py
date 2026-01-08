import json
from app.ai.prompt_builder import PromptBuilder
from app.ai.confidence_filter import ConfidenceFilter

class AIEngine:
    def __init__(self, llm_client):
        self.llm = llm_client
        self.prompt_builder = PromptBuilder()
        self.filter = ConfidenceFilter()

    def analyze(self, market_context):
        prompt = self.prompt_builder.build(market_context.to_dict())
        response = self.llm(prompt)

        data = json.loads(response)
        if not self.filter.allow(data["confidence"]):
            return None

        return data
