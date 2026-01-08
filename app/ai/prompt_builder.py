class PromptBuilder:
    def build(self, context: dict):
        return f"""
You are a professional crypto trader AI.
Market data:
{context}

Respond only in JSON:
{{
  "bias": "bull|bear|neutral",
  "confidence": 0-1,
  "notes": "short reasoning"
}}
"""
