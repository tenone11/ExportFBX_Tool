import unreal, sys, json, os

Unreal_Folder = '/Game/EGC_Bake'


def staticmesh_for_import_task_option():
    options = unreal.FbxImportUI()
    options.import_mesh = True
    options.import_textures = False
    options.import_materials = False
    options.import_as_skeletal = False
    options.mesh_type_to_import = unreal.FBXImportType.FBXIT_STATIC_MESH
    nomral_method = unreal.FBXNormalImportMethod.FBXNIM_COMPUTE_NORMALS
    options.static_mesh_import_data.normal_import_method = nomral_method
    options.static_mesh_import_data.combine_meshes = True
    options.static_mesh_import_data.auto_generate_collision = False
    options.static_mesh_import_data.compute_weighted_normals = False
    return options


def EGC_import(SingleFBX):
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
    static_mesh = unreal.load_asset(import_task.imported_object_paths[0])
    vertices = unreal.EditorStaticMeshLibrary.get_number_verts(static_mesh, 0)
    return vertices


verts = EGC_import('D:/bake/cal_verts/cal_verts.FBX')
with open('D:/EGC_Plugins/Config/Cal_Verts.json', 'w') as f:
    json.dump({'Vertex_Counts': verts}, f)

# unreal.EditorAssetLibrary.delete_asset('/Game/EGC_Bake/abc1.abc1')