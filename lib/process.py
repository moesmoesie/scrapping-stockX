from typing import Optional, Dict, List
import json


def read_file_bytes(file_path) -> Optional[bytes]:
    """
        reads the content of a file as bytes and returns the bytes
        if no file cant be found None will be returned
    """

    try:
        with open(file_path, "rb") as file:
            return file.read()
    except:
       return None


def read_bytes_json(bytes : bytes) -> Optional[Dict]:
    """
        returns a json of the givin bytes. If not in correct json format
        it wil return None
    """
    try:
        return json.loads(bytes)
    except:
        return None

def read_all_proxies() -> List[str]:
    f = open("proxies.txt", "r")
    text = f.read()
    proxies = text.split("\n")
    return proxies