import json
import requests
from config import exchanges

class ApiException(Exception):
    pass
class Converter:
    @staticmethod
    def get_price(base, sym, amount):
        try:
            base_key = exchanges[base.lower()]
        except KeyError:
            return ApiException(f'Валюта {base} не найдена!')
        try:
            sym_key = exchanges[sym.lower()]
        except KeyError:
            raise ApiException(f'Валюта {sym} не найдена!')

        if base_key == sym_key:
            raise ApiException(f'Невозможно сконвертировать одинаковые валюты{base}!')
        try:
            amount = float(amount.replace(',', '.'))
        except ValueError:
            raise ApiException(f'Не удалось обработать количество {amount}!')
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={sym_key}&from={base_key}&amount={amount}"
        payload = {}
        headers = {
            "apikey": "hXkFDNHiX0o0OMjijSZQT7vNkk73RWIt"
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        resp = json.loads(response.content)
        new_price = resp['result']
        return round(new_price, 2)


