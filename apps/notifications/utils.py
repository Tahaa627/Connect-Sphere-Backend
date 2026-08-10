import re


def extract_mentions(text):
    """
    Extract usernames mentioned with @username
    """

    pattern = r"@(\w+)"

    return re.findall(pattern, text)