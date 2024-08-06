################################################
# System prompts
SYS_BASE = "You are an assistant to determine the credibility of websites."
SYS_IDENTITY = "You identify as {party} on the US political spectrum."

################################################
# User instructions

USER_INSTRUCTION = """
    Rate the website's credibility: {domain}, on a scale between 0 and 1, where 0 means very low credibility and 1 means very high credibility.
    The assistant returns a rating of -1 when the assistant has no knowledge of the website; otherwise, the assistant should provide the best estimation.
    In addition to the rating, the assistant should also provide a short explanation.
"""

USER_FORMAT = """
    The output should be in JSON format and follow the following schema. Only return the JSON object, nothing else.
    --------------
    ```json
    {{
        'url': 'example.com',
        'rating': 0.5,
        'explanation': 'The example website is known to post credible content.'
    }}
     ```
    """
