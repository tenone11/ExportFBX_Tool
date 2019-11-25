# -*- coding: UTF-8 -*-
import os, shutil, getpass, Tkinter, ttk, tkMessageBox, re

yourName = getpass.getuser()
yourMain = ""
# Create GUI
win = Tkinter.Tk()
win.title('EGC_PluginSetup')
win.resizable(0, 0)                                       #cant resize UI
winlabel1 = Tkinter.Label(win, text=u'选择用户')
winlabel2 = Tkinter.Label(win, text=u'请输入你的Main文件夹地址')
winpath = Tkinter.Entry(win,width=35)

def delcreate(pyfile, Folder):
    if not os.path.exists(Folder):
        os.makedirs(Folder)
    if os.path.isfile(Folder + '\\' + pyfile):
        os.remove(Folder + '\\' + pyfile)
    shutil.copyfile(pyfile, os.path.join(Folder, os.path.basename(pyfile)))
    return (Folder+'\\'+pyfile+'\n')

def delcreate_folder(pyfolder, Folder):
    if os.path.isdir(Folder + '\\' + pyfolder):
         shutil.rmtree(Folder + '\\' + pyfolder)
    shutil.copytree(pyfolder, Folder+'\\'+'ForEGC')
    return (Folder+'\\'+'ForEGC' + '\n')

def delete(pyfile, Folder):
    if os.path.isfile(Folder+'\\'+pyfile) == True:
        os.remove(Folder + '\\' + pyfile)
    return (Folder+'\\'+pyfile+'\n')

EGC_Plugins = 'D:\\EGC_Plugins'
Maxscriptfolder = 'C:\\Program Files\\Autodesk\\3ds Max 2018\\scripts\\Startup'
MayaMelfolder = 'C:\\Users\\%s\\Documents\\maya\\2018\\prefs\\shelves' % yourName
MarmosetPlugFolder = 'C:\\Users\\%s\\AppData\\Local\\Marmoset Toolbag 3\\plugins' % yourName
Source='P:\\Developers\\Yifei.Zhang\\Plugins\\EGC_Auto\\'

def selmax(yourMain):
    try:
        Marmo_Setuped = delcreate(Source+'EGC_Bake_AutoGroup.py', MarmosetPlugFolder)
        software_Setuped = delcreate(Source+'EGC_ExportFBX.ms', Maxscriptfolder)
        #change path to your main folder
        openMS = open(Maxscriptfolder + '/' + 'EGC_ExportFBX.ms')
        newMS = re.sub('Main_Folder', yourMain, openMS.read())
        openMS = open(Maxscriptfolder + '/' +'EGC_ExportFBX.ms', 'w+')
        openMS.write(newMS)
        openMS.close()
        EGC_Setuped = delcreate(Source+'EGC_AutoImEx.py', EGC_Plugins)
        EGCForEGC = delcreate_folder(Source+'ForEGC',yourMain+'/FortniteGame')
        FBXpresent = delcreate(Source+'Fornite.fbxexportpreset', EGC_Plugins)
        tkMessageBox.showinfo(u'安装成功',
                              u'安装成功\n%s\n%s\n%s\n%s\n%s' % (EGC_Setuped, software_Setuped, Marmo_Setuped, EGCForEGC, FBXpresent))
    except Exception as e:
        tkMessageBox.showerror(u'注意', u'请关闭MAX,MAYA和引擎\n%s' % e)

def selmaya(yourMain):
    try:
        Marmo_Setuped = delcreate(Source+'EGC_Bake_AutoGroup.py', MarmosetPlugFolder)
        software_Setuped = delcreate(Source+'shelf_EGC_ExportFBX.mel', MayaMelfolder)
        #\\\\ in mel
        mainfolder = re.sub('\\\\','\\\\\\\\\\\\\\\\',yourMain)
        openMel = open(MayaMelfolder + '\\' + 'shelf_EGC_ExportFBX.mel')
        newMel = re.sub('Main_Folder', mainfolder, openMel.read())
        openMel = open(MayaMelfolder + '\\' + 'shelf_EGC_ExportFBX.mel', 'w+')
        openMel.write(newMel)
        openMel.close()
        EGCForEGC = delcreate_folder(Source+'ForEGC',yourMain+'\\FortniteGame')
        EGC_Setuped = delcreate(Source+'EGC_AutoImEx.py', EGC_Plugins)
        tkMessageBox.showinfo(u'安装成功',
                              u'安装成功\n%s\n%s\n%s\n%s' % (EGC_Setuped, software_Setuped, Marmo_Setuped, EGCForEGC))
    except Exception as e:
        tkMessageBox.showerror(u'注意', u'请关闭MAX,MAYA和引擎\n%s' % e)

def unsel():
    try:
        delete('EGC_Bake_AutoGroup.py', MarmosetPlugFolder)
        delete('EGC_ExportFBX.ms', Maxscriptfolder)
        delete('EGC_AutoImEx.py', EGC_Plugins)
        delete('shelf_EGC_ExportFBX.mel', MayaMelfolder)
        delete('EGC_AutoImEx.py', EGC_Plugins)
        tkMessageBox.showinfo(u'卸载成功', u'卸载成功')
    except Exception as e:
        tkMessageBox.showerror(u'注意', u'请关闭MAX,MAYA和引擎\n%s' % e)

maxbutton = ttk.Button(win, text='MAX', command=lambda:selmax(winpath.get()))
mayabutton = ttk.Button(win, text='MAYA', command=lambda:selmaya(winpath.get()))
unsetupbutton = ttk.Button(win, text=u'卸载', width=80,command=unsel)
winlabel1.grid(row=0,columnspan=3)
maxbutton.grid(row=1, column=0)
mayabutton.grid(row=1, column=1)
unsetupbutton.grid(row=2, columnspan=3)
winlabel2.grid(row=3,column=0)
winpath.grid(row=3,column=1)

win.mainloop()