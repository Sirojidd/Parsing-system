import ui
import processor

if __name__ == '__main__':
    processor.server.start()
    window = ui.Window()
    processor.server.stop()
