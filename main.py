from gui import RemoteGUI
from backend import Backend


def main():
    gui = RemoteGUI()
    interface = Backend(gui)

    gui.run()


if __name__ == '__main__':
    main()
