from pydantic import BaseModel, Field, model_validator

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
        "title": "Этюд в багровых тонах",
        "author": "Артур Конан Дойл",
        "format": "Текст",
        "url_part": "book",
        "icon_testid": "icon_iconText",
    },
    "series_second": {
        "title": "Знак четырёх",
        "author": "Артур Конан Дойл",
        "format": "Текст",
        "url_part": "book",
        "icon_testid": "icon_iconText",
    },
}
class BookData(BaseModel):
    title: str
    author: str
    format: str
    url_part: str
    icon_testid: str
    @property
    def search_input(self) -> str:
        return f"{self.title} {self.author} {self.format}"