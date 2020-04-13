import uiautomator2 as u2
from time import sleep

from app import App
from log.Log import MLog

APP_NAME = "虎牙直播"


class HuYa(App):

    def __init__(self, d):
        App.__init__(self, APP_NAME, d)

    def start_app(self):
        MLog.info('start_app')
        self.d(text=self.app_name).click()
        pass

    def stop_app(self):
        MLog.info('finish app')
        self.d.app_stop('com.duowan.kiwi')
        pass

    def ent_live(self):
        MLog.info('ent_live')
        # d.xpath(
        #     '//*[@resource-id="com.duowan.kiwi:id/content"]'
        #     '/android.widget.FrameLayout[1]'
        #     '/android.widget.FrameLayout[1]'
        #     '/androidx.recyclerview.widget.RecyclerView[1]'
        #     '/android.widget.LinearLayout[1]'
        #     '/android.widget.FrameLayout[1]'
        #     '/android.widget.RelativeLayout[1]'
        #     '/android.widget.FrameLayout[1]').click()
        self.d.xpath(
            '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]'
            '/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
        pass

    def quit_live(self):
        MLog.info('quit_live')
        self.d(resourceId="com.duowan.kiwi:id/close_living_ib").click()
        pass

    def swipe_live(self):
        MLog.info('swipe_live')
        width = self.d.info['displayWidth']
        height = self.d.info['displayHeight']
        sx = width * 0.8
        sy = height * 0.2
        ex = width * 0.8
        ey = height * 0.7
        self.d.swipe(sx, sy, ex, ey, 0.1)
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
    app = HuYa(d)
    MLog.info("start test...")
    app.test_fps()
    MLog.info("finish test...")
