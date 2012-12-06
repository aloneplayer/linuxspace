#!/usr/bin/python
# -*- coding: utf-8 -*-

# gotoclass.py

import wx

class Example(wx.Frame):
  
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, 
            size=(390, 350))
            
        self.InitUI()
        self.Centre()
        self.Show()     
        
    def InitUI(self):
    
        panel = wx.Panel(self)
        #The main content sizer
        contentSizer = wx.BoxSizer(wx.VERTICAL)

        #First line
        classNameSizer = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label='Class Name')
        tc = wx.TextCtrl(panel)
        classNameSizer.Add(st1, flag=wx.RIGHT, border=8)
        classNameSizer.Add(tc, proportion=1)
        contentSizer.Add(classNameSizer, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        contentSizer.Add((-1, 10))

        matchingClassesSizer = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(panel, label='Matching Classes')
        matchingClassesSizer.Add(st2)
        contentSizer.Add(matchingClassesSizer, flag=wx.LEFT | wx.TOP, border=10)

        contentSizer.Add((10, 10),)

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        tc2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        hbox3.Add(tc2, proportion=1, flag=wx.EXPAND)
        contentSizer.Add(hbox3, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, 
            border=10)

        contentSizer.Add((-1, 25))

        checkBoxesSizer = wx.BoxSizer(wx.HORIZONTAL)
        cb1 = wx.CheckBox(panel, label='Case Sensitive')
        cb2 = wx.CheckBox(panel, label='Nested Classes')
        cb3 = wx.CheckBox(panel, label='Non-Project classes')
        checkBoxesSizer.Add(cb1)
        checkBoxesSizer.Add(cb2, flag=wx.LEFT, border=10)
        checkBoxesSizer.Add(cb3, flag=wx.LEFT, border=10)
        contentSizer.Add(checkBoxesSizer, flag=wx.LEFT, border=10)

        contentSizer.Add((-1, 25))

        buttonsSizer = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(panel, label='Ok', size=(70, 30))
        btn2 = wx.Button(panel, label='Close', size=(70, 30))
        buttonsSizer.Add(btn1)
        buttonsSizer.Add(btn2, flag=wx.LEFT|wx.BOTTOM, border=5)
        contentSizer.Add(buttonsSizer, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)

        panel.SetSizer(contentSizer)


if __name__ == '__main__':
  
    app = wx.App()
    Example(None, title='Go To Class')
    app.MainLoop()
