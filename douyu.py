import uiautomator2 as u2
from time import sleep

from app import App
from log.Log import MLog

APP_NAME = "斗鱼直播"


class DouYu(App):

    def __init__(self, d):
        App.__init__(self, APP_NAME, d)

    def start_app(self):
        MLog.info('start_app')
        self.d(text=self.app_name).click()
        pass

    def stop_app(self):
        MLog.info('finish app')
        self.d.app_stop('air.tv.douyu.android')
        pass

    def ent_live(self):
        MLog.info('ent_live')
        self.d.xpath(
            '//*[@resource-id="air.tv.douyu.android:id/ku"]/android.view.ViewGroup[1]/android.widget.ImageView[1]').click()
        pass

    def quit_live(self):
        MLog.info('quit_live')
        self.d(resourceId="air.tv.douyu.android:id/cn7").click()
        pass

    def swipe_live(self):
        MLog.info('swipe_live')
        width = self.d.info['displayWidth']
        height = self.d.info['displayHeight']
        sx = width * 0.8
        sy = height * 0.2
        ex = width * 0.8
        ey = height * 0.7
        d.swipe(sx, sy, ex, ey, 0.1)
        pass

    def app_background(self):
        MLog.info('app_background')
        self.d.press("home")
        pass

    def app_foreground(self):
        MLog.info('app_foreground')
        self.start_app()
        pass

    def test_fps(self):
        MLog.info('start_fps')
        # self.start_app()  # 启动app
        # sleep(5)

        for i in range(0, 3):
            MLog.info('test repeat')
            self.ent_live()
            sleep(5)
            for j in range(0, 5):
                self.swipe_live()
                sleep(5)
            self.quit_live()
            sleep(5)
            self.app_background()
            sleep(5)
            self.app_foreground()
            sleep(5)
        self.stop_app()
        pass


if __name__ == '__main__':
    d = u2.connect()  # connect to device
    douyu = DouYu(d)
    douyu.test_fps()
