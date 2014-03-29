'''
Created on Jul 19, 2013

@author: hoanv
'''

import sys
from PyQt4 import QtCore, QtGui
import urllib2
import threading
import urllib
import commands
import os
from PyQt4.QtCore import Qt

class Introduction(QtGui.QWidget):
    step = 0 
    
    txtfname = None
    txtlname = None
    txtemail = None
    txtorganization = None
    
    txtOrder = None
    txtSerial = None
    
    progress = None 
    btnnext = None
    btnback = None
    
    fname = "" 
    lname = "" 
    email = "" 
    organization = "" 
    order = "" 
    serial = ""
     
    def __init__(self):
        self.step = 0
        
        if( edition == "Consumer_V1" ) :
            self.order = "Emotiv EPOC Control Panel"
            self.serial = "Emotiv EPOC Control Panel"
        elif edition == "SDKLite" :
            self.order = "Emotiv SDK Lite Control Panel"
            self.serial = "Emotiv SDK Lite Control Panel"
            
        super(Introduction,self).__init__()
        self.initUI()
    
    def initUI(self):         
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(QtGui.QPixmap("backgroud.png")))
        self.setFixedSize(620,418)        
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)               
        self.setPalette(palette)       
        self.widget_1 = QtGui.QWidget(self)
        self.widget_2 = QtGui.QWidget(self)
        self.widget_3 = QtGui.QWidget(self)
        self.hbox = QtGui.QHBoxLayout()
        self.widget_1.setLayout(self.hbox) 
        self.radio_layout = QtGui.QVBoxLayout()
        self.widget_2.setLayout(self.radio_layout)
        self.vbox = QtGui.QVBoxLayout()
        self.widget_3.setLayout(self.vbox) 
        self.widget_1.setGeometry(10,370,600,48)
        self.widget_2.setGeometry(15,20,160,180)
        self.widget_3.setGeometry(171,27,430,344)
        self.setWindowTitle("Install "+edkname+ " " + version)  
        self.setWindowIcon(QtGui.QIcon("emotiv_consumer.png"))                    
        self.create_layout_intro()
        
    def create_layout_intro(self) :
        nextButton = QtGui.QPushButton("Next")
        cancelButton = QtGui.QPushButton("Cancel")
        self.connect(nextButton, QtCore.SIGNAL('clicked()'),self.nextClick)
        cancelButton.clicked.connect(self.cancelClick)
        self.hbox.addStretch(1)
        self.hbox.addWidget(nextButton)
        self.hbox.addWidget(cancelButton)        
        
        radio_introduce = QtGui.QRadioButton("Introduction")
        radio_introduce.setChecked(True)
        radio_license = QtGui.QRadioButton("License")
        radio_license.setDisabled(True)
        radio_register = QtGui.QRadioButton("Registration")
        radio_register.setDisabled(True)
        radio_install = QtGui.QRadioButton("Installation")
        radio_install.setDisabled(True)
        radio_complete = QtGui.QRadioButton("Complete")
        radio_complete.setDisabled(True)
        
        self.radio_layout.addWidget(radio_introduce)
        self.radio_layout.addWidget(radio_license)
        self.radio_layout.addWidget(radio_register)
        self.radio_layout.addWidget(radio_install)
        self.radio_layout.addWidget(radio_complete)

        label_introduce = QtGui.QTextBrowser()
        label_introduce.setText("Welcome to Install Wizard for " + edkname +" " + version + "\n"
                        "This will install " + edkname + " " + version +  " version "+ version +" on your computer.\n"
                        "It is recommended that you close all other applications before continuing.\n"
                        "Click Next to continue or Cancel to exit Install.") 
        label_introduce.setFixedSize(420,332)
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Base, Qt.transparent)
        label_introduce.setPalette(palette)
        self.vbox.addWidget(label_introduce)
        self.show()
    
    def create_layout_intro_back(self) :
        nextButton = QtGui.QPushButton("Next")
        cancelButton = QtGui.QPushButton("Cancel")
        self.connect(nextButton, QtCore.SIGNAL('clicked()'),self.nextClick)
        cancelButton.clicked.connect(self.cancelClick)
        self.hbox.addStretch(1)
        self.hbox.addWidget(nextButton)
        self.hbox.addWidget(cancelButton)        
        
        radio_introduce = QtGui.QRadioButton("Introduction")
        radio_introduce.setChecked(True)
        radio_license = QtGui.QRadioButton("License")
        radio_license.setDisabled(True)
        radio_register = QtGui.QRadioButton("Registration")
        radio_register.setDisabled(True)
        radio_install = QtGui.QRadioButton("Installation")
        radio_install.setDisabled(True)
        radio_complete = QtGui.QRadioButton("Complete")
        radio_complete.setDisabled(True)
        
        self.radio_layout.addWidget(radio_introduce)
        self.radio_layout.addWidget(radio_license)
        self.radio_layout.addWidget(radio_register)
        self.radio_layout.addWidget(radio_install)
        self.radio_layout.addWidget(radio_complete)

        label_introduce = QtGui.QTextBrowser()
        label_introduce.setText("Welcome to Install Wizard for " + edkname + " " + version + "\n"
                        "This will install " + edkname + " " + version +  " version"+ version +" on your computer.\n"
                        "It is recommended that you close all other applications before continuing.\n"
                        "Click Next to continue or Cancel to exit Install.")  
        label_introduce.setFixedSize(420,332)
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Base, Qt.transparent)
        label_introduce.setPalette(palette)
        self.vbox.addWidget(label_introduce)
        self.show()
        
    def create_layout_license(self) :        
        nextButton = QtGui.QPushButton("Next")
        cancelButton = QtGui.QPushButton("Cancel")
        backButton = QtGui.QPushButton("Back")
        
        cancelButton.clicked.connect(self.cancelClick)
        self.connect(nextButton, QtCore.SIGNAL('clicked()'),self.nextClick)
        self.connect(backButton, QtCore.SIGNAL('clicked()'),self.backClick)
        
        self.hbox.addStretch(1)
        self.hbox.addWidget(backButton)
        self.hbox.addWidget(nextButton)
        self.hbox.addWidget(cancelButton)
                
        radio_introduce = QtGui.QRadioButton("Introduction")
        radio_introduce.setDisabled(True)
        radio_license = QtGui.QRadioButton("License")
        radio_license.setChecked(True)
        radio_register = QtGui.QRadioButton("Registration")
        radio_register.setDisabled(True)
        radio_install = QtGui.QRadioButton("Installation")
        radio_install.setDisabled(True)
        radio_complete = QtGui.QRadioButton("Complete")
        radio_complete.setDisabled(True)
        
        self.radio_layout.addWidget(radio_introduce)
        self.radio_layout.addWidget(radio_license)
        self.radio_layout.addWidget(radio_register)
        self.radio_layout.addWidget(radio_install)
        self.radio_layout.addWidget(radio_complete)
        
        license = QtGui.QPlainTextEdit()
        self.mlicense = license
        
        if os.path.isfile("./license.txt") :
#             license.setSource(QtCore.QUrl("license.txt"))
            text = open("license.txt").read()
            license.setPlainText(text)
        else :
            thread = asyncDownloadLicense(license)
            thread.run()
        
        license.setFixedSize(420,332)
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Base, Qt.transparent)
        license.setPalette(palette)
        self.vbox.addWidget(license)
        self.show()
        
    def create_layout_register(self) :
        
        nextButton = QtGui.QPushButton("Next")
        cancelButton = QtGui.QPushButton("Cancel")
        backButton = QtGui.QPushButton("Back")
        
        self.connect(backButton, QtCore.SIGNAL('clicked()'),self.backClick)
        self.connect(nextButton, QtCore.SIGNAL('clicked()'),self.nextClick)
        cancelButton.clicked.connect(self.cancelClick)
        
        self.hbox.addStretch(1)
        self.hbox.addWidget(backButton)
        self.hbox.addWidget(nextButton)
        self.hbox.addWidget(cancelButton)
        
        radio_introduce = QtGui.QRadioButton("Introduction")
        radio_introduce.setDisabled(True)
        radio_license = QtGui.QRadioButton("License")
        radio_license.setDisabled(True)
        radio_register = QtGui.QRadioButton("Registration")
        radio_register.setChecked(True)
        radio_install = QtGui.QRadioButton("Installation")
        radio_install.setDisabled(True)
        radio_complete = QtGui.QRadioButton("Complete")
        radio_complete.setDisabled(True)
        
        self.radio_layout.addWidget(radio_introduce)
        self.radio_layout.addWidget(radio_license)
        self.radio_layout.addWidget(radio_register)
        self.radio_layout.addWidget(radio_install)
        self.radio_layout.addWidget(radio_complete)
        
        label_1 = QtGui.QLabel("Please enter your information: ")
        fLayout = QtGui.QFormLayout()
        fistName = QtGui.QLabel("First Name:")
        lastName = QtGui.QLabel("Last Name:")
        email = QtGui.QLabel("Email:")
        organization = QtGui.QLabel("Organization:")        
        _fistName = QtGui.QLineEdit()
        _lastName = QtGui.QLineEdit()
        _email = QtGui.QLineEdit()
        _organization = QtGui.QLineEdit()
        
        _fistName.setText(self.fname)
        _lastName.setText(self.lname)
        _email.setText(self.email)
        _organization.setText(self.organization)
        
        self.txtfname = _fistName
        self.txtlname = _lastName
        self.txtemail = _email
        self.txtorganization = _organization
            
        fLayout.addWidget(label_1)
        fLayout.addRow(fistName, _fistName)
        fLayout.addRow(lastName, _lastName)
        fLayout.addRow(email, _email)
        fLayout.addRow(organization, _organization)
        label_2 = QtGui.QLabel("-------------------------------------------------------------------------------------------\n"
                               "Please enter your Order Number\n""and Serial Key: ")
        orderNumber = QtGui.QLabel("Order Number:")
        serialKey = QtGui.QLabel("Serial Key:")
        
        _orderNumber = QtGui.QLineEdit()
        _serialKey = QtGui.QLineEdit()
        
        _orderNumber.setText(self.order)
        _serialKey.setText(self.serial)
        
        self.txtOrder = _orderNumber
        self.txtSerial = _serialKey
        
        fLayout.addWidget(label_2)
        fLayout.addRow(orderNumber, _orderNumber)
        fLayout.addRow(serialKey, _serialKey)

        if edition == "Consumer_V1" or edition == "SDKLite"   :
            _orderNumber.setDisabled(True)
            _serialKey.setDisabled(True)

        fLayout.setContentsMargins(5, 10, 0, 0)
        self.vbox.addLayout(fLayout)
                 
        self.show() 
    
    def create_layout_install(self) :
        nextButton = QtGui.QPushButton("Next")
        cancelButton = QtGui.QPushButton("Cancel")
        backButton = QtGui.QPushButton("Back")
        self.btnnext = nextButton
        self.btnback = backButton
        
        self.connect(backButton, QtCore.SIGNAL('clicked()'),self.backClick)
        self.connect(nextButton, QtCore.SIGNAL('clicked()'),self.nextClick)
        cancelButton.clicked.connect(self.cancelClick)
        
        self.hbox.addStretch(1)
        self.hbox.addWidget(backButton)
        self.hbox.addWidget(nextButton)
        self.hbox.addWidget(cancelButton)
        
        radio_introduce = QtGui.QRadioButton("Introduction")
        radio_introduce.setDisabled(True)
        radio_license = QtGui.QRadioButton("License")
        radio_license.setDisabled(True)
        radio_register = QtGui.QRadioButton("Registration")
        radio_register.setDisabled(True)
        radio_install = QtGui.QRadioButton("Installation")
        radio_install.setChecked(True)
        radio_complete = QtGui.QRadioButton("Complete")
        radio_complete.setDisabled(True)
        
        self.radio_layout.addWidget(radio_introduce)
        self.radio_layout.addWidget(radio_license)
        self.radio_layout.addWidget(radio_register)
        self.radio_layout.addWidget(radio_install)
        self.radio_layout.addWidget(radio_complete)
        
        label_install = QtGui.QLabel()      
        label_install.setFixedSize(430,50)  
        label_install.setText("Please wait while setup installs "+ edkname +"\n"
                                +version+" on your computer. \n" )
        label_install.setContentsMargins(5, 5, 0, 0)
        progressName = QtGui.QLabel("Downloading Program Files...")
        progessbar = QtGui.QProgressBar()
        self.progress = progessbar
        self.progressname = progressName
        self.vbox.addWidget(label_install)
        
        vbox_progress = QtGui.QVBoxLayout()        
        
        vbox_progress.addWidget(progessbar)
        vbox_progress.addWidget(progressName)
        vbox_progress.addStretch(1)
        vbox_progress.setDirection((vbox_progress.BottomToTop))
        vbox_progress.setContentsMargins(5, 0, 0, 0)
        self.vbox.addLayout(vbox_progress)
                
        self.show() 
        
        self.installmode = "Downloading"
         
        self.thread2 = asyncDownloadSDK(self, progessbar, self.fname, self.lname, self.email, self.organization, self.order, self.serial)
        self.connect(self.thread2, QtCore.SIGNAL('taskUpdated'), self.handleTaskUpdated)
        self.thread2.start()
        self.btnnext.setDisabled(True)
        self.btnback.setDisabled(True)
    
    def handleTaskUpdated(self):
        
        if self.installmode == "Downloading" :
#             print self.thread2.p
            if self.thread2.p == 100  :
#                 self.btnnext.setDisabled(False)
#                 self.btnback.setDisabled(False)
                
                self.progressname.setText("Installing...") 
                self.progress.setValue(0)
                self.installmode = "Install"
                
            self.progress.setValue(self.thread2.p)
        elif self.installmode == "Install" :
            self.progress.setValue(self.thread2.p_install)
            
            if self.thread2.p_install == 100 :
                self.clearLayout(self.layout())
                self.clearLayout(self.widget_1.layout())
                self.clearLayout(self.widget_2.layout())
                self.clearLayout(self.widget_3.layout())
                self.step += 1
                
                self.create_layout_finish()

    def create_layout_finish(self) :
        finishButton = QtGui.QPushButton("Finish")
        self.connect(finishButton, QtCore.SIGNAL('clicked()'),self.finishClick)
        self.hbox.addStretch(1)
        self.hbox.addWidget(finishButton)
        
        radio_introduce = QtGui.QRadioButton("Introduction")
        radio_introduce.setDisabled(True)
        radio_license = QtGui.QRadioButton("License")
        radio_license.setDisabled(True)
        radio_register = QtGui.QRadioButton("Registration")
        radio_register.setDisabled(True)
        radio_install = QtGui.QRadioButton("Installation")
        radio_install.setDisabled(True)
        radio_complete = QtGui.QRadioButton("Complete")
        radio_complete.setChecked(True)
        
        self.radio_layout.addWidget(radio_introduce)
        self.radio_layout.addWidget(radio_license)
        self.radio_layout.addWidget(radio_register)
        self.radio_layout.addWidget(radio_install)
        self.radio_layout.addWidget(radio_complete)    
        
        label_finish = QtGui.QTextBrowser()
        label_finish.setText("The installation process has finished. Click Finish to complete the installation process.")
        label_finish.setFixedSize(420,332)
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Base, Qt.transparent)
        label_finish.setPalette(palette)
        self.vbox.addWidget(label_finish)          
        self.show() 
        
    def closeEvent(self, event):        
        reply = QtGui.QMessageBox.question(self, 'Exit Install',
                                            "Are you sure you want to to exit this install?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore() 
           
    def cancelClick(self):        
        reply = QtGui.QMessageBox.question(self, 'Exit Install',
                                            "Are you sure you want to exit this install?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            sys.exit()
            
    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())


    def nextClick(self): 
        self.clearLayout(self.widget_1.layout())
        self.clearLayout(self.widget_2.layout())
        self.clearLayout(self.widget_3.layout())
        self.step += 1
#         self.setLayout(None)
        if self.step == 1 :
            self.create_layout_license()
        if self.step == 2:
            self.create_layout_register()
        if self.step == 3:
            self.fname = self.txtfname.text()
            self.lname = self.txtlname.text()
            self.email = self.txtemail.text()
            self.organization = self.txtorganization.text()
            
            self.order = self.txtOrder.text()
            self.serial = self.txtSerial.text()

            
            if( self.fname == "" or self.lname == "" or self.email == "" or self.organization == "" or self.order == "" or self.serial == "" ):
                reply = QtGui.QMessageBox.question(self, 'Warning',
                                            "You must fill in all of the fields.", QtGui.QMessageBox.Yes)
        
                if reply == QtGui.QMessageBox.Yes :
                    self.create_layout_register()
                    self.step -= 1   
            else:
                params = urllib.urlencode({'order' : self.order, 'key' : self.serial })
                f = urllib.urlopen("http://emotiv.com/linuxdeployment/check.php?%s" % params)
                check =  f.read()
                
                if check != "ok" and edition != "Consumer_V1" and edition != "SDKLite" :
                    reply = QtGui.QMessageBox.question(self, 'Warning',
                                            "Please check your order number and serial number!", QtGui.QMessageBox.Yes)
        
                    if reply == QtGui.QMessageBox.Yes :
                        self.create_layout_register()
                        self.step -= 1   
                else :                   
                    self.create_layout_install()
                
        if self.step == 4:
            self.create_layout_finish()

    def backClick(self): 
        self.clearLayout(self.widget_1.layout())
        self.clearLayout(self.widget_2.layout())
        self.clearLayout(self.widget_3.layout())
        self.step -= 1
#         self.setLayout(None)
#         if self.step < 0:
#             return
        if self.step == 0 :
            self.create_layout_intro_back()
        if self.step == 1:
            self.create_layout_license()
        if self.step == 2:
            self.create_layout_register()
        if self.step == 3:
            self.create_layout_install()
    def finishClick(self): 
        sys.exit()

class asyncDownloadLicense(QtCore.QThread) :
    mylicense = None
    
    def __init__(self, license) :
        QtCore.QThread.__init__(self)
        self.mylicense = license
        
    def run(self):
        if edition == "Consumer_V1" or edition == "SDKLite"  :
            urllib.urlretrieve("http://emotiv.com/linuxdeployment/download.php?filename=agrement_consumer.txt", "license.txt")
        elif edition == "Education" :
            urllib.urlretrieve("http://emotiv.com/linuxdeployment/download.php?filename=agreement_education.txt", "license.txt")
        else :
            urllib.urlretrieve("http://emotiv.com/linuxdeployment/download.php?filename=agreement_others.txt", "license.txt")
            
        text = open("license.txt").read()
        self.mylicense.setPlainText(text)
        
import platform
import urllib2
import urllib
class asyncDownloadSDK(QtCore.QThread) :
    progressbar = None
    fname = ""
    lname = ""
    email = ""
    organization = ""
    order = ""
    serial = ""
    
    OSName = ""
    OSArch = ""
    
    p = 0
    p_install = 0
    
    def __init__(self, parent, mprogressbar, mfname, mlname, memail, morganization, morder, mserial) :
        QtCore.QThread.__init__(self, parent)
        self.progressbar = mprogressbar
        self.fname = mfname
        self.lname = mlname
        self.email = memail
        self.organization = morganization
        self.order = morder
        self.serial = mserial
        self.p = 0
        
        filename = ""
        
        platformAllInfo = platform.platform()
        machineInfo = platform.machine()
        
        if machineInfo == 'i386' or machineInfo == 'i486' or machineInfo == 'i586' or machineInfo == 'i686' :
            self.OSArch = 'x86'
        else : self.OSArch = 'x64' 
        
        plilc = platformAllInfo.lower()
        
        if plilc.find('ubuntu') != -1 :
            self.OSName = 'ubuntu'
        if plilc.find('fedora') != -1 :
            self.OSName = 'fedora'
        
        print self.OSName + self.OSArch
        

    def run(self):
        system = platform.platform()
        splatform = "linux " + self.OSName
        
#         self.p = 100
#         self.emit(QtCore.SIGNAL('taskUpdated'))
#             
#         self.p_install = 0
#         self.install()
#             
#         return
        
        params = urllib.urlencode({'first' : self.fname, 'last' : self.lname, 'email' : self.email, 'orgi' : self.organization, 'order' : self.order, 'key' : self.serial, 'sdkedition' : edition, 'platform' : splatform, 'systemver' : system, 'appver' : version})
        #f = urllib.urlopen("http://www.emotiv.com/SoftwareRegistration/setuplog.php", params)
        
        if edition != "Consumer_V1" :
            if version == "2.0.0.20" :
                if edition == "SDKLite" :
                    url =  'http://emotiv.com/linuxdeployment/download_test.php?filename=version2/'+self.OSArch+'/'+edition+'.tar.gz'
                else :
                    url = 'http://emotiv.com/linuxdeployment/download_test.php?order='+self.order+'&key='+self.serial+'&filename=version2/'+self.OSArch+'/'+edition+'.tar.gz'
            else :
                if self.OSName == "ubuntu" :
                    url = "http://emotiv.com/linuxdeployment/download_test.php?order="+self.order+"&key="+self.serial+"&filename=" + self.OSArch+"/" + edition +".tar.gz"
                elif self.OSName == "fedora":
                    url = "http://emotiv.com/linuxdeployment/download_test.php?order="+self.order+"&key="+self.serial+"&filename=fedora/" + self.OSArch+"/" +edition +".tar.gz"
        else :
            if version == "1.0.0.5" :
                if self.OSName == "ubuntu" :
                    url = "http://emotiv.com/linuxdeployment/download_test.php?filename=" + self.OSArch+"/Consumer_V1.tar.gz"
                elif self.OSName == "fedora":
                    url = "http://emotiv.com/linuxdeployment/download_test.php?filename=fedora/" + self.OSArch+"/Consumer_V1.tar.gz"
            else :
                url =  'http://emotiv.com/linuxdeployment/download_test.php?filename=version2/'+self.OSArch+'/'+edition+'.tar.gz'
            
        print url
        
        file_name = url.split('/')[-1]
        print file_name
        
        u = urllib2.urlopen(str(url))
        f = open(file_name, 'wb')
        meta = u.info()
#         print meta
        
        file_size = int(meta.getheaders("Content-Length")[0])
        print "Downloading: %s Bytes: %s" % (file_name, file_size)
        
        self.filename = file_name
        self.filesize = file_size
        
        file_size_dl = 0
        block_sz = 8192
        
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break
        
            file_size_dl += len(buffer)
            f.write(buffer)
            #print file_size_dl * 100. / file_size
            self.p = file_size_dl * 100. / file_size
            
            self.emit(QtCore.SIGNAL('taskUpdated'))

#             print status,
        
        f.close()
        
        self.p_install = 0
        self.install()
        
    def install(self) :
        self.emit(QtCore.SIGNAL('taskUpdated'))
        if self.OSName == "ubuntu" :
            print "os ubuntu"
            if edition != "Consumer_V1" or version == "2.0.0.20" :
                self.install_detail()
            else :
                self.install_detail_consumer()
        elif self.OSName == "fedora":
            print "os fedora"  
            if edition != "Consumer_V1"  or version == "2.0.0.20"  :
                self.install_detail()
            else :
                self.install_detail_consumer()
                    
    def install_detail(self) :
        if self.OSName == "fedora" :
            username = os.getenv('USERNAME')
        else :
            username = os.getenv('SUDO_USER')
        
        commands.getoutput("tar xvfz " + edition + ".tar.gz")
        
        print username
            
        self.p_install = 30
        self.emit(QtCore.SIGNAL('taskUpdated'))
        
        commands.getoutput("cp -f "+edition+"/* .")
        commands.getoutput("tar xvfz doc.tar.gz")
        commands.getoutput("tar xvfz lib.tar.gz")
        commands.getoutput("tar xvfz EmoScript\ Samples.tar.gz ")
        commands.getoutput("tar xvfz Qt.tar.gz")
        commands.getoutput("tar xvfz Qt3D.tar.gz")
        commands.getoutput("tar xvfz sceneformats.tar.gz ")
        commands.getoutput("tar xvfz imageformats.tar.gz")
        
        self.p_install = 60
        self.emit(QtCore.SIGNAL('taskUpdated'))
        
        if version == "1.0.0.5" :
            commands.getoutput("mv emotiv.png /usr/share/icons/");
            
        commands.getoutput("rm " + edition + ".tar.gz")
        commands.getoutput("rm  Research.tar.gz")
        commands.getoutput("rm doc.tar.gz")
        commands.getoutput("rm lib.tar.gz")
        commands.getoutput("rm EmoScript\ Samples.tar.gz")
        commands.getoutput("rm Qt.tar.gz")
        commands.getoutput("rm Qt3D.tar.gz")
        commands.getoutput("rm sceneformats.tar.gz")
        commands.getoutput("rm imageformats.tar.gz")
        commands.getoutput("rm -rf Research")
        commands.getoutput("rm -rf "+edition)
        commands.getoutput("rm key.csv")
        commands.getoutput("rm -rf *.sh~")
        
        self.p_install = 70
        self.emit(QtCore.SIGNAL('taskUpdated'))
        
        commands.getoutput("chmod +x ./*")
        
        if version != "1.0.0.5" :
            commands.getoutput('sed -i "s/username/' + username + '/" EmotivControlPanel.desktop')
            commands.getoutput('sed -i "s/username/' + username + '/" EmoKey.desktop')
            commands.getoutput('sed -i "s/username/' + username + '/" EmoComposer.desktop')
            
            if edition == "Research" or edition == "EnterprisePlus" or edition == "Education" :
                commands.getoutput('sed -i "s/username/' + username + '/" TestBench.desktop')
                
            commands.getoutput('sed -i "s/username/' + username + '/" EmotivUninstall.desktop')
            commands.getoutput('sed -i "s/username/' + username + '/" EmotivUninstall.desktop')
            
            if edition == "Research" or edition == "EnterprisePlus" or edition == "Education" :
                commands.getoutput('mv emotiv_sdk.png /usr/share/icons/; mv emokey.png /usr/share/icons/;mv TestBench.png /usr/share/icons/;cp -f EmotivUninstall.desktop /usr/share/applications/;cp -f EmotivControlPanel.desktop /usr/share/applications/;cp -f EmoKey.desktop /usr/share/applications/;cp -f TestBench.desktop /usr/share/applications/; cp -f EmoComposer.desktop /usr/share/applications/')
            else :
                commands.getoutput('mv emotiv_sdk.png /usr/share/icons/; mv emokey.png /usr/share/icons/;mv TestBench.png /usr/share/icons/;cp -f EmotivUninstall.desktop /usr/share/applications/;cp -f EmotivControlPanel.desktop /usr/share/applications/;cp -f EmoKey.desktop /usr/share/applications/;cp -f EmoComposer.desktop /usr/share/applications/')
            
        elif version == "1.0.0.5" :
            commands.getoutput('sed -i "s/username/' + username + '/" EmotivControlPanel.desktop')
            commands.getoutput('cp -f EmotivControlPanel.desktop /usr/share/applications/')
            commands.getoutput('sed -i "s/EmotivControlPanel/EmoComposer/" EmotivControlPanel.desktop')
            commands.getoutput('cp -f EmotivControlPanel.desktop /usr/share/applications/EmoComposer.desktop')
            commands.getoutput('sed -i "s/EmoComposer/EmoKey/" EmotivControlPanel.desktop')
            commands.getoutput('cp -f EmotivControlPanel.desktop /usr/share/applications/EmoKey.desktop')
            
            if edition == "Research" or edition == "EnterprisePlus" or edition == "Education" and version != "1.0.0.5" :
                commands.getoutput('sed -i "s/username/' + username + '/" TestBench.desktop')
            elif version == "1.0.0.5" :
                commands.getoutput('sed -i "s/EmoKey/TestBench/" EmotivControlPanel.desktop')
                commands.getoutput('sudo cp -f EmotivControlPanel.desktop /usr/share/applications/TestBench.desktop')
                
            commands.getoutput('sed -i "s/TestBench/EmotivUninstall/" EmotivControlPanel.desktop')
            commands.getoutput('sudo cp -f EmotivControlPanel.desktop /usr/share/applications/EmotivUninstall.desktop')
        
        if edition == "Consumer_V1" :
            commands.getoutput('sed -i "s/username/' + username + '/" Consumer.desktop')
            commands.getoutput('cp -f Consumer.desktop /usr/share/applications/')
            commands.getoutput('sed -i "s/username/' + username + '/" ConsumerUninstall.desktop')
            commands.getoutput('cp -f ConsumerUninstall.desktop /usr/share/applications/ConsumerUninstall.desktop')
            commands.getoutput('echo "/home/' + username + '/Emotiv_EPOC_Control_Panel/lib" >> /etc/ld.so.conf; ldconfig')
            commands.getoutput('mv emotiv_consumer.png /usr/share/icons/')
            
            
        self.p_install = 75
        self.emit(QtCore.SIGNAL('taskUpdated'))
        
        commands.getoutput('wget -O 70-emotiv.rules "http://emotiv.com/linuxdeployment/download.php?filename=70-emotiv.rules"')
        commands.getoutput('sed -i "s/username/' + username + '/" 70-emotiv.rules')
        self.p_install = 80
        self.emit(QtCore.SIGNAL('taskUpdated'))
        
        commands.getoutput('cp -f 70-emotiv.rules /etc/udev/rules.d/; udevadm control --reload-rules; ln -s /lib/libudev.so.1.1.6 /lib/libudev.so.0; ln -s /lib64/libudev.so.1 /lib64/libudev.so.0; ln -s /lib/x86_64-linux-gnu/libudev.so.1 /lib/x86_64-linux-gnu/libudev.so.0; ln -sf /lib/x86_64-linux-gnulibudev.so.1 /lib/x86_64-linux-gnulibudev.so.0; chown -R ' + username + ' /etc/ld.so.conf; echo "/home/' + username + '/Emotiv'+edition+ '_' +version+'/lib" >> /etc/ld.so.conf; ldconfig')
        self.p_install = 90
        self.emit(QtCore.SIGNAL('taskUpdated'))
        
        commands.getoutput('rm 70-emotiv.rules')
        commands.getoutput('chown -R ' + username + ' ./*');
        commands.getoutput('chgrp -R ' + username + ' ./*');
        
        commands.getoutput('echo "Install success"')
        self.p_install = 100
        self.emit(QtCore.SIGNAL('taskUpdated'))
        
    def install_detail_consumer(self) :
        if self.OSName == "fedora" :
            username = os.getenv('USERNAME')
        else :
            username = os.getenv('SUDO_USER')
        
        commands.getoutput("tar xvfz Consumer_V1.tar.gz")
            
        self.p_install = 30
        self.emit(QtCore.SIGNAL('taskUpdated'))
        
        commands.getoutput("cp -f Consumer_V1/* .")
        commands.getoutput("tar xvfz doc.tar.gz")
        commands.getoutput("tar xvfz lib.tar.gz")
        
        self.p_install = 60
        self.emit(QtCore.SIGNAL('taskUpdated'))
        
        commands.getoutput("rm  Consumer_V1.tar.gz")
        commands.getoutput("rm doc.tar.gz")
        commands.getoutput("rm lib.tar.gz")

        commands.getoutput("rm -rf Consumer_V1")
        commands.getoutput("rm key.csv")
        commands.getoutput("rm -rf *.sh~")
        
        self.p_install = 70
        self.emit(QtCore.SIGNAL('taskUpdated'))
        
        commands.getoutput("chmod +x ./*")
        commands.getoutput('sudo mv emotiv.png /usr/share/icons/')
        commands.getoutput('sed -i "s/username/' + username + '/" Consumer.desktop')
        
        if edition == "Research" or edition == "EnterprisePlus" or edition == "Education" :
            commands.getoutput('sed -i "s/username/' + username + '/" TestBench.desktop')
            
        commands.getoutput('cp -f Consumer.desktop /usr/share/applications/')
        commands.getoutput('sed -i "s/username/' + username + '/" ConsumerUninstall.desktop')
        commands.getoutput('cp -f ConsumerUninstall.desktop /usr/share/applications/ConsumerUninstall.desktop')
        commands.getoutput('rm -rf Consumer.desktop')
        
        self.p_install = 75
        self.emit(QtCore.SIGNAL('taskUpdated'))
        
        commands.getoutput('wget -O 70-emotiv.rules "http://emotiv.com/linuxdeployment/download.php?filename=70-emotiv.rules"')
        commands.getoutput('sed -i "s/username/' + username + '/" 70-emotiv.rules')
        self.p_install = 80
        self.emit(QtCore.SIGNAL('taskUpdated'))
        
        commands.getoutput('cp -f 70-emotiv.rules /etc/udev/rules.d/; udevadm control --reload-rules; ln -s /lib/libudev.so.1.1.6 /lib/libudev.so.0; ln -s /lib64/libudev.so.1 /lib64/libudev.so.0; ln -s /lib/x86_64-linux-gnu/libudev.so.1 /lib/x86_64-linux-gnu/libudev.so.0; ln -sf /lib/x86_64-linux-gnulibudev.so.1 /lib/x86_64-linux-gnulibudev.so.0; chown -R ' + username + ' /etc/ld.so.conf;echo "/home/' + username + '/Emotiv_EPOC_Control_Panel/lib" >> /etc/ld.so.conf; ldconfig')
        self.p_install = 90
        self.emit(QtCore.SIGNAL('taskUpdated'))
        
        commands.getoutput('rm 70-emotiv.rules')
        commands.getoutput('chown -R ' + username + ' ./*');
        commands.getoutput('chgrp -R ' + username + ' ./*');
        commands.getoutput('echo "Install success"')
        
        self.p_install = 100
        self.emit(QtCore.SIGNAL('taskUpdated'))
        
class Install(QtGui.QWidget):
    def __init__(self):
        super(Install,self).__init__()
        self.initUI()
    
    def initUI(self):        
        reply = QtGui.QMessageBox.question(self, 'Install '+ edkname +" " + version,
                                            "This will install "+ edkname + " "+ version + " on your computer. Are you sure you want to install?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        
        if reply == QtGui.QMessageBox.Yes:
            self.introduce = Introduction()
            self.introduce.show()
def main():
    app = QtGui.QApplication(sys.argv)
    install = Install()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
     
    version = "2.0.0.20"
    edition = "Research"

    
    if edition == "EnterprisePlus" :
        edkname = "Emotiv Enterprise Plus Edition"
    elif edition == "Consumer_V1" :
        edkname = "Emotiv EPOC Control Panel"
    elif edition == "SDKLite" :
         edkname = "Emotiv SDK Lite Control Panel"
    else:
        edkname = "Emotiv " + edition + " Edition"
    
    main()
