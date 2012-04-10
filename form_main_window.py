from gi.repository import Gtk

UI_INFO = """
<ui>
  <menubar name='MenuBar'>
    <menu action='DatabaseMenu'>
      <menuitem action='DatabaseNew' />
      <menuitem action='DatabaseOpen' />
      <menuitem action='DatabaseClose' />
      <menuitem action='DatabaseSave' />
      <separator />
      <menuitem action='DatabaseQuit' />
    </menu>
    <menu action='MovieMenu'>
      <menuitem action='MovieAdd' />
      <menuitem action='MovieEdit' />
      <menuitem action='MovieRemove' />
      <menuitem action='MovieDetail' />
    </menu>
    <menu action='HelpMenu'>
      <menuitem action='About' />
      <menuitem action='Help' />
    </menu>
  </menubar>
</ui>
"""

class GptMainWindow(Gtk.Window):
    def __init__(self,translator):
        Gtk.Window.__init__(self,title=translator('AppName'))
        self.translator = translator
        self.bxWindow = Gtk.VBox(False,1)
        self.add(self.bxWindow)
        self.mbMenu = self._addMenu()
        self.bxWindow.pack_start(self.mbMenu,False,False,0)

        self.bxTop = Gtk.HBox(True,5)
        self.bxWindow.pack_start(self.bxTop,True,True,0)
        self.bxList = Gtk.VBox(False,5)
        self.bxTop.pack_start(self.bxList,True,True,5)
        self.bxButtons = Gtk.VBox(True,2)
        self.bxTop.pack_start(self.bxButtons,True,True,5)

        self.enSearch = Gtk.Entry()
        self.bxList.pack_start(self.enSearch,False,True,1)
        self.movieStore = Gtk.ListStore(str)
        self.movieRender = Gtk.CellRendererText()
        self.movieColumn = Gtk.TreeViewColumn(self.translator("MovieHeader"),self.movieRender,text=0)
        self.tvMovies = Gtk.TreeView(self.movieStore)
        self.tvMovies.append_column(self.movieColumn)
        self.bxList.pack_start(self.tvMovies,True,True,1)
        self.btnFilter = Gtk.Button(self.translator("FiltrButtonNoFiltr"))
        self.btnFilter.connect("clicked",self.on_FilterClick)
        self.bxList.pack_start(self.btnFilter,False,True,1)
        
        self.btnAdd = self._addButton("AddMovie",self.on_AddClick)
        self.btnDelete = self._addButton("RemoveMovie",self.on_DeleteClick)
        self.btnEdit = self._addButton("EditMovie",self.on_EditClick)
        self.btnDetail = self._addButton("MovieDetails",self.on_DetailClick)
        self.btnSave = self._addButton("SaveDB",self.on_SaveClick)
        self.btnQuit = self._addButton("QuitApp",self.on_QuitClick)


    def _addButton(self,strid,onclick):
        btn = Gtk.Button(self.translator(strid))
        self.bxButtons.pack_start(btn,True,True,2)
        btn.connect("clicked",onclick)
        return btn

    def _addMenu(self):
        self.agMenu = Gtk.ActionGroup('MainMenu')

        self.acDatabaseMenu = Gtk.Action('DatabaseMenu',self.translator('DatabaseMenu'),None,None)
        self.agMenu.add_action(self.acDatabaseMenu)
        self.acDatabaseNew = Gtk.Action('DatabaseNew',self.translator('NewDB'),None,Gtk.STOCK_NEW)
        self.agMenu.add_action(self.acDatabaseNew)
        self.acDatabaseOpen = Gtk.Action('DatabaseOpen',self.translator('OpenDB'),None,None)
        self.agMenu.add_action(self.acDatabaseOpen)
        self.acDatabaseClose = Gtk.Action('DatabaseClose',self.translator('CloseDB'),None,None)
        self.agMenu.add_action(self.acDatabaseClose)
        self.acDatabaseSave = Gtk.Action('DatabaseSave',self.translator('SaveDB'),None,None)
        self.agMenu.add_action(self.acDatabaseSave)
        self.acDatabaseQuit = Gtk.Action('DatabaseQuit',self.translator('QuitApp'),None,Gtk.STOCK_QUIT)
        self.agMenu.add_action(self.acDatabaseQuit)

        self.acMovieMenu = Gtk.Action('MovieMenu',self.translator('MovieMenu'),None,None)
        self.agMenu.add_action(self.acMovieMenu)
        self.acMovieAdd = Gtk.Action('MovieAdd',self.translator('AddMovie'),None,Gtk.STOCK_ADD)
        self.agMenu.add_action(self.acMovieAdd)
        self.acMovieEdit = Gtk.Action('MovieEdit',self.translator('EditMovie'),None,Gtk.STOCK_EDIT)
        self.agMenu.add_action(self.acMovieEdit)
        self.acMovieRemove = Gtk.Action('MovieRemove',self.translator('RemoveMovie'),None,Gtk.STOCK_REMOVE)
        self.agMenu.add_action(self.acMovieRemove)
        self.acMovieDetail = Gtk.Action('MovieDetail',self.translator('MovieDetails'),None,None)
        self.agMenu.add_action(self.acMovieDetail)
        self.acHelpMenu = Gtk.Action('HelpMenu',self.translator('HelpMenu'),None,None)
        self.agMenu.add_action(self.acHelpMenu)
        self.acAbout = Gtk.Action('About',self.translator('About'),None,Gtk.STOCK_ABOUT)
        self.agMenu.add_action(self.acAbout)
        self.acHelp = Gtk.Action('Help',self.translator('Help'),None,Gtk.STOCK_HELP)
        self.agMenu.add_action(self.acHelp)

        
        self.uimanager = Gtk.UIManager()
        self.uimanager.add_ui_from_string(UI_INFO)
        self.add_accel_group(self.uimanager.get_accel_group())
        self.uimanager.insert_action_group(self.agMenu)

        return self.uimanager.get_widget("/MenuBar")

    def on_AddClick(self,widget):
        # TO-DO Handling
        pass

    def on_DeleteClick(self,widget):
        # TO-DO Handling
        pass

    def on_EditClick(self,widget):
        # TO-DO Handling
        pass

    def on_DetailClick(self,widget):
        # TO-DO Handling
        pass

    def on_SaveClick(self,widget):
        # TO-DO Handling
        pass

    def on_QuitClick(self,widget):
        # TO-DO Handling
        Gtk.main_quit()

    def on_FilterClick(self,widget):
        # TO-DO Handling
        pass
