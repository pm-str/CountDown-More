import abc
from datetime import datetime


class ItemType:
    TEXT = 'text'
    COUNTDOWN = 'countdown'
    CLOCK = 'clock'
    ABSTRACT = 'abstract'


class AbstractItem(abc.ABC):
    def __init__(self):
        self.has_changed = False
        self.ratio_x: float = 0
        self.ratio_y: float = 0
        self.size: int = 30
        self.color: str = None
        self.font: str = None
        self.is_bold: bool = False
        self.is_italic: bool = False
        self.is_underline: bool = False

        # shadow effect must be >= 0 and <= 8
        self.shadow_blur: int = 0
        self.shadow_offset: int = 0

        self.type: str = ItemType.ABSTRACT

    def __str__(self):
        raise NotImplementedError

    def get_data(self):
        raise NotImplementedError


class RichText(AbstractItem):
    def __init__(self):
        super().__init__()
        self.text: str = ''
        self.type = ItemType.TEXT
        self._trunc_length = 30
        self.prefix = 'T'

    def __str__(self):
        if len(self.text) < self._trunc_length:
            return f'{self.prefix}: {self.text}'
        return f'{self.prefix}: {self.text[:self._trunc_length]}...'

    def get_data(self):
        return self.text


class ClocksData(AbstractItem):
    def __init__(self):
        super().__init__()
        self.fmt: str = None
        self.prefix = 'C'

        self.type = ItemType.CLOCK

    @staticmethod
    def now_in_fmt(fmt: str):
        return datetime.now().strftime(fmt)

    def __str__(self):
        return f'{self.prefix}: {self.now_in_fmt(self.fmt)}'

    def get_data(self):
        return self.now_in_fmt(self.fmt)


class Countdown(AbstractItem):
    def __init__(self):
        super().__init__()
        self.start: float = None
        self.end: float = None
        self.format: str = None
        self.blink_before: int = -1
        self.type = ItemType.COUNTDOWN
        self.prefix = 'D'

    # for blinking, inner counter
    blink_counter = 0

    @staticmethod
    def timestamp_to_datetime(timestamp: float, fmt: str):
        return datetime.fromtimestamp(timestamp).strftime(fmt)

    def __str__(self):
        start = self.timestamp_to_datetime(self.start, self.format)
        end = self.timestamp_to_datetime(self.end, self.format)
        if self.blink_before > -1:
            return f'{self.prefix}: {start} - {end} - blink ({self.blink_before}s)'
        return f'{self.prefix}: {start} - {end}'

    def timestamp_left(self):
        return max(int(self.end - datetime.now().timestamp()), 0)

    def get_data(self):
        left_tsp = self.timestamp_left()
        hours = int(left_tsp // 3600)
        minutes = int((left_tsp - (hours * 60)) // 60)
        seconds = int((left_tsp - (hours * 60)) % 60)

        dt = datetime(year=2000, month=1, day=1, hour=hours, minute=minutes, second=seconds)
        return dt.strftime(self.format)





