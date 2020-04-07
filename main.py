import uiautomator2 as u2

from bigo import start_fps, ent_live

d = u2.connect()  # connect to device
print(d.info)


def dumpxml(d):
    xml = d.dump_hierarchy()
    print(xml)


if __name__ == '__main__':
    print("hello world")
    # dumpxml(d)

    start_fps(d)
    # ent_live(d)

