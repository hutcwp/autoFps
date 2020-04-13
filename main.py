import uiautomator2 as u2

# from yy import start_fps
# from bigo import start_fps
# from bigo import start_fps
from yy import change_top_tab, change_bottom_tab, enter_quit_live, swipe_up_down_live_room, change_orientation, \
    test_start_live

d = u2.connect()  # connect to device
print(d.info)


def dumpxml(d):
    xml = d.dump_hierarchy()
    print(xml)


if __name__ == '__main__':
    print("start test ...")
    # dumpxml(d)

    # start_fps(d)

    # change_top_tab(d)

    # change_bottom_tab(d)

    # swipe_up_down_live_room(d)

    enter_quit_live(d)

    # swipe_up_down_live_room(d)

    # change_orientation(d)

    # test_start_live(d)

    print("end test ...")
