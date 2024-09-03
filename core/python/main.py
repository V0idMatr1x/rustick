import yfinance as yf
from core import main_window

class Stock:
    @staticmethod
    def get_curr_price(symbol) -> str:
        stock = yf.Ticker(symbol)

        return str(stock.info['currentPrice'])    


def main() -> None:
    gold = Stock.get_curr_price("GOLD")    
    main_window(gold)


main()
