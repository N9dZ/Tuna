import wx

class bucky(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Frame aka window', size = (500, 400))
        panel = wx.Panel(self)
##      ---zero to 2rd
##        button = wx.Button(panel, label = "exit", pos = (123, 10), size = (70, 70))
##        self.Bind(wx.EVT_BUTTON, self.closebutton, button)
##        self.Bind(wx.EVT_CLOSE, self.closewindow)
##    def closebutton(self, event):
##        self.Close(True)
##
##    def closewindow(self, event):
##        self.Destroy()
        
##      ---3th
##        status = self.CreateStatusBar()
##        menubar = wx.MenuBar()
##        first = wx.Menu()
##        second = wx.Menu()
##        first.Append(wx.NewId(), "New Window", "This is a new window")
##        first.Append(wx.NewId(), "Open...", "This will open a new window")
##        menubar.Append(first, "File")
##        menubar.Append(second, "Edit")
##        self.SetMenuBar(menubar)
        
##      ---4th
##        box = wx.MessageDialog(None, 'Do i have the best tuts?', 'Title', wx.YES_NO)
##        answer = box.ShowModal()
##        box.Destroy()
        
##      ---5th
##        box = wx.TextEntryDialog(None, "What's your name?", "Question 1", "default text")
##        if box.ShowModal() == wx.ID_OK:
##            anwer = box.GetValue()
        
##      ---6th
##        box = wx.SingleChoiceDialog(None, 'Whats ur fav food?', 'Title', ['Tuna', 'Beef', 'Apples'])
##        if box.ShowModal() == wx.ID_OK:
##            answer = box.GetStringSelection()
        
##      ---7th
##        wx.StaticText(panel, -1, "This is static text", (10, 10))
##
##        custom = wx.StaticText(panel, -1, "This is custom", (10, 30), (260, -1), wx.ALIGN_CENTER)
##        custom.SetForegroundColour('white')
##        custom.SetBackgroundColour('blue')
        
##      ---8th
##        test = wx.TextEntryDialog(None, "Whats ur name?", 'Title', 'enter name')
##        if test.ShowModal() == wx.ID_OK:
##            apples = test.GetValue()
##
##        wx.StaticText(panel, -1, apples, (10, 10))
        
##      ---9th
##        pic = wx.Image("pig24bit.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
##        self.button = wx.BitmapButton(panel, -1, pic, pos = (10, 10))
##        self.Bind(wx.EVT_BUTTON, self.doMe, self.button)
##        self.button.SetDefault()
##
##    def doMe(self, event):
##        self.Destroy()
        
##      --10th
##        slider = wx.Slider(panel, -1, 47, 1, 100, pos = (10, 10), size = (250, -1), style = wx.SL_AUTOTICKS | wx.SL_LABELS)
##        slider.SetTickFreq(5, 1)
        
##      --11th
##        spinner = wx.SpinCtrl(panel, -1, "", (40, 40), (90, -1))
##        spinner.SetRange(1, 100)
##        spinner.SetValue(10)
        
##      --12th
##        wx.CheckBox(panel, -1, "Apples", (20, 20), (160, -1))
##        wx.CheckBox(panel, -1, "Pears", (20, 40), (160, -1))
##        wx.CheckBox(panel, -1, "Watermelon", (20, 60), (160, -1))
##        wx.CheckBox(panel, -1, "Strawberries", (20, 80), (160, -1))
        
##      --13th
##        mylist = ['beef', 'pork', 'coconuts', 'cereal']
##        cunt = wx.ListBox(panel, -1, (20, 20), (80, 60), mylist, wx.LB_SINGLE)
##        cunt.SetSelection(3)
        
##      --14th is in file '14th_EndOfTuna.py'
        
        
        
if __name__=='__main__':
    app = wx.App()
    frame = bucky(parent = None, id = -1)
    frame.Show()
    app.MainLoop()
