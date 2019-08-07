--create GUI
try(
	cui.unRegisterDialogBar EGC_Export
	destroyDialog EGC_Export
	)
catch()
global TxtValue = "D:\\bake\\low\\"

rollout EGC_Export "EGC_ExportUI" width:454 height:28
(
	edittext 'edt1' "ExportFBX_Path:" text:TxtValue pos:[5,3] width:353 height:20 align:#left
	button 'btn2' "Export_FBX" pos:[368,3] width:83 height:21 align:#left

	--export FBX and create or edit txtfile
	local EGC_Plug_folder = "D:\\EGC_Plugins"
	local configini = EGC_Plug_folder+"\\EGC_configs.py"
	local ExportfbxFile = #()
	fn Export_Exectue yourPath=(
		if selection[1] == undefined then(
			messagebox "Please choose an object fisrt"
		)
		else(
			--have to add noe array, otherwise mesh will combine to export
			yoursel = #()
			for x in selection do(
				if classof x == Editable_Poly or classof x == Editable_Mesh then(
					append yoursel x
				)
				else(
					messagebox (x.name+" is not a Mesh or Poly")
				)
			)
			clearSelection()
			for i in yoursel do(
				select i
				--FBX config for Fornite
				pluginManager.loadClass FbxExporter 
				FbxExporterSetParam "Animation" False
				FbxExporterSetParam "ASCII" False
				FbxExporterSetParam "SmoothingGroups" True
				FbxExporterSetParam "TangentSpaceExport" False
				FbxExporterSetParam "Triangulate" False                
				FbxExporterSetParam "GeomAsBone" False
				FbxExporterSetParam "Cameras" False
				FbxExporterSetParam "EmbedTextures" False
				FbxExporterSetParam "Preserveinstances" False
				FbxExporterSetParam "SmoothMeshExport" False
				FbxExporterSetParam "FileVersion" "FBX201300"
				exportPath = yourPath + i.name
				exportfile exportPath #noPrompt selectedOnly:true using:FBXEXP
				append ExportfbxFile i.name
			)
		)
	)
	on edt1 changed val do(
		if (findString val "\n") != undefined do(
			Npostion = findString val "\n"
			val = replace val Npostion 1 ""
			if val[val.count] != "\\" do(
				val = val + "\\"
			) 
		edt1.text = val
		)
	)
	on btn2 pressed do
	(
		--create export folder
		if edt1.text[edt1.text.count] == "\\" then(
			forCreateFoder = substring edt1.text 1 (edt1.text.count-1)
		)
		if (getDirectories forCreateFoder).count == 0 then(
			messagebox ("no " + forCreateFoder + "will auto create")
			makeDir edt1.text
			messagebox ("created " + forCreateFoder) 
		)
		else if edt1.text == "" then(messageBox "Please add your location")
		else if edt1.text[2] == "" then(messagebox "This is not a real path")
		else if edt1.text[2] != ":" then(messagebox "This is not a real path")
		else(
			if edt1.text[edt1.text.count] != "\\" do(
				edt1.text = edt1.text + "\\" 
			)
			Export_Exectue edt1.text
			FisrtLine = "MaxToUnreal = True"+"\n"
			PYfileArray = ""
			for i=1 to ExportfbxFile.count do(
				PYfileArray += "r'" + edt1.text + ExportfbxFile[i] + ".FBX', "		
			)
			SecLine = "maxExportedAddressFile = [" + PYfileArray + "]\n"
			textcontent = FisrtLine + SecLine
			if (doesFileExist configini) == False then(
				out_file = createfile configini
				format "%" textcontent to:out_file
				close out_file
			)
			else(
				out_file = (openFile configini mode:"w")
				format "%" textcontent to:out_file
				close out_file
			)
			free ExportfbxFile
		)
	)
)
createdialog EGC_Export 
cui.RegisterDialogBar EGC_Export style:#(#cui_dock_top,#cui_max_sized)
cui.DockDialogBar EGC_Export #cui_dock_top
