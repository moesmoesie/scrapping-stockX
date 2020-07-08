from bot import JordanBot
from database_provider import DatabaseProvider
import queries
if __name__ == "__main__":
    jordan_bot = JordanBot()
    jordan_bot.scrape_jordan_sales()