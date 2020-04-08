import uiautomator2 as u2

# from yy import start_fps
# from bigo import start_fps
# from bigo import start_fps

d = u2.connect()  # connect to device
print(d.info)


def dumpxml(d):
    xml = d.dump_hierarchy()
    print(xml)


if __name__ == '__main__':
    print("start test ..."
          ""
          "")
    # dumpxml(d)

    # start_fps(d)

    print("end test ...")
