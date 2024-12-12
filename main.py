import streamlit as st
from transformers import pipeline
import requests

# Define the sentiment analysis function
def get_sentiment(ticker, keyword, api_key):
    url = f'https://newsapi.org/v2/everything?q={keyword}&apiKey={api_key}'
    pipe = pipeline("text-classification", model="ProsusAI/finbert")

    response = requests.get(url)
    if response.status_code != 200:
        return {"error": "Failed to fetch news articles."}

    articles = response.json().get('articles', [])

    total_score = 0
    num_articles = 0
    analyzed_articles = []

    for article in articles:
        title = article.get('title')
        description = article.get('description')

        if not description:
            continue

        sentiment = pipe(description)[0]

        if sentiment['label'] in ['positive', 'negative']:
            score = sentiment['score'] if sentiment['label'] == 'positive' else -sentiment['score']
            total_score += score
            num_articles += 1

        analyzed_articles.append({
            "title": title,
            "url": article.get("url"),
            "publishedAt": article.get("publishedAt"),
            "description": description,
            "sentiment": sentiment["label"],
            "score": sentiment["score"]
        })

    if num_articles == 0:
        return {"error": "No relevant articles found."}

    final_score = total_score / num_articles
    overall_sentiment = 'Positive' if final_score > 0.15 else 'Negative' if final_score < -0.15 else 'Neutral'

    return {
        "overall_sentiment": overall_sentiment,
        "final_score": final_score,
        "num_articles": num_articles,
        "analyzed_articles": analyzed_articles
    }

# Streamlit application
def main():
    st.title("News Sentiment Analysis 📈")
    st.write("Analyze news sentiment for a given stock ticker and keyword.")

    # Sidebar instructions
    with st.sidebar:
        st.header("Steps to Get NewsAPI Key")
        with st.expander("Step-by-Step Guide"):
            st.write("1. Visit [NewsAPI.org](https://newsapi.org).")
            st.write("2. Sign up with your email to create an account.")
            st.write("3. Log in and navigate to the 'Get API Key' section.")
            st.write("4. Copy the provided API key.")
            st.write("5. Paste the API key into the field provided in this app.")

    # Input fields
    ticker = st.text_input("Enter Stock Ticker (Optional)")
    keyword = st.text_input("Enter Keyword")
    api_key = st.text_input("Enter NewsAPI Key", type="password")

    if st.button("Analyze"):
        if not keyword or not api_key:
            st.error("Please provide the required inputs.")
        else:
            st.write("Fetching and analyzing articles...")
            result = get_sentiment(ticker, keyword, api_key)

            if "error" in result:
                st.error(result["error"])
            else:
                st.success(f"Overall Sentiment: {result['overall_sentiment']}")
                st.write(f"Sentiment Score: {result['final_score']:.2f}")
                st.write(f"Number of Articles Analyzed: {result['num_articles']}")

                st.subheader("Detailed Article Analysis")
                for article in result["analyzed_articles"]:
                    st.write(f"**Title**: {article['title']}")
                    st.write(f"**Published At**: {article['publishedAt']}")
                    st.write(f"**URL**: [Link]({article['url']})")
                    st.write(f"**Description**: {article['description']}")
                    st.write(f"**Sentiment**: {article['sentiment']} | **Score**: {article['score']:.2f}")
                    st.write("---")

if __name__ == "__main__":
    main()
