import random

def download_image(folder_name):
    # Получаем список файлов в папке
    files = os.listdir(folder_name)

    # Определяем порядковый номер следующей картинки
    image_number = len(files) + 1

    # Формируем URL для скачивания картинки
    url = "https://fonwall.ru/category/koty/"  # Здесь нужно указать URL сервиса с котиками

    # Отправляем GET-запрос для получения HTML-страницы
    response = requests.get(url)
    html = response.text

    # Извлекаем URL-адреса всех картинок на странице
    image_urls = re.findall(r'<img src="([^"]+)"', html)

    # Выбираем случайный URL-адрес картинки
    random_image_url = random.choice(image_urls)

    # Отправляем GET-запрос для скачивания случайной картинки
    response = requests.get(random_image_url)

    # Сохраняем картинку в папку с текущим днем
    image_path = os.path.join(folder_name, f"{image_number}.png")
    with open(image_path, 'wb') as file:
        file.write(response.content)

folder_name = create_folder()
download_image(folder_name)