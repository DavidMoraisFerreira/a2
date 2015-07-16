'''
Created on Mar 6, 2015

@author: eRiC

# create header edit controls
def editctrl(nfoDict, keyName, typ, parent, editCtrls):
    if keyName not in nfoDict:
        return
    
    label = QtGui.QLabel('%s:' % keyName)
    parent.addWidget(label)
    if typ == 'text':
        inputctrl = QtGui.QPlainTextEdit()
        inputctrl.setPlainText(nfoDict.get(keyName) or '')
        inputctrl.setTabChangesFocus(True)
    else:
        inputctrl = QtGui.QLineEdit()
        inputctrl.setText(nfoDict.get(keyName) or '')
    parent.addWidget(inputctrl)
    editCtrls[keyName] = inputctrl

nfo item is always the 0th entry in the config.json it just draws and holds all
the author, name, version, description info
'''

from PySide import QtGui, QtCore
from functools import partial
import subprocess
from os.path import join
from hotkey_edit_ui import Ui_hotkey_edit
import inspect
import logging
logging.basicConfig()
log = logging.getLogger('a2ctrl')
log.setLevel(logging.DEBUG)
margin = 5
labelW = 100


def draw(cfg, mod):
    """
    mapper that returns display control objects
    according to the 'typ' of a config element
    """
    if cfg['typ'] == 'nfo':
        return DrawNfo(cfg)
    elif cfg['typ'] == 'check':
        return DrawCheck(cfg)
    elif cfg['typ'] == 'hotkey':
        return DrawHotkey(cfg, mod)


class DrawWelcome(QtGui.QWidget):
    'Hello user! Welcome to a2! This is a template introduction Text. So far there is not much to say. I just wanted this to fill up more than one line properly. Voila!'


class DrawNfo(QtGui.QWidget):
    def __init__(self, data):
        super(DrawNfo, self).__init__()
        self.layout = QtGui.QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.label = QtGui.QLabel(self)
        self.label.setText(data.get('description') or '')
        self.label.setWordWrap(True)
        self.layout.addWidget(self.label)


class DrawCheck(QtGui.QWidget):
    def __init__(self, data):
        super(DrawCheck, self).__init__()
        self.layout = QtGui.QVBoxLayout(self)


class DrawHotkey(QtGui.QWidget):
    """
    User ui for a Hotkey control.
    shows: label, checkbox if disablable, shortcut(s), controls to add, remove
        additional shortcuts, controls to change scope if that's enabled...
    
    cfg['label'] == 'Hotkeytest with a MsgBox'
    cfg['typ'] == 'hotkey':
    cfg['name'] == 'modnameHotkey1'
    cfg['enabled'] = True
    cfg['disablable'] = True
    cfg['key'] = 'Win+G'
    cfg['keyChange'] = True
    cfg['multiple'] = True
    cfg['scope'] = ''
    cfg['scopeChange'] = True
    # mode can be: ahk, file, key: to execute code, open up sth, send keystroke
    cfg['mode'] = 'ahk'
    """
    def __init__(self, cfg, mod):
        super(DrawHotkey, self).__init__()
        self.cfg = cfg
        self.mod = mod
        self._setupUi()
    
    def _setupUi(self):
        userCfg = self.mod.db.getd(self.cfg['name'], self.mod.name)
        self.ctrllayout = QtGui.QHBoxLayout(self)
        # left, top, right, bottom
        self.ctrllayout.setContentsMargins(0, 0, 0, 0)
        self.labelBoxLayout = QtGui.QVBoxLayout()
        self.labelBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.labelLayout = QtGui.QHBoxLayout()
        if self.cfg['disablable']:
            state = self.mod.getCfgValue(self.cfg, userCfg, 'enabled')
            self.check = QtGui.QCheckBox(self)
            self.check.setMinimumSize(QtCore.QSize(25, 25))
            self.check.setMaximumSize(QtCore.QSize(25, 25))
            self.check.setChecked(state)
            self.check.clicked.connect(self.hotkeyCheck)
            self.labelLayout.addWidget(self.check)
        self.label = QtGui.QLabel(self.cfg.get('label') or '', self)
        self.label.setWordWrap(True)
        self.label.setMinimumSize(QtCore.QSize(16777215, 35))
        self.labelLayout.addWidget(self.label)
        self.labelBoxLayout.addLayout(self.labelLayout)
        self.labelBoxLayout.addItem(QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum,
                                                      QtGui.QSizePolicy.Expanding))
        self.ctrllayout.addLayout(self.labelBoxLayout)
        
        self.hotkeyListLayout = QtGui.QVBoxLayout()
        self.hotkeyLayout = QtGui.QHBoxLayout()
        #self.hotkeyButton = QtGui.QPushButton(self.data.get('key') or '')
        self.hotkeyButton = HotKey(self.mod.getCfgValue(self.cfg, userCfg, 'key'),
                                   self.hotkeyChange)
        self.hotkeyButton.setMinimumSize(QtCore.QSize(100, 35))
        self.hotkeyOption = QtGui.QPushButton()
        self.hotkeyOption.setMaximumSize(QtCore.QSize(35, 35))
        self.hotkeyOption.setMinimumSize(QtCore.QSize(35, 35))
        self.hotkeyOption.setFlat(True)
        self.hotkeyOption.setText('...')
        self.hotkeyLayout.addWidget(self.hotkeyButton)
        self.hotkeyLayout.addWidget(self.hotkeyOption)
        self.hotkeyButton.setEnabled(self.cfg['keyChange'])
        
#         self.hotkeyLayout.addItem(QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding,
#                                                     QtGui.QSizePolicy.Minimum))
        self.hotkeyListLayout.addLayout(self.hotkeyLayout)
        self.hotkeyListLayout.addItem(QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum,
                                                        QtGui.QSizePolicy.Expanding))
        self.ctrllayout.addLayout(self.hotkeyListLayout)
        self.ctrllayout.setStretch(2, 1)
        self.setLayout(self.ctrllayout)
        
    def hotkeyCheck(self):
        # setUserCfg: subcfg, attributeName, value, ctrlName
        state = self.check.isChecked()
        self.mod.setUserCfg(self.cfg, 'enabled', state)
        self.mod.change()
#         self.cfg['enabled']
#         hkUserCfg = self.mod.db.gets(self.cfg['name'])
#         print('hkUserCfg: %s' % str(hkUserCfg))
    
    def hotkeyChange(self, newKey):
        log.info('cfg key: %s' % self.cfg['key'])
        log.info('newKey: %s' % newKey)
        self.mod.setUserCfg(self.cfg, 'key', newKey)
        self.mod.change()


def edit(cfg, mod, main):
    if cfg['typ'] == 'nfo':
        return EditNfo(cfg)
    elif cfg['typ'] == 'include':
        return EditInclude(cfg, mod, main)
    elif cfg['typ'] == 'hotkey':
        return EditHotkey(cfg, mod, main)


class EditNfo(QtGui.QGroupBox):
    def __init__(self, data):
        super(EditNfo, self).__init__()
        self.setStyleSheet("QGroupBox {font: 10pt};")
        
        self.data = data
        self.typ = data['typ']
        self.setTitle('module information:')
        self.setSizePolicy(QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,
                                             QtGui.QSizePolicy.Maximum))
        self.layout = QtGui.QVBoxLayout(self)
        self.layout.setSpacing(5)
        self.layout.setContentsMargins(5, 5, 5, 5)
        self.description = EditText('description', data.get('description'), self.layout, self.getCfg)
        self.author = EditLine('author', data.get('author'), self.layout, self.getCfg)
        self.version = EditLine('version', data.get('version'), self.layout, self.getCfg)
        self.date = EditLine('date', data.get('date'), self.layout, self.getCfg)

    def getCfg(self):
        self.data['description'] = self.description.value
        self.data['author'] = self.author.value
        self.data['version'] = self.version.value
        self.data['date'] = self.date.value
        return self.data


class EditCtrl(QtGui.QWidget):
    """
    frame widget for an edit control which enables basic arrangement of the
    control up & down as well as deleting the control.
    
    It's made to work with handwritten and compiled Uis right away.
    To embedd a compiled ui tell it so addLayout=False in the super()-statement:
        super(MyNewCtrl, self).__init__(addLayout=False)
    state the mainWidget in setupUi:
        self.ui.setupUi(self.mainWidget)
    and then set the self.mainWidget-layout to your top layout in the compiled ui:
        self.mainWidget.setLayout(self.ui.mytoplayout)
    
    TODO: currently this is embedded as menuitems on a button which is pretty shitty.
        I'd like to have some actual up/down buttons and an x to indicate delete
        functionality
    """
    def __init__(self, cfg, main, addLayout=True):
        super(EditCtrl, self).__init__()
        self.cfg = cfg
        self.main = main
        self._setupUi(addLayout)
        self._getCfgList = []
    
    def delete(self):
        if self.cfg in self.main.tempConfig:
            self.main.tempConfig.remove(self.cfg)
            self.main.editMod()
    
    def move(self, value):
        index = self.main.tempConfig.index(self.cfg)
        newindex = index + value
        if newindex < 1 or newindex >= len(self.main.tempConfig):
            return

        cfg = self.main.tempConfig.pop(index)
        self.main.tempConfig.insert(newindex, cfg)
        self.main.editMod()

    def _setupUi(self, addLayout):
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self._ctrlLayout = QtGui.QHBoxLayout(self)
        self._ctrlLayout.setSpacing(0)
        self._ctrlLayout.setContentsMargins(0, 0, 0, 0)
        self.mainWidget = QtGui.QWidget(self)
        if addLayout:
            self.mainLayout = QtGui.QVBoxLayout()
            self.mainLayout.setContentsMargins(5, 5, 5, 5)
            self.mainWidget.setLayout(self.mainLayout)
        self._ctrlLayout.addWidget(self.mainWidget)
        
        self._ctrlButtonLayout = QtGui.QVBoxLayout()
        self._ctrlButtonLayout.setSpacing(0)
        self._ctrlButtonLayout.setContentsMargins(5, 0, 0, 0)
        self._ctrlButtonLayout.setObjectName("ctrlButtonLayout")
        
        self._ctrlButton = QtGui.QPushButton(self)
        self._ctrlButton.setMaximumSize(QtCore.QSize(50, 50))
        self._ctrlButton.setText("...")
        self._ctrlButton.setObjectName("ctrlButton")
        self._ctrlButtonLayout.addWidget(self._ctrlButton)
        spacerItem = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum,
                                       QtGui.QSizePolicy.Expanding)
        self._ctrlButtonLayout.addItem(spacerItem)
        self._ctrlLayout.addLayout(self._ctrlButtonLayout)
        self._ctrlLayout.setStretch(0, 1)
        
        self._ctrlMenu = QtGui.QMenu(self)
        self._ctrlButton.setMenu(self._ctrlMenu)
        
        for item in [('up', partial(self.move, -1)),
                     ('down', partial(self.move, 1)),
                     ('delete', self.delete)]:
            action = QtGui.QAction(self._ctrlMenu)
            action.setText(item[0])
            action.triggered.connect(item[1])
            self._ctrlMenu.addAction(action)
    
    def getCtrlData(self):
        for ctrl in self._getCfgList:
            self.cfg[ctrl[0]] = ctrl[1]()
    
    def getCfg(self):
        self.getCtrlData()
        return self.cfg

    def enlistCfgCtrls(self, uiclass):
        """
        already deprecated. You'd have to connect the widgets to the getCfg method
        anyways and then fetch them there in again...
        
        just for historic reasons...
        browses a given widget class members and according to their type adds
        them to the _getCfgList which is then looped by getCfg on change.
        To have a widget listed its name MUST start with 'cfg_'
        The string after that will be the name of the data piece in the element
        dictionary. So
            self.ui.cfg_bananas = QtGui.QCheckBox()
        will end up as ('bananas', self.ui.cfg_bananas.isChecked) in the list so
        it can be called to get the value and set in the dict.
        just if like you wrote
            self.cfg['bananas'] = self.ui.cfg_bananas.isChecked()
        """
        self._getCfgList = []
        for ctrl in inspect.getmembers(uiclass):
            if ctrl[0].startswith('cfg_'):
                name = ctrl[0][4:]
                #log.info('ctrl: %s' % str(ctrl))
                if isinstance(ctrl[1], QtGui.QCheckBox):
                    self._getCfgList.append((name, ctrl[1].isChecked))
                    if name in self.cfg:
                        ctrl[1].setChecked(self.cfg[name])
            #log.info('e.__name__: %s' % e.__name__)
    
    def connectCfgCtrls(self, uiclass):
        for ctrl in inspect.getmembers(uiclass):
            if not ctrl[0].startswith('cfg_'):
                continue
            
            name = ctrl[0][4:]
            control = ctrl[1]
            
            if isinstance(control, QtGui.QCheckBox):
                # checkBox doesn't send state, so we put the func to check
                control.clicked.connect(partial(self._updateCfgData,
                                                name, control.isChecked))
                # set ctrl according to config or set config from ctrl
                if name in self.cfg:
                    control.setChecked(self.cfg[name])
                else:
                    self.cfg[name] = control.isChecked()
            
            elif isinstance(control, QtGui.QLineEdit):
                control.textChanged.connect(partial(self._updateCfgData, name, None))
                if name in self.cfg:
                    control.setText(self.cfg[name])
                else:
                    self.cfg[name] = control.text()
            
            elif isinstance(control, QtGui.QComboBox):
                control.currentIndexChanged.connect(partial(self._updateCfgData, name, None))
                if name in self.cfg:
                    control.setCurrentIndex(self.cfg[name])
                else:
                    self.cfg[name] = control.currentIndex()

            else:
                log.error('Cannot handle widget "%s"!\n  type "%s" NOT covered yet!' %
                          (ctrl[0], type(control)))
    
    def _updateCfgData(self, name, func, data=None, *args):
        #print('widget sent data: %s' % str(args))
        if data is not None:
            self.cfg[name] = data
        elif func is not None:
            self.cfg[name] = func()


class EditLine(QtGui.QWidget):
    def __init__(self, name, text, parentLayout=None, updatefunc=None):
        super(EditLine, self).__init__()
        self.name = name
        self.updatefunc = updatefunc
        self.parentLayout = parentLayout
        self.layout = QtGui.QHBoxLayout(self)
        self.layout.setSpacing(5)
        self.layout.setContentsMargins(margin, margin, margin, margin)
        self.labelCtrl = QtGui.QLabel('%s:' % name)
        self.labelCtrl.setMinimumSize(QtCore.QSize(labelW, 0))
        self.layout.addWidget(self.labelCtrl)
        self.inputCtrl = QtGui.QLineEdit()
        self.inputCtrl.setText(str(text))
        self.inputCtrl.textChanged.connect(self.update)
        self.layout.addWidget(self.inputCtrl)
        if parentLayout:
            parentLayout.addWidget(self)
    
    def update(self):
        if self.updatefunc:
            self.updatefunc()
    
    @property
    def value(self):
        return self.inputCtrl.text()


class EditText(QtGui.QWidget):
    def __init__(self, name, text, parent=None, updatefunc=None):
        super(EditText, self).__init__()
        self.name = name
        self.parent = parent
        self.updatefunc = updatefunc
        self.baselayout = QtGui.QVBoxLayout(self)
        self.baselayout.setSpacing(5)
        self.baselayout.setContentsMargins(margin, margin, margin, margin)
        self.labelCtrl = QtGui.QLabel('%s:' % name)
        self.baselayout.addWidget(self.labelCtrl)
        self.inputCtrl = QtGui.QPlainTextEdit()
        self.inputCtrl.setPlainText(str(text))
        self.inputCtrl.setTabChangesFocus(True)
        self.inputCtrl.setMaximumSize(QtCore.QSize(16777215, 100))
        self.inputCtrl.textChanged.connect(self.update)
        self.baselayout.addWidget(self.inputCtrl)
        if parent:
            parent.addWidget(self)
    
    def update(self):
        if self.updatefunc:
            self.updatefunc()
    
    @property
    def value(self):
        return self.inputCtrl.toPlainText()


class EditAddElem(QtGui.QWidget):
    """
    to add a control to a module setup. This will probably go into some popup
    later. This way its a little too clunky I think.
    
    TODO: the popup will show all available scripts to include in a sub menu
        * include > script1.ahk
                    script2.ahk
                    create new script
        * hotkey
        * checkBox
        * ...
    
    til: if you don't make this a widget and just a object Qt will forget about
    any connections you make!
    """
    def __init__(self, mod, tempConfig, rebuildFunc):
        super(EditAddElem, self).__init__()
        self.tempConfig = tempConfig
        self.rebuildFunc = rebuildFunc
        self.mod = mod
        self.baselayout = QtGui.QHBoxLayout(self)
        self.baselayout.setSpacing(5)
        self.baselayout.setContentsMargins(margin, margin, margin, margin)
        
        self.addButton = QtGui.QPushButton('add')
        self.baselayout.addWidget(self.addButton)
        
        self.menu = QtGui.QMenu(self.addButton)
        self.menu.aboutToShow.connect(self.populateMenu)
        self.addButton.setMenu(self.menu)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.baselayout.addItem(spacerItem)

    def populateMenu(self):
        self.menu.clear()
        self.menu_include = self.menu.addMenu('include')
        scriptsInUse = set()
        for cfg in self.tempConfig:
            if cfg['typ'] == 'include':
                scriptsInUse.add(cfg['file'])
        scriptsUnused = set(self.mod.scripts) - scriptsInUse
        for scriptName in scriptsUnused:
            action = QtGui.QAction(self.menu_include)
            action.setText(scriptName)
            action.triggered.connect(partial(self.newInclude, scriptName))
            self.menu_include.addAction(action)
        
        newIncludeAction = QtGui.QAction(self.menu_include)
        newIncludeAction.setText('create new')
        newIncludeAction.triggered.connect(self.newInclude)
        self.menu_include.addAction(newIncludeAction)
        
        for el in 'checkBox hotkey groupBox textField floatField intField '\
                  'fileField text button comboBox'.split():
            action = QtGui.QAction(self.menu)
            action.setText(el)
            action.triggered.connect(partial(self.addCtrl, el))
            self.menu.addAction(action)
    
    def newInclude(self, name=''):
        if not name:
            name = self.mod.createScript()
            if not name:
                return
        log.info('including: %s' % name)
        self.addCtrl('include', name)
    
    def addCtrl(self, typ, name=''):
        """
        TODO: I guess we should put the configuration of the element rather to the
        very class that builds it instead of writing it all in this wrapper thingy
        here. Maybe there could be a class method that adds to the tempConfig...
        """
        cfg = {'typ': typ}
        if cfg['typ'] == 'include':
            cfg['file'] = name
        elif cfg['typ'] == 'hotkey':
            cfg['enabled'] = True
            cfg['disablable'] = True
            cfg['key'] = 'Win+G'
            cfg['keyChange'] = True
            cfg['multiple'] = True
            cfg['scope'] = ''
            cfg['scopeChange'] = True
            # mode can be: ahk, file, key
            # to execute code, open up sth, send keystroke
            cfg['mode'] = 'ahk'
        
        self.tempConfig.append(cfg)
        self.rebuildFunc()


class EditInclude(EditCtrl):
    """
    TODO: An Include control has to know what can be included. Plus a
    'create script' item. If a file was included already then a new
    Include control won't show that script file. If there are no more
    scripts to include it will only show the 'create script'.
    
    TODO: each edit control has built-in functionality to delete itself
    and/or shift it up/down in the layout. Which also shifts it up/down
    in the configuration in the background. 
    """
    #def __init__(self, parent, mod):
    def __init__(self, cfg, mod, main):
        super(EditInclude, self).__init__(cfg, main, addLayout=False)
        self.typ = cfg['typ']
        self.file = cfg['file']
        self.mod = mod

        #self.layout = QtGui.QHBoxLayout(self.ctrlui.layout)
        self.layout = QtGui.QHBoxLayout()
        self.layout.setSpacing(5)
        self.layout.setContentsMargins(margin, margin, margin, margin)
        self.labelCtrl = QtGui.QLabel('include script:')
        self.labelCtrl.setMinimumSize(QtCore.QSize(labelW, 0))
        self.layout.addWidget(self.labelCtrl)
        self.button = QtGui.QPushButton(self.file)
        self.layout.addWidget(self.button)
        
        self.editButton = QtGui.QPushButton('edit script')
        self.editButton.pressed.connect(self.editScript)
        self.layout.addWidget(self.editButton)
        
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.layout.addItem(spacerItem)
        self.mainWidget.setLayout(self.layout)
    
    def getCfg(self):
        cfg = {'typ': self.typ,
               'file': self.file}
        return cfg
    
    def editScript(self):
        subprocess.Popen([self.main.scriptEditor, join(self.mod.path, self.file)])


class EditHotkey(EditCtrl):
    """
    TODO: Oh boy... this has so many implications but it has to be done. Let's do it!
    First: Have the edit ctrl, then the display one, Then we need checks when a mod
    config change is about to be comitted. The change will not be able to be OKed as long
    as there are conflicts with hotkeys, or missing includes or ...

    elif cfg['typ'] == 'hotkey':
        cfg['enabled'] = True
        cfg['disablable'] = True
        cfg['key'] = 'Win+G'
        cfg['keyChange'] = True
        cfg['multiple'] = True
        cfg['scope'] = ''
        cfg['scopeChange'] = True
        # mode can be: ahk, file, key
        # to execute code, open up sth, send keystroke
        cfg['mode'] = 'ahk',
        cfg['name'] = 'someModule_hotkey1',
        cfg['label'] = 'do awesome stuff on:'
    """
    def __init__(self, cfg, mod, main):
        super(EditHotkey, self).__init__(cfg, main, addLayout=False)
        self.main = main
        self.cfg = cfg
        self.ui = Ui_hotkey_edit()
        self.ui.setupUi(self.mainWidget)
        self.ui.hotkeyButton = HotKey(cfg.get('key') or '', self.hotkeyChange)
        self.ui.hotkeyKeyLayout.insertWidget(0, self.ui.hotkeyButton)
        self.mainWidget.setLayout(self.ui.hotkeyCtrlLayout)

        self.disablableCheck()
        self.ui.cfg_disablable.clicked.connect(self.disablableCheck)

        self.functions = ['functionCode', 'functionURL', 'functionSend']
        self.ui.cfg_functionMode.currentIndexChanged.connect(self.functionSetText)
        self.functionMenu = QtGui.QMenu(self.ui.functionButton)
        self.functionMenu.aboutToShow.connect(self.functionMenuBuild)
        self.ui.functionButton.setMenu(self.functionMenu)
        self.functionSetText()
        self.ui.functionText.textChanged.connect(self.functionChanged)
        
        self.ui.cfg_scopeMode.currentIndexChanged.connect(self.scopeModeChanged)
        self.scopeModeChanged()
        
        self.connectCfgCtrls(self.ui)
    
    def functionMenuBuild(self):
        self.functionMenu.clear()
        index = self.ui.cfg_functionMode.currentIndex()
        if index == 0:
            fsubmenu1 = self.functionMenu.addMenu('local functions')
            _fsubmenu2 = self.functionMenu.addMenu('built-in functions')
        elif index == 1:
            for x in [('browse...', self.functionBrowse),
                      ('explore to...', self.functionExplore)]:
                action = QtGui.QAction(self.functionMenu)
                action.setText(x[0])
                action.triggered.connect(x[1])
                self.functionMenu.addAction(action)
        else:
            fsubmenu1 = self.functionMenu.addMenu('Send Mode')
            for x in ['Send', 'SendInput', 'SendRaw']:
                action = QtGui.QAction(fsubmenu1)
                action.setText(x)
                action.triggered.connect(partial(self.functionSendMode, x))
                fsubmenu1.addAction(action)
            #fsubmenu2 = self.functionMenu.addMenu('built-in variables')
            for x in [('Help on Send', self.functionSendHelp)]:
                action = QtGui.QAction(self.functionMenu)
                action.setText(x[0])
                action.triggered.connect(x[1])
                self.functionMenu.addAction(action)
    
    def functionSendMode(self, mode):
        self.cfg['sendmode'] = mode
    
    def functionBrowse(self):
        """TODO"""
        log.info('open a browser and all that ...')
        self.functionSetText(1, 'C:\asasasdf\asdfasdf')

    def functionExplore(self):
        """TODO: verify"""
        text = self.ui.functionText.text()
        subprocess.Popen(['explorer.exe', text])
    
    def functionSendHelp(self):
        self.main.surfTo(self.main.urls.ahksend)
    
    def functionChanged(self, text=None):
        #text = self.ui.functionText.text()
        index = self.ui.cfg_functionMode.currentIndex()
        print('text changed %s: %s' % (index, text))
        print('self.functions[index]: %s' % self.functions[index])
        self.cfg[self.functions[index]] = text
    
    def functionSetText(self, index=None, text=None):
        if index is None:
            index = self.ui.cfg_functionMode.currentIndex()
        if text is None:
            text = self.cfg.get(self.functions[index]) or ''
        print('mode change: %s' % text)
        self.ui.functionText.setText(text)
        # show include thingy
        #self.ui.scopePlus.setVisible(index == 0)
    
    def scopeModeChanged(self, index=None):
        if index is None:
            index = self.ui.cfg_scopeMode.currentIndex()
        state = index != 0
        self.ui.cfg_scope.setVisible(state)
        self.ui.scopePlus.setVisible(state)
        self.ui.scopeMinus.setVisible(state)

    def disablableCheck(self):
        """would be useless if hotkey is off by default and cannot be changed"""
        state = self.ui.cfg_disablable.isChecked()
        self.ui.cfg_enabled.setEnabled(state)
        self.ui.cfg_enabled.setChecked(True)
    
    def hotkeyChange(self, newKey):
        log.info('newKey: %s' % newKey)
        self.cfg['key'] = newKey
    
    def getCfg(self):
        return self.cfg


class HotKey(QtGui.QPushButton):
    def __init__(self, key, func, parent=None):
        super(HotKey, self).__init__()
        self.key = key
        self.tempKey = key
        self.tempOK = True
        self.func = func
        font = QtGui.QFont()
        font.setPointSize(10)
        self.setFont(font)
        #self.main = main
        self.setText(key)
        if parent is not None:
            parent.addWidget(self)
    
    def mousePressEvent(self, event):
        self.buildPopup(event.globalX(), event.globalY())

    def buildPopup(self, x, y):
        self.popup = Popup(x, y)
        self.popup.textEdit = QtGui.QLineEdit(self.popup)
        #self.popup.textEdit.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.popup.textEdit.setFont(font)
        self.popup.textEdit.setText(self.key)
        self.popup.textEdit.textChanged.connect(self.validateHotkey)
        self.popup.textEdit.returnPressed.connect(self.ok)
        
        self.popup.buttonLyt = QtGui.QHBoxLayout()
        self.popup.okButton = QtGui.QPushButton("OK")
        self.popup.okButton.clicked.connect(self.ok)
        self.popup.closeButton = QtGui.QPushButton("&Cancel")
        self.popup.closeButton.clicked.connect(self.popup.close)
        self.popup.buttonLyt.addWidget(self.popup.okButton)
        self.popup.buttonLyt.addWidget(self.popup.closeButton)
        
        self.popup.layout = QtGui.QVBoxLayout()
        self.popup.layout.addWidget(self.popup.textEdit)
        self.popup.layout.addLayout(self.popup.buttonLyt)
        self.popup.setLayout(self.popup.layout)
        self.validateHotkey(self.key)
        
        QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Enter), self.popup, self.ok)
        
        self.popup.show()
        self.popup.placeAtCursor()

    def ok(self):
        log.info('key: %s' % self.tempKey)
        log.info('ok: %s' % self.tempOK)
        if self.tempOK:
            self.key = self.tempKey
            self.popup.close()
            self.func(self.key)
            self.setText(self.key)

    def validateHotkey(self, hkstring):
        """
        first implementation: checks for valid modifyers + a single key
        TODO: handle F1-F12, Del, Home..., handle single keys when in scope, check availability ...
        """
        styleBad = '* {color:#F00}'
        styleGood = '* {color:#0F0}'
        good = False
        hkparts = hkstring.split('+')
        key = hkparts[-1].strip().lower()
        allModifiers = ['win', 'ctrl', 'alt', 'shift']
        modifier = []
        
        if len(key) != 1:
            msg = 'Hotkey must use a single key (%s)' % key
        elif len(hkparts) == 1:
            good = True
        else:
            modifier = [k.strip().lower() for k in hkparts[:-1]]
            badModifier = [k for k in modifier if k not in allModifiers]
            if badModifier:
                msg = ('Modifyer not one of Win, Ctrl, Alt or Shift! (%s)' % ', '.join(badModifier))
            else:
                good = True
        
        if not good:
            self.popup.textEdit.setStyleSheet(styleBad)
            log.error(msg)
        else:
            modifier = [k.title() for k in modifier]
            key = key.title()
            self.tempKey = '+'.join(modifier) + '+' + key
            
            log.info('tempKey %s:' % self.tempKey)
            
            self.popup.textEdit.setStyleSheet(styleGood)
        
        self.tempOK = good


class Popup(QtGui.QWidget):
    """QtCore.Qt.Window
    | QtCore.Qt.CustomizeWindowHint
    """
    def __init__(self, x, y):
        super(Popup, self).__init__()
        self.setpos = (x, y)
        QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Escape),
                        self, self.close)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
    
    def placeAtCursor(self):
        x, y = self.setpos
        pos = self.pos()
        pos.setX(x - (self.width() / 2))
        pos.setY(y - (self.height() / 2))
        self.move(pos)
    
    def leaveEvent(self, *args, **kwargs):
        self.close()
    
    def focusOutEvent(self, event):
        self.close()
        #self.focusOutEvent()
        

class EditView(QtGui.QWidget):
    """
    TODO: self contained object that displays editable controls for the
    different parameters of a module
    """
    def __init__(self):
        pass
