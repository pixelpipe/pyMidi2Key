import platform

if platform.system() == 'Darwin':
    from AppKit import NSWorkspace

class TopWindow:
    def __init__(self):
        self.system = platform.system()

    def getTopWindow(self):
        if self.system == 'Darwin':
            topAppName =  NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
            return topAppName
        else:
            if self.system == 'Windows':
                return ""
            else:
                if self.system == 'Linux':
                    return ""