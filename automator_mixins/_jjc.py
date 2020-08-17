import time

from core.cv import UIMatcher
from ._base import BaseMixin


class JJCMixin(BaseMixin):
    """
    竞技场插片
    包含日常行动相关的脚本
    """

    # 进入jjc
    def enterJJC(self, x, y):
        self.d.click(480, 505)
        time.sleep(2)
        while True:
            screen_shot_ = self.d.screenshot(format="opencv")
            if UIMatcher.img_where(screen_shot_, 'img/dixiacheng.jpg'):
                break
        self.d.click(x, y)
        time.sleep(2)
        while True:
            screen_shot_ = self.d.screenshot(format="opencv")
            self.d.click(36, 77)
            if UIMatcher.img_where(screen_shot_, 'img/list.jpg'):
                break

    # 做jjc任务
    def doJJC(self):
        # 进入jjc
        self.enterJJC(579, 411)

        # 选择第一位进入对战
        self.d.click(604, 162)
        time.sleep(1)
        # 点击战斗开始
        self.d.click(822, 456)

        while True:
            screen_shot_ = self.d.screenshot(format="opencv")
            if UIMatcher.img_where(screen_shot_, 'img/xiayibu.jpg'):
                self.d.click(803, 496)
                break
        time.sleep(1)
        self.lockimg('img/liwu.bmp', elseclick=[(131, 533)], elsedelay=1, at=(891, 413, 930, 452))  # 回首页

        # 做pjjc任务

    def doPJJC(self):
        self.enterJJC(821, 410)
        # 选择第一位进入对战
        self.d.click(604, 162)
        time.sleep(1)
        # 点击队伍2
        self.d.click(822, 456)
        time.sleep(1)
        # 点击队伍3
        self.d.click(822, 456)
        time.sleep(1)
        # 点击战斗开始
        self.d.click(822, 456)
        time.sleep(1)
        # 确保战斗开始
        self.d.click(822, 456)

        while True:
            screen_shot_ = self.d.screenshot(format="opencv")
            if UIMatcher.img_where(screen_shot_, 'img/xiayibu.jpg'):
                self.d.click(803, 506)
                break
        time.sleep(1)
        self.lockimg('img/liwu.bmp', elseclick=[(131, 533)], elsedelay=1, at=(891, 413, 930, 452))  # 回首页
