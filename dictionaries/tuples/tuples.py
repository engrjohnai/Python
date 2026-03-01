

stocks = {
    "info": [600, 630, 620],
    "ril":  [1430, 1490, 1567],
    "mtl": [234, 180, 160]
}
a = input('Enter the value of Operation: Either Print/Add: ').lower()

info_avg = round(sum(stocks['info']) / len(stocks['info']), 2)
ril_avg = round(sum(stocks['ril']) / len(stocks['ril']), 2)
mtl_avg = round(sum(stocks['mtl']) / len(stocks['mtl']), 2)

if a == 'print':
    print(f'info ==> {stocks['info']} ==> avg: {info_avg}')
    print(f'ril ==> {stocks['ril']} ==> avg: {ril_avg}')
    print(f'mtl ==> {stocks['mtl']} ==> avg: {mtl_avg}')

elif a == 'add':
    a_stock = input('Enter the stock sticker name: ')
    a_price = int(input('Enter the price: '))
    stocks[a_stock] = [a_price]
    print(stocks)

else:
    print('You have selected the wrong operator')

