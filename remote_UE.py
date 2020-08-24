# import win32gui, win32con, socket

# # hld is window puid
# hld = win32gui.FindWindow(None, u"FortniteGame - Unreal Editor")
# if hld==0:
#     print "Open Main Editor"
# else:
#     print hld
#     win32gui.ShowWindow(hld, win32con.SW_SHOW)
#     win32gui.SetForegroundWindow(hld)

import sys, unreal
sys.path.append(r'D:\Builds_Fortnite_Engine\Engine\Plugins\Experimental\PythonScriptPlugin\Content\Python')
import remote_execution as remote


def staticmesh_for_import_task_option():
    options = unreal.FbxImportUI()
    options.import_mesh = True
    options.import_textures = False
    options.import_materials = False
    options.import_as_skeletal = False
    options.mesh_type_to_import = unreal.FBXImportType.FBXIT_STATIC_MESH
    nomral_method = unreal.FBXNormalImportMethod.FBXNIM_COMPUTE_NORMALS
    options.static_mesh_import_data.normal_import_method = nomral_method
    options.static_mesh_import_data.combine_meshes = False
    options.static_mesh_import_data.auto_generate_collision = False
    options.static_mesh_import_data.compute_weighted_normals = False
    return options


def executeCommand(command):
    remote_exec = remote.RemoteExecution()
    remote_exec.start()
    remote_exec.open_command_connection(remote_exec.remote_nodes)
    rec = remote_exec.run_command(command, exec_mode='ExecuteFile')
    if rec['success'] == True:
        return rec['result']
    return None
address = r'C:\\Users\\Yifei.Zhang\\Documents\\Allegorithmic\\Substance Painter\\python\\plugins\\fprint.py'

def remote_Go():
    # command = "str(unreal.GlobalEditorUtilityBase.get_default_object().get_selected_assets())"
    command = "execfile('%s')" % address
    executeCommand(command)
    # print command

remote_Go()
