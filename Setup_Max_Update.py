# -*- coding: UTF-8 -*-
import os, shutil, getpass, re, sys, tkMessageBox

# use U disk Python module
sys.path.append('U:\\colossus-live\\_Colossus\\Python\\python27Lib\\Lib\\site-packages')
from P4 import P4

yourName = getpass.getuser()

# Max excute this py with doscommand and you need to check dir to your setup address again
os.chdir("P:\\Developers\\Yifei.Zhang\\Plugins\\EGC_Auto")


def p4Clients():
    p4 = P4()
    p4.port = "proxy:1667"
    p4.user = yourName
    p4.connect()
    p4clientinfo = p4.run('clients', '--me')  # 获得所有本机的workspace
    p4Engine_client = []
    for i in p4clientinfo:
        if i['client'].lower() == yourName + '_fortnite_main':  # junjun的enging目录有问题
            p4Engine_client.append(i['client'])
            p4Engine_client.append(i['Root'])
        elif i['client'].lower() == yourName + '_fortnite_engine':
            p4Engine_client.append(i['client'])
            p4Engine_client.append(i['Root'])
    p4.disconnect()
    return p4Engine_client


# ['Yifei.Zhang_Fortnite_Engine', 'd:\\Builds_Fortnite_Engine']

def delcreate(pyfile, Folder):
    if not os.path.exists(Folder):
        os.makedirs(Folder)
    if os.path.isfile(Folder + '\\' + pyfile):
        os.remove(Folder + '\\' + pyfile)
    shutil.copy(pyfile, Folder)
    return (Folder + '\\' + pyfile + '\n')


def delcreate_folder(pyfolder, Folder):
    if os.path.isdir(Folder + '\\' + pyfolder):
        os.system("rmdir /s/q %s" % (Folder + '\\' + pyfolder))
    shutil.copytree(pyfolder, Folder + '\\' + 'ForEGC')
    return (Folder + '\\' + 'ForEGC' + '\n')


def delete(pyfile, Folder):
    if os.path.isfile(Folder + '\\' + pyfile) == True:
        os.remove(Folder + '\\' + pyfile)
    return (Folder + '\\' + pyfile + '\n')


EGC_Plugins = 'D:\\EGC_Plugins'
Maxscriptfolder = 'C:\\Program Files\\Autodesk\\3ds Max 2018\\scripts\\Startup'
MarmosetPlugFolder = 'C:\\Users\\%s\\AppData\\Local\\Marmoset Toolbag 3\\plugins' % yourName


# Bakefolder = p4Clients()[0][1] + '\\FortniteGame\\Content\\EGC_Bake'

def selmax():
    try:
        Marmo_Setuped = delcreate('EGC_Bake_AutoGroup.py', MarmosetPlugFolder)
        software_Setuped = delcreate('EGC_ExportFBX.ms', Maxscriptfolder)
        # change path to your main folder
        openMS = open(Maxscriptfolder + '\\' + 'EGC_ExportFBX.ms')
        newMS = re.sub('Main_Folder', p4Clients()[1], openMS.read())
        openMS = open(Maxscriptfolder + '\\' + 'EGC_ExportFBX.ms', 'w+')
        openMS.write(newMS)
        openMS.close()
        # Engine_Setuped = delcreate('EGC_Auto_Export_MAX.uasset', Bakefolder)
        EGC_Setuped = delcreate('EGC_AutoImEx.py', EGC_Plugins)
        Version_Setuped = delcreate('Version.json', EGC_Plugins)
        EGCForEGC = delcreate_folder('ForEGC', p4Clients()[1] + '\\FortniteGame')
        FBXpresent = delcreate('Fornite.fbxexportpreset', EGC_Plugins)
        tkMessageBox.showinfo(u'安装成功',
                              u'安装成功\n%s\n%s\n%s\n%s\n%s\n%s' % (
                                  EGC_Setuped, software_Setuped, Marmo_Setuped, EGCForEGC, FBXpresent, Version_Setuped))
    except Exception as e:
        tkMessageBox.showerror(u'注意出现错误', u'请关闭MAX,MAYA和引擎\n%s' % e)


if __name__ == "__main__":
    selmax()
