import requests

from settings import CURRENCY, LOCATION, MAIN_URL, SPP


def parse(item):
    params = {
        'nm': item,
        'curr': CURRENCY,
        'dest': LOCATION,
        'spp': SPP
    }
    response = requests.get(MAIN_URL, params=params).json()
    product_info = response['data']['products'][0]
    original_price = product_info['priceU']
    sale_price = product_info['salePriceU']
    price_info = {
        'original_price': original_price,
        'sale_price': sale_price
    }
    return price_info


def main():
    print('Введите артикул:')
    item = input()
    product_info = parse(item)
    print(
        f'Старая цена: {product_info["original_price"]/100} ₽\n'
        f'Новая цена: {product_info["sale_price"]/100} ₽'
    )


if __name__ == '__main__':
    main()
