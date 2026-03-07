def summarize_article(text):

    if not text:
        return "No summary available."

    sentences = text.split(".")

    summary = ". ".join(sentences[:3])

    return summary