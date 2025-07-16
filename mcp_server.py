import json
import gradio as gr
from textblob import TextBlob


def sentiment_analysis(text: str) -> str:
    """
    Analysis of the sentiment behing a text
    Args:
        text(str): it's the text you want to make a sentiment analysis on
    Return a Json String, containing
        - polarity
        - subjectivity
        - assessment
    """
    blob = TextBlob(text)
    data = {
        "polarity": round(blob.sentiment.polarity, 2),
        "subjectivity" : round(blob.sentiment.subjectivity, 2),
         "assessment": "positive" if blob.sentiment.polarity > 0 else "negative" if blob.sentiment.polarity < 0 else "neutral"
    }
    return json.dumps(data)



demo = gr.Interface(fn = sentiment_analysis,
                    inputs= gr.Textbox(placeholder= "Enter your text, and our system will give you the sentiment"),
                    outputs= gr.Textbox(),
                    title= "Sentiment Analysis")



if __name__ == "__main__":
    demo.launch(mcp_server=True)