import requests

search_term = input("Enter search term: ")
pg_num = 0
products = []
while True:
    url = "https://www.mio.se/api/product-listing/search?from=" + str(pg_num) + "&query=" + search_term
    response = requests.get(url)
    data = response.json()

    d = data["products"]
    for i in d:
        product = {}
        product['name'] = i.get('name', '').strip()
        product['url'] = "https://www.mio.se" + i.get('url', '')
        product['price'] = i.get('price', 0)
        products.append(product)

    if data.get("nextPage") == None:
        break
    pg_num += 24


for product in products:
    print(f"{product}\n")