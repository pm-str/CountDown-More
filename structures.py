import abc
from datetime import datetime


class ItemType:
    TEXT = 'text'
    COUNTDOWN = 'countdown'
    CLOCK = 'clock'
    ABSTRACT = 'abstract'


class AbstractItem(abc.ABC):
    ratio_x: float = None
    ratio_y: float = None
    size: int = 30
    color: str = None
    font: str = None
    is_bold: bool = False
    is_italic: bool = False
    is_underline: bool = False

    type: str = ItemType.ABSTRACT

    def __str__(self):
        raise NotImplementedError

    def get_data(self):
        raise NotImplementedError


class RichText(AbstractItem):
    text: str = ''
    type = ItemType.TEXT
    _trunc_length = 30
    prefix = 'TXT'

    def __str__(self):
        if len(self.text) < self._trunc_length:
            return f'{self.prefix}: {self.text}'
        return f'{self.prefix}: {self.text[:self._trunc_length]}...'

    def get_data(self):
        return self.text


class ClocksData(AbstractItem):
    fmt: str = None
    prefix = 'CLK'

    type = ItemType.CLOCK

    @staticmethod
    def now_in_fmt(fmt: str):
        return datetime.now().strftime(fmt)

    def __str__(self):
        return f'{self.prefix}: {self.now_in_fmt(self.fmt)}'

    def get_data(self):
        return self.now_in_fmt(self.fmt)


class Countdown(AbstractItem):
    start: float = None
    end: float = None
    format: str = None
    is_blinked: bool = None
    type = ItemType.COUNTDOWN
    prefix = 'CNT'

    @staticmethod
    def timestamp_to_datetime(timestamp: float, fmt: str):
        return datetime.fromtimestamp(timestamp).strftime(fmt)

    def __str__(self):
        start = self.timestamp_to_datetime(self.start, self.format)
        end = self.timestamp_to_datetime(self.end, self.format)
        if self.is_blinked:
            return f'{self.prefix}: {start} - {end} - blink'
        return f'{self.prefix}: {start} - {end}'

    def get_data(self):
        left_tsp = max(self.end - datetime.now().timestamp(), 0)
        hours = int(left_tsp // 3600)
        minutes = int((left_tsp - (hours * 60)) // 60)
        seconds = int((left_tsp - (hours * 60)) % 60)

        dt = datetime(year=2000, month=1, day=1, hour=hours, minute=minutes, second=seconds)
        return dt.strftime(self.format)





