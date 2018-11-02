from PIL import Image


def get_image_dimension(path) -> (int, int):
    image = Image.open(path)
    return image.size


def get_ratio_max_size(iwidth, iheight, swidth, sheight) -> (int, int):
    KOEF = 1
    new_iw = iwidth
    new_ih = iheight

    swidth_new = swidth * KOEF
    sheight_new = sheight * KOEF

    height_k = iheight/sheight_new
    width_k = iwidth/swidth_new

    if max(height_k, width_k) > 1:
        if height_k > width_k:
            new_iw /= height_k
            new_ih /= height_k
        else:
            new_iw /= width_k
            new_ih /= width_k

    print('Appropriate size:', new_iw, new_ih)

    return new_iw, new_ih


def set_widget_stylesheet(widget, styles: str = ""):
    """Hack that should be eliminated further"""
    widget.setStyleSheet(f"border-image: url() 0 0 0 0 stretch stretch; " + styles)


class DisplayCoords:
    THRESHOLD = 0.1

    @staticmethod
    def center(widget_w, widget_h, wind_w, wind_h):
        return round(wind_w/2-widget_w/2), round(wind_h/2-widget_h/2), widget_w, widget_h

    @classmethod
    def leftup(cls, widget_w, widget_h, wind_w, wind_h):
        return (wind_w - widget_w) * cls.THRESHOLD, (wind_h - widget_h) * cls.THRESHOLD, widget_w, widget_h

    @classmethod
    def leftdown(cls, widget_w, widget_h, wind_w, wind_h):
        return (wind_w - widget_w) * cls.THRESHOLD, (wind_h - widget_h) * (1 - cls.THRESHOLD), widget_w, widget_h

    @classmethod
    def rightup(cls, widget_w, widget_h, wind_w, wind_h):
        return (wind_w - widget_w) * (1 - cls.THRESHOLD), (wind_h - widget_h) * cls.THRESHOLD, widget_w, widget_h

    @classmethod
    def rightdown(cls, widget_w, widget_h, wind_w, wind_h):
        return (wind_w - widget_w) * (1 - cls.THRESHOLD), (wind_h - widget_h) * (1 - cls.THRESHOLD), widget_w, widget_h


