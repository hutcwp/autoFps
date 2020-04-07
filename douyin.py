# 帧率调研场景操作路径：1⃣️app启动->2⃣️5s后进入直播间->3⃣️5s后开始上下滑切直播间（每隔5s切一次，总共切5次）->4⃣️5s后进后台播放
# ->5⃣️5s后进前台播放->6⃣️5s后退直播间，接着2⃣️到6⃣️再重复二次。
from time import sleep

app_name = "抖音短视频"


def start_app(d):
    print('start_app')
    d(text=app_name).click()
    pass


def ent_live(d):
    print('ent_live')
    d(resourceId="com.ss.android.ugc.aweme:id/cj7").click()
    # d.click(80,140)
    pass


def quit_live(d):
    print('quit_live')
    d(resourceId="com.ss.android.ugc.aweme:id/a4o").click()
    pass


def swipe_live(d):
    print('swipe_live')
    # d.swipe_ext("up", box=(500, 100, 500, 1000))
    d.swipe_ext("up")
    pass


def app_background(d):
    print('app_background')
    d.press("home")
    pass


def app_foreground(d):
    print('app_foreground')
    start_app(d)
    pass


def start_fps(d):
    print('start_fps')
    start_app(d)  # 启动app
    sleep(5)

    for i in (0, 2):
        print("i -> " + str(i))
        repeat_method(d)

    pass


# 需要重复三次
def repeat_method(d):
    ent_live(d)  # 进直播间
    sleep(5)
    swipe_live(d)  # 上下滑切直播间5次
    sleep(5)
    swipe_live(d)
    sleep(5)
    swipe_live(d)
    sleep(5)
    swipe_live(d)
    sleep(5)
    swipe_live(d)
    sleep(5)
    app_background(d)  # 进入后台
    sleep(5)
    app_foreground(d)  # 进入前台
    sleep(5)
    quit_live(d)  # 退直播间
    sleep(15)


if __name__ == '__main__':
    print("抖音短视频")
