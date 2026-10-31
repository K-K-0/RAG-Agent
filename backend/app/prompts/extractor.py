import json

from prompts.metadata import DocumentMetadata


class MetadataExtractor:

    def __init__(self, llm):
        self.llm = llm


    def extract(self, text):

        prompt = f"""
You are a metadata extraction system.

Extract metadata from the text.

Return ONLY valid JSON.

Do not return explanation.
Do not return a list.

Format:

{{
    "course_name": "",
    "document_type": "",
    "level": "",
    "topic": ""
}}

If something is missing return null.

TEXT:

{text}
"""


        response = self.llm.invoke(prompt)


        metadata = json.loads(
            response.content
        )


        return DocumentMetadata(
            **metadata
        ).model_dump()