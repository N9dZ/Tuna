import wx

if __name__ == '__main__':
    app = wx.App()

    names = ['buckly', 'lucky', 'sarah', 'dustin']
    modal = wx.SingleChoiceDialog(None, "Whats ur name?", "title here", names)
    if modal.ShowModal() == wx.ID_OK:
        print "Your name is %s\n" % modal.GetStringSelection()
    modal.Destroy()
