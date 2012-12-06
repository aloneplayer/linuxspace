import wx 

class MyApp(wx.App):  

    def OnInit(self):  
       frame = MyFrame("wxMenu Demo", (50, 60), (450, 340))  
       frame.Show()  
       self.SetTopWindow(frame)  
       return True  



class MyFrame(wx.Frame):  
    def __init__(self, title, pos, size):  
        wx.Frame.__init__(self, None, -1, title, pos, size)  

        # create file menu  
        menuFile = wx.Menu()  
        # add file menu items
        menuFile.Append(1, "&About...")  
        menuFile.AppendSeparator()  
        menuFile.Append(2, "E&xit")          


        # create exit menu  
        menuExit = wx.Menu()
        # add exit menu items
        menuExit.Append(3,"E&xit")  


        # create menubar and add menus
        menuBar = wx.MenuBar()  
        menuBar.Append(menuFile, "&File")  
        menuBar.Append(menuExit, "&Exit")  

        self.SetMenuBar(menuBar)  
        self.CreateStatusBar()  
        self.SetStatusText("Welcome to wxPython!")  

        # add events  
        self.Bind(wx.EVT_MENU, self.OnAbout, id=1)  
        self.Bind(wx.EVT_MENU, self.OnQuit, id=2)  
        self.Bind(wx.EVT_MENU, self.OnQuit, id=3)  

    def OnQuit(self, event):  
        self.Close()  

    def OnAbout(self, event):  
        wx.MessageBox("This is a wxPython Hello world sample",   
                "About Hello World", wx.OK | wx.ICON_INFORMATION, self)  

if __name__ == '__main__':  

    app = MyApp(False)  
    app.MainLoop()  
