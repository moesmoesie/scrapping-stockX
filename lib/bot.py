import network
import process
import create
from models.shoe import Shoe
from models.sale import Sale
from models.filter import Filter
from typing import List
from database_provider import DatabaseProvider
from header_manager import HeaderManager
from proxy_manager import ProxyManager
import queries
from typing import cast
import time
import random

class Bot:
    header_manager = HeaderManager()
    def __init__(self,database_name, proxies):
        self.proxy_manager = ProxyManager(proxies)
        self.database = DatabaseProvider(database_name)

    def scrape_products_from_link(self,link : str) -> List[Shoe]:
        """
            Returns the shoes that are showed on this link
            The maximum shoes that stockx will show are 40
            example link : https://stockx.com/api/browse?productCategory=sneakers&currency=EUR
        """
        attempts = 0
        while True: 
            headers = self.header_manager.load_header()
            proxies = self.proxy_manager.load_proxy()
            status_code,product_bytes,_ = network.get_page_info(link, headers= headers, proxies=proxies)
            try: 
                if status_code == 200:
                    page_json = process.read_bytes_json(product_bytes)
                    products_json = page_json["Products"]
                    products = list(map(lambda x: Shoe(x), products_json))
                    return products
                raise Exception
            except KeyError:
                return []
            except:
                self.pause()
                self.proxy_manager.change_proxy()
                self.header_manager.change_header()
                attempts += 1
                if attempts > 10:
                    return []

    def scape_shoes_from_filters(self,filters:List[Filter]) -> List[Shoe]:
        """
            Returns the shoes that are showed when the provided filters are active.
            The maximum shoes that stockx will show are 1000.
            example filters: [Filter("year", "2020"), Filter("brand", "Nike")]
        """
        query = create.create_query(filters)
        shoes = []
        page_number = 1
        while(True):
            self.pause()
            link = create.create_link(page_number,query)
            products = self.scrape_products_from_link(link)
            if not products:
                break
            shoes.extend(products)
            page_number += 1
        return shoes

    def scrape_sales_from_page(self,link,product_id) -> List[Sale]:
        attempts = 0
        while True:
            headers = self.header_manager.load_header()
            proxies = self.proxy_manager.load_proxy()
            try:
                status_code,sales_bytes,_ = network.get_page_info(link, headers= headers, proxies=proxies)
                if status_code == 200:
                    page_json = process.read_bytes_json(sales_bytes)
                    sales_json = page_json["ProductActivity"]
                    sales = list(map(lambda x: Sale(x,product_id), sales_json))  
                    return sales 
                raise Exception
            except KeyError:
                return []            
            except:
                self.pause()
                self.proxy_manager.change_proxy()
                self.header_manager.change_header()
                attempts += 1
                if attempts > 10:
                    return []

    def scrape_sales_from_shoe_id(self,shoe_id) -> List[Sale]:
        page_number = 1
        all_sales = []
        while True:
            self.pause()
            link = create.create_sales_link(page_number, shoe_id)
            sales = self.scrape_sales_from_page(link,shoe_id)
            if not sales:
                break
            page_number += 1
            all_sales.extend(sales)
        return all_sales

    def scrape_filters_from_link(self,link : str) -> List[Filter]:
        """
            Returns the filters that are available on the provided link.
            example link : https://stockx.com/api/browse?productCategory=sneakers
        """
        _,page_bytes,_ = network.get_page_info(link, headers= self.header_manager.load_header())
        page_json = cast(dict,process.read_bytes_json(page_bytes))
        filters_json = page_json["Facets"]
        filters = []
        for key in filters_json:
            for value in filters_json[key]:
                filters.append(Filter(key,value,filters_json[key][value]))
        return filters


    def pause(self):
        sleep_time = random.randint(0,5)
        time.sleep(sleep_time)

class JordanBot(Bot):
    def __init__(self,database_name, proxies):
        super().__init__(database_name,proxies)

    def scrape_all_jordans(self):
        jordan_filter = Filter("brand", "Jordan")
        initial_link = create.create_link(1,create.create_query([jordan_filter]))
        all_filters : List[Filter] = self.scrape_filters_from_link(initial_link)
        year_queries = [year_filter for year_filter in all_filters if year_filter.name == "year"]
        for year_filter in year_queries:
            shoes = self.scape_shoes_from_filters([year_filter,jordan_filter])
            for shoe in shoes:
                self.database.insert_values(queries.insert_shoe,shoe.get_attributes_tuple())
                print("Shoe Count", self.database.get_values(queries.get_shoe_count)[0][0])


    def jordan_count_in_stockx(self):
        jordan_filter = Filter("brand", "Jordan")
        link = create.create_link(1,create.create_query([jordan_filter]))
        all_filters : List[Filter] = self.scrape_filters_from_link(link)
        count = 0
        for filter in all_filters:
            if filter.name == "year":
                count += filter.amount
        return count

    def scrape_jordan_sales(self, shoes):
        shoe_count = 0
        total_shoe_count = len(shoes)
        for shoe_id in shoes:
            shoe_count += 1
            sales = self.scrape_sales_from_shoe_id(shoe_id)
            for sale in sales:
                self.database.insert_values(queries.insert_sale, sale.get_attributes_tuple())
            sales_count = self.database.get_values(queries.get_sale_count)[0][0]
            print(f"DB: {self.database.name}", 
                  f"Shoe Count: {shoe_count} / {total_shoe_count}", 
                  f"Sale Count:", sales_count)