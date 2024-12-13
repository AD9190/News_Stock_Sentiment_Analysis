# News Sentiment Analysis Application

This project is a **News Sentiment Analysis Application** built using **Streamlit** and **Transformers**. It fetches news articles related to a given stock ticker or keyword and analyzes their sentiment using the `ProsusAI/finbert` model. The app provides an overall sentiment score and detailed insights into individual articles, making it useful for understanding market sentiment for a stock or topic.

## Features

- **Sentiment Analysis**: Analyzes news articles using a financial sentiment analysis model.
- **Real-Time Fetching**: Fetches the latest articles using the [NewsAPI](https://newsapi.org/).
- **Detailed Analysis**: Displays sentiment scores and classifications (Positive, Negative, Neutral) for each article.
- **Interactive Interface**: User-friendly and responsive design using Streamlit.

---

## Demo

![image](https://github.com/user-attachments/assets/327766d0-c40b-4f82-a14d-27890148d738)


---

## How It Works

1. **User Input**: Enter a stock ticker (optional), a keyword, and your NewsAPI key.
2. **Data Fetching**: The app fetches news articles matching the keyword from NewsAPI.
3. **Sentiment Analysis**: Each article's sentiment is analyzed using the `ProsusAI/finbert` model.
4. **Results Display**: Overall sentiment and detailed article sentiment are shown in the app.

---

## Installation

### Prerequisites

- Python 3.8 or higher
- A valid API key from [NewsAPI](https://newsapi.org/)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/news-sentiment-analysis.git
   cd news-sentiment-analysis
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```
4. Open your browser and navigate to `http://localhost:8501` to access the app.

---

## Usage

1. **Enter Stock Ticker (Optional)**: Specify a stock ticker for context (e.g., `AAPL`, `GOOGL`).
2. **Enter Keyword**: Provide a keyword to fetch related articles (e.g., `technology`, `finance`).
3. **Enter NewsAPI Key**: Paste your NewsAPI key to allow fetching of news articles.
4. Click **Analyze** to view sentiment results.

---

## Sidebar Instructions

### Steps to Get a NewsAPI Key

1. Visit [NewsAPI.org](https://newsapi.org).
2. Sign up using your email to create an account.
3. Log in and navigate to the "Get API Key" section.
4. Copy the provided API key.
5. Paste the API key in the app to fetch news articles.

---

## File Structure

```
news-sentiment-analysis/
├── app.py               # Main application file
├── requirements.txt     # Dependencies
├── README.md            # Project documentation
```

---

## Dependencies

The project requires the following Python libraries:

- **Streamlit**: For the web app interface
- **Transformers**: For sentiment analysis using `ProsusAI/finbert`
- **Requests**: To fetch news articles from NewsAPI

Install these dependencies using the command:
```bash
pip install -r requirements.txt
```

---

## Future Enhancements

- Add support for visualizing sentiment trends over time.
- Include additional filtering options for news sources.
- Support multi-language sentiment analysis.

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.


## Acknowledgments

- **Transformers Library**: [Hugging Face](https://huggingface.co/)
- **NewsAPI**: [NewsAPI.org](https://newsapi.org/)

---

## Contact

For any inquiries or support, please reach out to:

- **Email**: adasgupta2004@gmail.com
- **GitHub**: [AD9190](https://github.com/AD9190)
