# -*- coding: UTF-8 -*-
import unreal, re, os, sys

sys.path.append('D:\\EGC_Plugins')
import EGC_configs

# update info
reload(EGC_configs)
fbxPath = EGC_configs.ExportedAddressFile
Unreal_Folder = '/Game/EGC_Bake'


# import task define to FBX
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
    return options


# export task define to FBX
def staticmesh_for_export_task_option():
    options = unreal.FbxExportOption()
    options.ascii = False
    options.collision = False
    options.level_of_detail = False
    options.map_skeletal_motion_to_root = False
    options.vertex_color = False
    options.export_preview_mesh = False
    options.force_front_x_axis = False
    return options


def EGC_imexport(SingleFBX):
    # import
    import_task = unreal.AssetImportTask()
    import_task.automated = True
    import_task.replace_existing = True
    import_task.filename = SingleFBX
    (_FilePath, Filename) = os.path.split(SingleFBX)
    import_task.destination_name = Filename.split('.')[0]
    import_task.destination_path = Unreal_Folder
    import_task.options = staticmesh_for_import_task_option()
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([import_task])

    # export
    export_FBXtask = unreal.AssetExportTask()
    export_FBXtask.automated = True
    export_FBXtask.filename = SingleFBX
    export_FBXtask.object = unreal.load_asset(import_task.imported_object_paths[0])
    export_FBXtask.options = staticmesh_for_export_task_option()
    # print export_task     >>obj : AssetExportTask
    final = unreal.ExporterFBX.run_asset_export_task(export_FBXtask)
    return final


configini = "D:\\EGC_Plugins\\EGC_configs.py"

if __name__ == "__main__":
    if os.path.isfile(configini) == True:
        if EGC_configs.MaxMayaToUnreal == True:
            for i in fbxPath:
                EGC_imexport(i)
            out_file = open(configini, 'w')
            out_file.write('MaxMayaToUnreal = False')
            out_file.write('\nUnrealExport = True')
            out_file.write('\nExportedFile = None')
            out_file.close()
        else:
            print "no FBX from MAX or MAYA currently"