import sys
from functools import partial
from typing import List, Union

from PyQt5.QtGui import QFont
from PyQt5.QtCore import QDateTime, QRect, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QDialog, QFileDialog, QMainWindow, QMessageBox, QLabel,
                             QColorDialog, QGraphicsDropShadowEffect)

import config
from Countdown import Ui_Dialog as CountdownUi
from RichText import Ui_Dialog as RichTextUi
from Clocks import Ui_Dialog as ClocksUi
from MainMenu import Ui_MainWindow as MainMenuUi
from Layout import Ui_MainWindow as LayoutUi
from PositionLayout import Ui_PositionLayout as PositionLayoutUi
from structures import RichText, ItemType, Countdown, ClocksData
import utils


class CustomErrorMessageBox(QMessageBox):
    def __init__(self, message: str):
        super().__init__()
        self.setIcon(QMessageBox.Critical)
        self.setWindowTitle("Error")
        self.setText(message)


class CountDownDialog(QDialog):
    def __init__(self, active_el: Countdown = None):
        super().__init__()
        self.ui = CountdownUi()
        self.ui.setupUi(self)
        self.active_el = active_el

        now = QDateTime.currentDateTime()
        self.ui.timeStart.setDateTime(now)
        self.ui.timeEnd.setDateTime(now.addSecs(3600))

        if active_el:
            self.ui.timeStart.setDateTime(QDateTime.fromSecsSinceEpoch(int(active_el.start)))
            self.ui.timeEnd.setDateTime(QDateTime.fromSecsSinceEpoch(int(active_el.end)))
            self.ui.blinkCheckBox.setChecked(active_el.is_blinked)
            self.ui.timeFormat.setText(active_el.format)

    def apply_slot(self):
        if not self.active_el:
            el = Countdown()
            el.start = self.ui.timeStart.dateTime().toPyDateTime().timestamp()
            el.end = self.ui.timeEnd.dateTime().toPyDateTime().timestamp()
            el.is_blinked = self.ui.blinkCheckBox.isChecked()
            el.format = self.ui.timeFormat.text()
            items_list.append(el)
        else:
            self.active_el.start = self.ui.timeStart.dateTime().toPyDateTime().timestamp()
            self.active_el.end = self.ui.timeEnd.dateTime().toPyDateTime().timestamp()
            self.active_el.is_blinked = self.ui.blinkCheckBox.isChecked()
            self.active_el.format = self.ui.timeFormat.text()

        self.close()


class RichTextDialog(QDialog):
    def __init__(self, active_el=None):
        super().__init__()
        self.ui = RichTextUi()
        self.ui.setupUi(self)
        self.active_el = active_el

        if active_el:
            self.ui.textEdit.setText(active_el.text)

    def apply_slot(self):
        if not self.active_el:
            text_struct = RichText()
            text_struct.text = self.ui.textEdit.toPlainText()
            items_list.append(text_struct)
        else:
            self.active_el.text = self.ui.textEdit.toPlainText()

        self.close()


class ClocksDialog(QDialog):
    def __init__(self, active_el=None):
        super().__init__()
        self.ui = ClocksUi()
        self.ui.setupUi(self)
        self.active_el = active_el

    def apply_slot(self):
        fmt = self.ui.timeFormat.text()
        clock_item = ClocksData()
        clock_item.fmt = fmt

        items_list.append(clock_item)
        self.close()


class LayoutWindow(QMainWindow):
    def __init__(self, path, error=None):
        super().__init__()
        self.ui = LayoutUi()

        self.error = error or "Can't display selected image. Choose another."

        try:
            if not len(path):
                self.error = "No selected image."
                raise BaseException

            self.setStyleSheet(f"border-image: url({path}) 0 0 0 0 stretch stretch; border-width: 0px;")
        except BaseException:
            err_m = CustomErrorMessageBox(self.error)
            err_m.exec_()
            return

        self.ui.setupUi(self)

        self.screen_w = self.geometry().width()
        self.screen_h = self.geometry().height()
        self.setWindowState(Qt.WindowFullScreen)

        self.widgets_list = []

        self._display_all_items()
        self.show()

    def _display_all_items(self):
        for index, el in enumerate(items_list):

            el_name = f'label__{index}'
            setattr(self.ui, el_name, QLabel(self.ui.centralwidget))

            widget: QLabel = getattr(self.ui, el_name)
            self.widgets_list.append(widget)

            utils.set_widget_stylesheet(
                widget,
                "background-color: rgb(243, 243, 243, 0%); border-width: 5px;"
                "color: rgb(255, 255, 255);")
            widget.setObjectName(el_name)
            widget.setText(el.get_data())

            # adjust size
            widget.adjustSize()
            self._configure_widget(el, widget)

            if el.type in [ItemType.COUNTDOWN, ItemType.CLOCK]:
                timer = QTimer(self)
                timer.timeout.connect(partial(self._update_timers, el, widget))
                timer.start(config.FREQUENCY)

    def _update_timers(self, el, widget):
        widget.setText(el.get_data())

    def _configure_widget(self, el, widget):
        w, h = widget.geometry().width(), widget.geometry().height()
        widget.setGeometry(
            QRect(round(el.ratio_x * self.screen_w),
                  round(el.ratio_y * self.screen_h), w, h))

        font = QFont()
        font.setFamily(el.font)

        if el.color:
            utils.set_widget_stylesheet(widget, f'color: {el.color}')
        if el.size:
            font.setPointSize(el.size)
        if el.is_bold:
            font.setBold(True)
        if el.is_italic:
            font.setItalic(True)
        if el.is_underline:
            font.setUnderline(True)
        if el.shadow_blur or el.shadow_offset:
            eff = QGraphicsDropShadowEffect()
            eff.setBlurRadius(el.shadow_blur)
            eff.setOffset(el.shadow_offset)
            widget.setGraphicsEffect(eff)
        if el.shadow_offset or el.shadow_blur:
            eff = QGraphicsDropShadowEffect()
            eff.setBlurRadius(el.shadow_blur)
            eff.setOffset(el.shadow_offset)
            widget.setGraphicsEffect(eff)
        widget.setFont(font)
        widget.adjustSize()

    def _update_widget_positions(self):
        """Update widget position due new screen resolution"""
        for el, w in zip(items_list, self.widgets_list):
            position = list(w.geometry().getRect())
            position[0] = round(el.ratio_x * self.screen_w)
            position[1] = round(el.ratio_y * self.screen_h)

            w.setGeometry(QRect(*position))

    def resizeEvent(self, event):
        QMainWindow.resizeEvent(self, event)

        self.screen_w = self.geometry().width()
        self.screen_h = self.geometry().height()

        self._update_widget_positions()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()


class PositionItemsWindow(QMainWindow):
    def __init__(self, path, error=None, rendered_els=None):
        super().__init__()
        self.ui = PositionLayoutUi()
        self.error = error or "Can't display selected image. Choose another."
        self.common_stylesheet = "background-color: rgb(243, 243, 243); border-width: 5px;"
        try:
            if not len(path):
                self.error = "No selected image"
                raise BaseException

            if not rendered_els:
                self.error = "Choose positioned items"
                raise BaseException

            if len(rendered_els) > 1:
                """For a while. In the future we're going to use simultaneous items positioning"""
                self.error = "Select only one item"
                raise BaseException

            self.setStyleSheet(f"border-image: url({path}) 0 0 0 0 stretch stretch; border-width: 0px;")
        except BaseException as er:
            err_m = CustomErrorMessageBox(self.error)
            err_m.exec_()
            print("Error has occurred", er)
            return

        self.ui.setupUi(self)
        im_size = utils.get_image_dimension(path)
        screen_size = QApplication.desktop().availableGeometry()

        self._screen_h = self.geometry().height()
        self._screen_w = self.geometry().width()

        ratio_max_size = utils.get_ratio_max_size(*im_size, screen_size.width(), screen_size.height())
        self.setGeometry(0, 0, *ratio_max_size)

        utils.set_widget_stylesheet(self.ui.widget, self.common_stylesheet)
        utils.set_widget_stylesheet(self.ui.fontComboBox, self.common_stylesheet)

        self.rendered_els: List[int] = rendered_els
        self.current_el = items_list[self.rendered_els[0]]
        self.current_w: QLabel = None
        self.render_items()

        self.show()

    @property
    def screen_w(self):
        val = self.geometry().width()

        if val != self._screen_w and self.current_el.ratio_x:
            position = list(self.current_w.geometry().getRect())
            position[0] = round(self.current_el.ratio_x * val)

            self.current_w.setGeometry(QRect(*position))
            self._screen_w = val

        return val

    @property
    def screen_h(self):
        val = self.geometry().height()

        if val != self._screen_h and self.current_el.ratio_y:
            position = list(self.current_w.geometry().getRect())
            position[1] = round(self.current_el.ratio_y * val)

            self.current_w.setGeometry(QRect(*position))
            self._screen_h = val

        return val

    def render_items(self):
        for index in self.rendered_els:

            el = items_list[index]
            el_name = f'label__{index}'
            setattr(self.ui, el_name, QLabel(self.ui.centralwidget))

            self.current_w = getattr(self.ui, el_name)
            utils.set_widget_stylesheet(
                self.current_w,
                "background-color: rgb(243, 243, 243, 0%); border-width: 5px;"
                "color: rgb(255, 255, 255);")
            self.current_w.setObjectName(el_name)
            self.current_w.setText(el.get_data())

            # adjust size
            self.current_w.adjustSize()

            if not self.current_el.has_changed:
                self._setup_fields_with_widget()
                self.current_el.has_changed = True
            else:
                self._restore_default_values()

    def _update_axis_spinbox_values(self):
        x1, y1, w, h = self.current_w.geometry().getRect()
        self.ui.XAxisSpinBox.setValue(x1)
        self.ui.YAxisSpinBox.setValue(y1)

    def _restore_default_values(self):
        # position
        screen_w, screen_h = self.screen_w, self.screen_h
        w, h = self.current_w.geometry().width(), self.current_w.geometry().height()
        self.current_w.setGeometry(
            QRect(round(self.current_el.ratio_x * screen_w), round(self.current_el.ratio_y * screen_h), w, h))
        # font
        font = QFont()
        try:
            if self.current_el.font:
                font.setFamily(self.current_el.font)
        except:
            err_m = CustomErrorMessageBox("Can't display default font type. Used default")
            err_m.exec_()
        if self.current_el.color:
            utils.set_widget_stylesheet(self.ui.colorBotton, f'background-color: {self.current_el.color}')
            utils.set_widget_stylesheet(self.current_w, f'color: {self.current_el.color}')
        if self.current_el.size:
            font.setPointSize(self.current_el.size)
        if self.current_el.is_bold:
            font.setBold(True)
        if self.current_el.shadow_offset or self.current_el.shadow_blur:
            eff = QGraphicsDropShadowEffect()
            eff.setBlurRadius(self.current_el.shadow_blur)
            eff.setOffset(self.current_el.shadow_offset)
            self.current_w.setGraphicsEffect(eff)
            self.ui.shadowBlurSpinBox.setValue(self.current_el.shadow_blur)
            self.ui.shadowOffsetSpinBox.setValue(self.current_el.shadow_offset)
        if self.current_el.is_italic:
            font.setItalic(True)
        if self.current_el.is_underline:
            font.setUnderline(True)
        self.current_w.setFont(font)
        self._update_font_checkboxes()
        self.ui.sizeSpinBox.setValue(self.current_w.font().pointSizeF())
        self.ui.fontComboBox.setCurrentFont(font)
        self.current_w.adjustSize()

    def _update_font_checkboxes(self):
        if self.current_el.is_underline:
            self.ui.underlineCheckBox.setChecked(True)
        if self.current_el.is_bold:
            self.ui.boldCheckBox.setChecked(True)
        if self.current_el.is_italic:
            self.ui.italicCheckBox.setChecked(True)

    def _setup_fields_with_widget(self):
        self._update_font_checkboxes()
        self.ui.shadowBlurSpinBox.setValue(self.current_el.shadow_blur)
        self.ui.shadowOffsetSpinBox.setValue(self.current_el.shadow_offset)

        font = self.current_w.font()
        font.setPointSize(self.current_el.size)
        self.current_w.setFont(font)

        self.ui.sizeSpinBox.setValue(self.current_w.font().pointSizeF())
        self.ui.centerRadioButton.setChecked(True)

        color = self.current_w.palette().button().color()
        utils.set_widget_stylesheet(self.ui.colorBotton, f'background-color: {color}')
        self.current_w.adjustSize()

        widget_geometry = self._get_widget_geometry_center()
        self.current_w.setGeometry(QRect(*widget_geometry))

        self._update_axis_spinbox_values()

    def _get_widget_geometry_center(self):
        w, h = self.current_w.geometry().width(), self.current_w.geometry().height()
        return utils.DisplayCoords.center(w, h, self.screen_w, self.screen_h)

    def center_slot(self):
        widget_geometry = self._get_widget_geometry_center()
        self.current_w.setGeometry(QRect(*widget_geometry))
        self._update_axis_spinbox_values()

    def left_up_slot(self):
        w, h = self.current_w.geometry().width(), self.current_w.geometry().height()
        geometry = utils.DisplayCoords.leftup(w, h, self.screen_w, self.screen_h)

        self.current_w.setGeometry(QRect(*geometry))
        self._update_axis_spinbox_values()

    def left_down_slot(self):
        w, h = self.current_w.geometry().width(), self.current_w.geometry().height()
        geometry = utils.DisplayCoords.leftdown(w, h, self.screen_w, self.screen_h)

        self.current_w.setGeometry(QRect(*geometry))
        self._update_axis_spinbox_values()

    def right_down_slot(self):
        w, h = self.current_w.geometry().width(), self.current_w.geometry().height()
        geometry = utils.DisplayCoords.rightdown(w, h, self.screen_w, self.screen_h)

        self.current_w.setGeometry(QRect(*geometry))
        self._update_axis_spinbox_values()

    def right_up_slot(self):
        w, h = self.current_w.geometry().width(), self.current_w.geometry().height()
        geometry = utils.DisplayCoords.rightup(w, h, self.screen_w, self.screen_h)

        self.current_w.setGeometry(QRect(*geometry))
        self._update_axis_spinbox_values()

    def _update_el_position(self):
        el_x, el_y = self.current_w.geometry().getRect()[:2]
        self.current_el.ratio_x = el_x / self.screen_w
        self.current_el.ratio_y = el_y / self.screen_h

    def update_X_axis_slot(self):
        x_cur = self.ui.XAxisSpinBox.value()
        x1, y1, w, h = self.current_w.geometry().getRect()

        geometry = x_cur, y1, w, h
        self.current_w.setGeometry(QRect(*geometry))
        self._update_el_position()

    def update_Y_axis_slot(self):
        y_cur = self.ui.YAxisSpinBox.value()
        x1, y1, w, h = self.current_w.geometry().getRect()

        geometry = x1, y_cur, w, h
        self.current_w.setGeometry(QRect(*geometry))
        self._update_el_position()

    def change_color_slot(self):
        color = QColorDialog.getColor()
        utils.set_widget_stylesheet(self.ui.colorBotton, f'background-color: {color.name()}')
        utils.set_widget_stylesheet(self.current_w, f'color: {color.name()}')
        self.current_el.color = color.name()

    def update_shadow_blur_slot(self):
        blur = self.ui.shadowBlurSpinBox.value()

        eff = QGraphicsDropShadowEffect()
        eff.setBlurRadius(blur)

        self.current_el.shadow_blur = blur
        self.current_w.setGraphicsEffect(eff)

    def update_shadow_offset_slot(self):
        offset = self.ui.shadowOffsetSpinBox.value()

        eff = QGraphicsDropShadowEffect()
        eff.setOffset(offset)

        self.current_el.shadow_offset = offset
        self.current_w.setGraphicsEffect(eff)

    def update_font_slot(self):
        font = QFont()

        is_bold = self.ui.boldCheckBox.isChecked()
        font.setBold(is_bold)
        self.current_el.is_bold = is_bold

        is_italic = self.ui.italicCheckBox.isChecked()
        font.setItalic(is_italic)
        self.current_el.is_italic = is_italic

        is_underline = self.ui.underlineCheckBox.isChecked()
        font.setUnderline(is_underline)
        self.current_el.is_underline = is_underline

        font_name = self.ui.fontComboBox.currentText()
        self.current_el.font = font_name
        font.setFamily(font_name)

        size = self.ui.sizeSpinBox.value()
        font.setPointSize(size)
        self.current_el.size = size

        self.current_w.setFont(font)
        self.current_w.adjustSize()

    def _update_widget_position(self):
        """Update widget position due new screen resolution"""

        screen_w = self.screen_w
        screen_h = self.screen_h

        position = list(self.current_w.geometry().getRect())
        position[0] = round(self.current_el.ratio_x * screen_w)
        position[1] = round(self.current_el.ratio_y * screen_h)
        self._update_axis_spinbox_values()

        self.current_w.setGeometry(QRect(*position))

    def resizeEvent(self, event):
        QMainWindow.resizeEvent(self, event)

        if self.current_el.ratio_y and self.current_el.ratio_x:
            self._update_widget_position()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()


class QMainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = MainMenuUi()
        self.ui.setupUi(self)

        self.filePath = ''

        self._update_items_list()

    def _update_items_list(self):
        self.ui.itemsList.clear()
        for item in items_list:
            self.ui.itemsList.addItem(str(item))

    def delete_item_slot(self):
        selected = self.ui.itemsList.selectedIndexes()
        indexes = reversed(sorted(list(map(lambda x: x.row(), selected))))
        for i in indexes:
            items_list.pop(i)

        self._update_items_list()

    def edit_item_slot(self):
        selected = self.ui.itemsList.selectedIndexes()
        if len(selected) > 1:
            err_m = CustomErrorMessageBox("Select only one item")
            err_m.exec_()
            return
        if not len(selected) != 0:
            err_m = CustomErrorMessageBox("Select an item")
            err_m.exec_()
            return

        i = selected[0].row()

        if items_list[i].type == ItemType.TEXT:
            element = RichTextDialog(items_list[i])
            element.show()
            element.exec_()
        elif items_list[i].type == ItemType.COUNTDOWN:
            element = CountDownDialog(items_list[i])
            element.show()
            element.exec_()

        self._update_items_list()

    def create_clocks_slot(self):
        element = ClocksDialog()
        element.show()
        element.exec_()

        self._update_items_list()

    def choose_file_slot(self):
        self.filePath, _ = QFileDialog.getOpenFileName(None, "Select the one file to open", "",
                                                       "Images (*.jpg *.bmp *.png)")
        if len(self.filePath):
            self.ui.fileLabel.setText(str(self.filePath)[:7] + '... ...' + str(self.filePath)[-15:])

    def display_layout_slot(self):
        self.layout_window = LayoutWindow(self.filePath)

    def create_text_slot(self):
        element = RichTextDialog()
        element.show()
        element.exec_()

        self._update_items_list()

    def create_countdown_slot(self):
        element = CountDownDialog()
        element.show()
        element.exec_()

        self._update_items_list()

    def position_item_slot(self):
        selected = self.ui.itemsList.selectedIndexes()
        indexes = list(map(lambda x: x.row(), selected))

        self.layout_window = PositionItemsWindow(self.filePath, rendered_els=indexes)

    def reset_image_slot(self):
        self.filePath = ""
        self.ui.fileLabel.setText("no file")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    items_list: List[Union[Countdown, RichText, ClocksData]] = []

    w = QMainMenu()
    w.show()

    sys.exit(app.exec_())

