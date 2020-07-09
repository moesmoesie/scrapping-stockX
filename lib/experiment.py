from bot import JordanBot
import queries
import asyncio
from threading import Thread
import time
import process
import numpy as np
from database_provider import DatabaseProvider

def thread_function(name,proxies,shoes):
    bot = JordanBot(f"DB_{name}.db" ,proxies)
    bot.scrape_jordan_sales(shoes)

if __name__ == "__main__":
    database = DatabaseProvider()
    proxies = process.read_all_proxies()
    shoes = list(map(lambda x: x[0],database.get_values(queries.get_all_shoe_ids)))[1000:]

    proxies_array = list(map(lambda x: list(x),np.array_split(proxies, 3)))
    shoes_array = np.array_split(shoes, 3)

    for i in range(3):
        Thread(target=thread_function, args=(f"{i}", list(proxies_array[i]), list(shoes_array[i]),)).start()