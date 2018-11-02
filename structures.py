import abc
from datetime import datetime


class ItemType:
    TEXT = 'text'
    COUNTDOWN = 'countdown'
    ABSTRACT = 'abstract'


class AbstractItem(abc.ABC):
    ratio_x: float = None
    ratio_y: float = None
    size: int = None
    color: str = None
    font: str = None
    is_bold: bool = False
    is_italic: bool = False
    is_underline: bool = False

    type: str = ItemType.ABSTRACT

    def __str__(self):
        return f'T: {self.ratio_w:5.2f} {self.ratio_h:5:2f}'


class RichText(AbstractItem):
    text: str = ''
    type = ItemType.TEXT
    _trunc_length = 30
    prefix = 'T'

    def __str__(self):
        if len(self.text) < self._trunc_length:
            return f'{self.prefix}: {self.text}'
        return f'{self.prefix}: {self.text[:self._trunc_length]}...'


class Countdown(AbstractItem):
    start: float = None
    end: float = None
    format: str = None
    is_reversed: bool = None
    type = ItemType.COUNTDOWN
    prefix = 'C'

    @staticmethod
    def timestamp_to_datetime(timestamp: float, fmt: str):
        return datetime.fromtimestamp(timestamp).strftime(fmt)

    def __str__(self):
        start = self.timestamp_to_datetime(self.start, self.format)
        end = self.timestamp_to_datetime(self.end, self.format)
        if self.is_reversed:
            return f'{self.prefix}: {end} - {start}'
        return f'{self.prefix}: {start} - {end}'




