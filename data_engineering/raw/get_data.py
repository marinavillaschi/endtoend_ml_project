import finnhub
from decouple import config


API_KEY = config("API_KEY")

# def get_esg_data():
#     finnhub_client = finnhub.Client(api_key=API_KEY)
#     print(finnhub_client.company_esg_score("AAPL"))


def get_us_visa_data(from_date: str, to_date: str):
    finnhub_client = finnhub.Client(api_key=API_KEY)
    response = finnhub_client.stock_visa_application("AAPL", from_date, to_date)
    return response

    
if __name__ == "__main__":
    get_us_visa_data("2021-01-01", "2022-06-15")