import random

class ProxyManager:
    use_count = 0

    def __init__(self):
        f = open("proxies.txt", "r")
        text = f.read()
        self.__proxies = text.split('\n')
        random.shuffle(self.__proxies)
        
    def load_proxy(self):
        if self.use_count > 20:
            self.change_proxy()
            print(f"IP has changed to {self.__proxies[0]}")
        self.use_count += 1
        return {
                f"http://": self.__proxies[0],
                f"https://": self.__proxies[0],
        }
        
    def change_proxy(self):
        ip = self.__proxies.pop()
        self.__proxies.insert(0,ip)
        self.use_count = 0