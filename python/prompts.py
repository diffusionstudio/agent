import requests
from smolagents import CODE_SYSTEM_PROMPT

DOCUMENT_CONTEXT_PROMPT = """
<document>
{doc_content}
</document>
"""

CHUNK_CONTEXT_PROMPT = """
Here is the chunk we want to situate within the whole document
<chunk>
{chunk_content}
</chunk>

Please give a short succinct context to situate this chunk within the overall document for the purposes of improving search retrieval of the chunk.
Answer only with the succinct context and nothing else.
"""

QUERY_PROMPT = "Represent this sentence for searching relevant passages: "


def get_system_prompt():
    result = requests.get("https://operator.diffusion.studio/system-prompt.txt")

    return f"{CODE_SYSTEM_PROMPT}\n\n{result.text}"
