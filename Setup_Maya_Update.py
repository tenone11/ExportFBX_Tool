# -*- coding: UTF-8 -*-
import os, shutil, getpass, re, sys, tkMessageBox, stat

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
        elif i['client'].lower() == yourName + '_main':      # chen si rui Main目录问题
            p4Engine_client.append(i['client'])
            p4Engine_client.append(i['Root'])
    p4.disconnect()
    return p4Engine_client


# ['Yifei.Zhang_Fortnite_Engine', 'd:\\Builds_Fortnite_Engine']

def delcreate(pyfile, Folder):
    if not os.path.exists(Folder):
        os.makedirs(Folder)
    if os.path.isfile(Folder + '\\' + pyfile):
        os.chmod(Folder + '\\' + pyfile, stat.S_IWRITE)     # remove read only
        os.remove(Folder + '\\' + pyfile)
    shutil.copy(pyfile, Folder)
    return Folder + '\\' + pyfile + '\n'


def delcreate_folder(pyfolder, Folder):
    if os.path.isdir(Folder + '\\' + pyfolder):
        os.system("rmdir /s/q %s" % (Folder + '\\' + pyfolder))
    shutil.copytree(pyfolder, Folder + '\\' + 'ForEGC')
    return Folder + '\\' + 'ForEGC' + '\n'


EGC_Plugins = 'D:\\EGC_Plugins'
MayaMelfolder = 'C:\\Users\\%s\\Documents\\maya\\2018\\prefs\\shelves' % yourName
MarmosetPlugFolder = 'C:\\Users\\%s\\AppData\\Local\\Marmoset Toolbag 3\\plugins' % yourName


def selmaya():
    try:
        Marmo_Setuped = delcreate('EGC_Bake_AutoGroup.py', MarmosetPlugFolder)
        software_Setuped = delcreate('shelf_EGC_ExportFBX.mel', MayaMelfolder)
        # \\\\ in mel
        mainfolder = re.sub('\\\\', '\\\\\\\\\\\\\\\\', p4Clients()[1])
        openMel = open(MayaMelfolder + '\\' + 'shelf_EGC_ExportFBX.mel')
        newMel = re.sub('Main_Folder', mainfolder, openMel.read())
        openMel = open(MayaMelfolder + '\\' + 'shelf_EGC_ExportFBX.mel', 'w+')
        openMel.write(newMel)
        openMel.close()
        os.chmod(MayaMelfolder + '\\' + 'shelf_EGC_ExportFBX.mel', stat.S_IREAD)      # restart MAYA and no change for shelf file
        # Engine_Setuped = delcreate('EGC_Auto_Export_MAYA.uasset', Bakefolder)
        EGCForEGC = delcreate_folder('ForEGC', p4Clients()[1] + '\\FortniteGame')
        Version_Setuped = delcreate('Version.json', EGC_Plugins)
        EGC_Setuped = delcreate('EGC_AutoImEx.py', EGC_Plugins)
        tkMessageBox.showinfo(u'安装成功', u'请重新启动MAYA')
        tkMessageBox.showinfo(u'安装成功',
                              u'安装成功\n%s\n%s\n%s\n%s\n%s' % (
                                  EGC_Setuped, software_Setuped, Marmo_Setuped, EGCForEGC, Version_Setuped))
    except Exception as e:
        tkMessageBox.showerror(u'注意出现错误', u'请关闭MAX,MAYA和引擎\n%s' % e)


if __name__ == "__main__":
    selmaya()
