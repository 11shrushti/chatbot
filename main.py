import os
import openai
from fastapi import FastAPI , HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from nltk.sentiment.vader import SentimentIntensityAnalyzer

load_dotenv

app = FastAPI()

analyzer = SentimentIntensityAnalyzer()

openai.api_key = os.getenv("sk-zAJwQEULIAoWvsqNWdlw2uao9-quh-TQVlvfbhG1NNT3BlbkFJifcMg8h0vYdKq4ITTwZm-errmKfJeykV1wKkbZROQA")

# define the price range for the negotiation
MIN_PRICE = 50
MAX_PRICE = 100

class Offer(BaseModel):
    user_price: float
    user_message: str

def get_chatgpt_response(prompt:str):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens = 150
        )  
        return response.choices[0].text.strip()
    except Exception as e:
        raise HTTPException  (status_code=500, details = str(e))
    
def analyze_sentiment(text:str):
    sentiment = analyzer.polarity_scores(text)  
    return sentiment["compound"]  

@app.post("/negotite/")
async def negotiate(offer:Offer):
    user_price = offer.user_price
    user_message = offer.user_message

    sentiment_score = analyze_sentiment(user_message)

    discout_factor = 0.05 if sentiment_score > 0.5 else 0

    chatbot_price = MAX_PRICE * (1-discout_factor)

    # negotiation logic
    if user_price >= chatbot_price:
        response_text = f"Great! we can agree on {user_price}"
    elif MIN_PRICE <= user_price < chatbot_price:
        chatbot_price = (user_price + chatbot_price) / 2
        response_text = f"Hmm, {user_price} is a bit low . How about we settle at {chatbot_price}?" 
    else:
        response_text = f"Sorry,{user_price} is too low. The minimun we can accept is {MIN_PRICE}"      

    chagpt_prompt = f"Respond as a friendly supplier negotiating with the a customer. The customer offered {user_price}, and the bot suggests {chatbot_price}"     
    chatbot_response = get_chatgpt_response(chagpt_prompt)

    return {"bot_response": chatbot_response, "final_offer":chatbot_price}