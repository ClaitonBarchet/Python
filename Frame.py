import wx

'''

app = wx.App()
frame = wx.Frame(None, -1, "Window Title", style = wx.MAXIMIZE_BOX |
wx.SYSTEM_MENO | wx.CAPTION)

frame.Show()

app.MainLoop()

'''

class WindowClass(wx.Frame):

    def _init_(self, parent, title):
        super(WindowClass, self)._init_(parent, title=title, size=(200,300))
        #self.Move(800,450)
        self.Show()

app = wx.App()
WindowClass(None, "Window Title")
app.MainLoop()
