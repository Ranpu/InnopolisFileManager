import requests
from bs4 import BeautifulSoup


def parse_book_page(url):
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Ошибка запроса. Код состояния: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    book_blocks = soup.find_all("article", class_="product-card")

    for book_block in book_blocks:
        image_url_list = book_block.find("source")["data-srcset"].split(",")
        image_url = image_url_list[0]
        if ".jpg 2x" in image_url:
            image_url = "https:" + image_url[:-3]
        book_name = book_block["data-b24-name"]
        discount = float(book_block["data-b24-discount"])
        new_price = float(book_block["data-b24-discount"])
        authors_list = [
            elem.text for elem in book_block.find_all(class_="author-list__item")
        ]
        authors = ",".join(authors_list) if len(authors_list) else "Нет"
        old_price = new_price / discount * 100 if discount else new_price
        print(f"Ссылка на изображение: {image_url}")
        print(f"Новая цена: {new_price}")
        print(f"Старая цена: {old_price}")
        print(f"Название книги: {book_name}")
        print(f"Авторы: {authors}")
        print("\n")


url = "https://book24.ru/catalog/vse-obo-vsem-universalnye-entsiklopedii-1239/"
parse_book_page(url)
