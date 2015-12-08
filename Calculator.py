import wx

class displaynumber(wx.Frame):
    
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'This a calculator', size = (250, 400))
        panel = wx.Panel(self)
        numlist = ["<--", "CE", "C", "+", "-",
                "7", "8", "9", "/", "%",
                "4", "5", "6", "*", "1/X",
                "1", "2", "3", "-", "=",
                "0", ".", "+"]
        # use a for-loop to display buttons
        for i in range(len(numlist)):
            # 'a' means which line is the button in
            a = i%5
            # 'b' means which row is the button in
            b = i/5
            # Four special conditions
            if i == 19:
                button = wx.Button(panel, label = numlist[19], pos = (10 + 45 * a, 150 + 40 * b), size = (35, 70))
            if i == 20:
                button = wx.Button(panel, label = numlist[20], pos = (10 + 45 * a, 150 + 40 * b), size = (80, 30))
            if i == 21:
                button = wx.Button(panel, label = numlist[21], pos = (10 + 45 * 2, 150 + 40 * b), size = (35, 30))
            if i == 22:
                button = wx.Button(panel, label = numlist[22], pos = (10 + 45 * 3, 150 + 40 * b), size = (35, 30))
            # use one-line code to show other 19 buttons
            button = wx.Button(panel, label = numlist[i], pos = (10 + 45 * a, 150 + 40 * b), size = (35, 30))
        # # 1st line a = i%5, which line
        # #button = wx.Button(panel, label = numlist[i], pos = (10, 150), size = (35, 30))
        # button = wx.Button(panel, label = numlist[0], pos = (10, 150), size = (35, 30))
        # button = wx.Button(panel, label = numlist[1], pos = (10+45, 150), size = (35, 30))
        # button = wx.Button(panel, label = numlist[2], pos = (10+45*2, 150), size = (35, 30))
        # button = wx.Button(panel, label = numlist[3], pos = (10+45*3, 150), size = (35, 30))
        # button = wx.Button(panel, label = numlist[4], pos = (10+45*4, 150), size = (35, 30))
        # # 2nd line b = i/5, which row
        # button = wx.Button(panel, label = numlist[5], pos = (10, 150+40), size = (35, 30))
        # button = wx.Button(panel, label = numlist[6], pos = (10+45, 150+40), size = (35, 30))
        # button = wx.Button(panel, label = numlist[7], pos = (10+45*2, 150+40), size = (35, 30))
        # button = wx.Button(panel, label = numlist[8], pos = (10+45*3, 150+40), size = (35, 30))
        # button = wx.Button(panel, label = numlist[9], pos = (10+45*4, 150+40), size = (35, 30))
        # # 3rd line
        # button = wx.Button(panel, label = numlist[10], pos = (10, 150+40*2), size = (35, 30))
        # button = wx.Button(panel, label = numlist[11], pos = (10+45, 150+40*2), size = (35, 30))
        # button = wx.Button(panel, label = numlist[12], pos = (10+45*2, 150+40*2), size = (35, 30))
        # button = wx.Button(panel, label = numlist[13], pos = (10+45*3, 150+40*2), size = (35, 30))
        # button = wx.Button(panel, label = numlist[14], pos = (10+45*4, 150+40*2), size = (35, 30))
        # # 4th line
        # button = wx.Button(panel, label = numlist[15], pos = (10, 150+40*3), size = (35, 30))
        # button = wx.Button(panel, label = numlist[16], pos = (10+45, 150+40*3), size = (35, 30))
        # button = wx.Button(panel, label = numlist[17], pos = (10+45*2, 150+40*3), size = (35, 30))
        # button = wx.Button(panel, label = numlist[18], pos = (10+45*3, 150+40*3), size = (35, 30))
        # button = wx.Button(panel, label = numlist[19], pos = (10+45*4, 150+40*3), size = (35, 70))
        # # 5th line
        # button = wx.Button(panel, label = numlist[20], pos = (10, 150+40*4), size = (80, 30))
        # button = wx.Button(panel, label = numlist[21], pos = (10+45*2, 150+40*4), size = (35, 30))
        # button = wx.Button(panel, label = numlist[22], pos = (10+45*3, 150+40*4), size = (35, 30))

if __name__=='__main__':
    app = wx.App()
    frame = displaynumber(parent = None, id = -1)
    frame.Show()
    app.MainLoop()
