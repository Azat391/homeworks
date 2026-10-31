from pydantic import BaseModel

BOOKS = {
    "main_text": {
        "title": "Мастер и Маргарита",
        "author": "Михаил Булгаков",
        "format": "Текст",
        "url_part": "book",
        "icon_testid": "icon_iconText",
    },
    "second_text": {
        "title": "Собачье сердце",
        "author": "Михаил Булгаков",
        "format": "Текст",
        "url_part": "book",
        "icon_testid": "icon_iconText",
    },
    "audiobook": {
        "title": "Сахарное свечение (сборник)",
        "author": "Дина Рубина",
        "format": "Аудио",
        "url_part": "audiobook",
        "icon_testid": "icon_iconAudio",
    },
    "series_first": {
        "title": "Зима, в которую мы влюбились",
        "author": "Ксения Власова",
        "format": "Текст",
        "url_part": "book",
        "icon_testid": "icon_iconText",
    },
    "series_second": {
        "title": "Война миров. Вечные истории",  # Взял название из URL (voyna-mirov-vechnye-istorii)
        "author": "Герберт Джордж Уэллс",
        "format": "Текст",
        "url_part": "book",
        "icon_testid": "icon_iconText",
    },
    "collection1": {
        "title": "Психосоматика заболеваний кожи",
        "author": "Алексей Игоревич Мелёхин",
        "format": "Текст",
        "url_part": "book",
        "icon_testid": "icon_iconText",
        "url": "https://www.litres.ru/book/aleksey-igorevich-melehin/psihosomatika-zabolevaniy-kozhi-72779659/",
        "collection": "Премия «Здравомыслие»: лонг-лист 2026",
    },
    "collection2": {
        "title": "Сожги свою диету. Как питаться, чтобы потерять вес, а не рассудок",
        "author": "Максим Кузнецов",
        "format": "Текст",
        "url_part": "book",
        "icon_testid": "icon_iconText",
        "url": "https://www.litres.ru/book/maksim-kuznecov-3339/sozhgi-svou-dietu-kak-pitatsya-chtoby-poteryat-ves-a-71865667/",
        "collection": "Премия «Здравомыслие»: лонг-лист 2026",
    },
    "delegation": {
        "title": "Делегирование: результат руками сотрудников. Технология регулярного менеджмента",
        "author": "Александр Фридман",
        "format": "Аудио",
        "genre": "Менеджмент",  # деловая литература / управление
        "url_part": "audiobook",
        "icon_testid": "icon_iconAudio",
        "url": "https://www.litres.ru/audiobook/aleksandr-fridman/delegirovanie-rezultat-rukami-sotrudnikov-tehnologiya-re-63362022/",
    },
    "exploitation": {
        "title": "Вы или вас: профессиональная эксплуатация подчиненных. Регулярный менеджмент для рационального руководителя",
        "author": "Александр Фридман",
        "format": "Аудио",
        "genre": "Менеджмент",  # управление персоналом / деловая литература
        "url_part": "audiobook",
        "icon_testid": "icon_iconAudio",
        "url": "https://www.litres.ru/audiobook/aleksandr-fridman/vy-ili-vas-professionalnaya-ekspluataciya-podchinennyh-r-37961319/",
    },
    "text_audio": {
        "title": "Евгений Онегин",
        "author": "Александр Пушкин",
        "format": "Текст",  # На скриншоте открыта вкладка "Текст"
        "genre": "Классическая литература",
        "url_part": "book",  # В ссылке используется /book/, а не /audiobook/
        "icon_testid": "icon_iconText",
        "url": "https://www.litres.ru/book/aleksandr-pushkin/evgeniy-onegin-72098089/",
    },
}


class BookData(BaseModel):
    title: str
    author: str
    format: str
    url_part: str
    icon_testid: str
    collection: str | None = None
    genre: str | None = None

    @property
    def search_input(self) -> str:
        return f"{self.title} {self.author} {self.format}"
