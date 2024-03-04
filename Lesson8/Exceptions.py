import requests
import json

from Config import keys


class APIException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):

        if quote == base:
            raise APIException(f'Введите различные валюты: {base}.')

        if (base == 'dollar' or base == 'euro' or base == 'rouble' or quote == 'dollar'
                or quote == 'euro' or quote == 'rouble'):
            raise APIException('Введите валюту на русском языке.')

        if float(amount) <= 0:
            raise APIException(f'Количество должно быть больше 0.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')
        try:
            amount = float(amount)

        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        return json.loads(r.content)[keys[quote]] * amount
