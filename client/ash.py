import wx
from menu import MainMenu
from toolbars import Toolbar
from panel import TunePanel
from panel import SongPanel


class MainFrame(wx.Frame):
  def __init__(self):
    wx.Frame.__init__(self,None,title="Astute Song Hunter",style=wx.DEFAULT_FRAME_STYLE)
    self.Menubar = MainMenu(self)
    self.SetMenuBar(self.Menubar)
    MainPanel = wx.Panel(self)
    self.Tools = Toolbar(self,MainPanel)
    self.Tune = TunePanel(self,MainPanel)
    self.Song = SongPanel(self,MainPanel)
    self.SetToolBar(self.Tools)
    VBox = wx.BoxSizer()
    VBox.Add(self.Tune, proportion=1, flag=wx.EXPAND|wx.ALL, border=5)
    VBox.Add(self.Song, proportion=1, flag=wx.EXPAND|wx.ALL, border=5)
    MainPanel.SetSizer(VBox)
    self.Centre()
#    self.Maximize(True)
    self.Show(True)


ASH = wx.App()
ASH_Frame = MainFrame()
ASH.MainLoop()

