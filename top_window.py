import platform

if platform.system() == 'Darwin':
    from AppKit import NSWorkspace


class TopWindow:
    def __init__(self):
        self.system = platform.system()

    def get_top_window(self):
        if self.system == 'Darwin':
            top_app_name = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
            return top_app_name
        else:
            if self.system == 'Windows':
                return ""
            else:
                if self.system == 'Linux':
                    return ""
