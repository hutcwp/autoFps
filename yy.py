# 帧率调研场景操作路径：1⃣️app启动->2⃣️5s后进入直播间->3⃣️5s后开始上下滑切直播间（每隔5s切一次，总共切5次）->4⃣️5s后进后台播放
# ->5⃣️5s后进前台播放->6⃣️5s后退直播间，接着2⃣️到6⃣️再重复二次。
import random
from time import sleep

app_name = "YY"


def get_rand_without(num, start, end):
    while True:
        n = random.randint(start, end)
        if num != n:
            return n


def start_app(d):
    print('start_app')
    d(text=app_name).click()
    pass


def ent_live(d):
    print('ent_live')
    d(resourceId="com.yy.mobile.plugin.homepage:id/living_common_container").click()
    pass


def ent_live_random(d):
    no = str(get_rand_without(-1, 1, 3))
    page = str(get_rand_without(-1, 1, 2))
    print('ent_live_random: no = ' + no + ' page=' + page)
    path = '//*[@resource-id="com.yy.mobile.plugin.homepage:id/rv_home_content"]/androidx.recyclerview.widget.RecyclerView[' + no + ']/android.widget.RelativeLayout[' + page + ']/android.widget.ImageView[1]'
    d.xpath(path).click()
    pass


def quit_live(d):
    print('quit_live')
    d(resourceId="com.yy.mobile.plugin.livebasebiz:id/btn_exit_portrait").click()
    pass


def swipe_live(d):
    print('swipe_live')
    width = d.info['displayWidth']
    height = d.info['displayHeight']
    sx = width * 0.8
    sy = height * 0.2
    ex = width * 0.8
    ey = height * 0.7
    d.swipe(sx, sy, ex, ey, 0.1)
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

    for i in (0, 1, 2):
        print("i -> " + str(i))
        repeat_method(d)

    pass


def swipe_horizontal(d):
    d(resourceId="com.duowan.mobile.entlive:id/btn_rotate_portrait").click()


def swipe_vertical(d):
    d(resourceId="com.duowan.mobile.entlive:id/btn_rotate_landscape").click()


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


# 切顶部tab
def change_top_tab(d):
    start_app(d)
    sleep(5)
    swipe_count = 15
    for i in range(1, swipe_count):
        d.swipe_ext("left")
        sleep(5)
        print("swipe left")
    for i in range(1, swipe_count):
        d.swipe_ext("right")
        sleep(5)
        print("swipe right")
    pass


# 切底部tab
def change_bottom_tab(d):
    tabs = '//*[@resource-id="android:id/tabs"]/android.widget.FrameLayout'
    start_app(d)
    sleep(5)
    cur_index = 1
    for i in range(1, 30):
        cur_index = get_rand_without(cur_index, 1, 5)
        tab_path = tabs + '[' + str(cur_index) + ']'
        d.xpath(tab_path).click()
        print('tab: ' + str(cur_index))
        sleep(5)
    pass


def swipe_up_down_homepage(d):
    start_app(d)
    sleep(5)

    width = d.info['displayWidth']
    height = d.info['displayHeight']
    sx = width * 0.8
    sy = height * 0.2
    ex = width * 0.8
    ey = height * 0.7

    for i in range(1, 15):
        d.swipe(ex, ey, sx, sy, 0.1)
        d.swipe_ext("down")
        sleep(5)

    for i in range(1, 15):
        d.swipe(sx, sy, ex, ey, 0.1)
        print('swipe up')



        sleep(5)


def swipe_up_down_live_room(d):
    # start_app(d)
    # sleep(5)
    ent_live(d)
    sleep(5)
    for i in range(1, 30):
        swipe_live(d)
        sleep(5)


def enter_quit_live(d):
    start_app(d)
    sleep(5)
    for i in range(1, 15):
        # ent_live_random(d)
        ent_live(d)
        sleep(5)
        quit_live(d)
        sleep(5)
    d.press("back")
    d.press("back")
    pass


def change_orientation(d):
    for i in range(1, 15):
        swipe_horizontal(d)
        sleep(5)
        swipe_vertical(d)
        sleep(5)


def test_start_live(d):
    d.watcher.when("下次再说").click()
    d.watcher.start()
    d.watcher.run()

    sleep(2)
    for i in range(1, 15):
        d(text="我要开播").click()
        sleep(2)

        d(text="开始直播").click()
        sleep(5)
        d(resourceId="com.yy.mobile.plugin.homepage:id/iv_close").click()
        sleep(1)
        d(text="关闭直播").click()
        sleep(2)
        d(text="返回首页").click()
        sleep(2)
        # 停止监控
        d.watcher.stop()

        # 停止并移除所有的监控，常用于初始化
        d.watcher.reset()
        pass


if __name__ == '__main__':
    print("yy")
