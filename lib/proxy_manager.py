import random

class ProxyManager:
    use_count = 0

    def __init__(self,proxies):
        self.__proxies = proxies
        
    def load_proxy(self):
        if self.use_count > 20:
            self.change_proxy()
        self.use_count += 1
        return {
                f"http://": self.__proxies[0],
                f"https://": self.__proxies[0],
        }
        
    def change_proxy(self):
        ip = self.__proxies.pop()
        self.__proxies.insert(0,ip)
        self.use_count = 0