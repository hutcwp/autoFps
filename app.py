# coding:utf-8
from time import sleep


class App(object):
    app_name = ""

    def __init__(self, app_name, d):
        self.app_name = app_name
        self.d = d

    def start_app(self):
        print('start_app')
        pass

    def ent_live(self):
        print('ent_live')
        pass

    def quit_live(self):
        print('quit_live')
        pass

    def swipe_live(self):
        print('swipe_live')
        pass

    def app_background(self):
        print('app_background')
        pass

    def app_foreground(self):
        print('app_foreground')
        pass

    def test_fps(self):
        print('start_fps')
        pass
