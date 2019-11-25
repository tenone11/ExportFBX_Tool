--create GUI
try(
	cui.unRegisterDialogBar EGC_Export
	destroyDialog EGC_Export
	)
catch()
global TxtValue = "D:\\bake\\low"

rollout EGC_Export "EGC_ExportUI" width:454 height:28
(
	edittext 'edt1' "ExportFBX_Path:" text:TxtValue pos:[5,3] width:353 height:20 align:#left
	button 'btn2' "Export_FBX" pos:[368,3] width:83 height:21 align:#left

	--export FBX and create or edit txtfile
	local EGC_Plug_folder = "D:\\EGC_Plugins"
	local configini = EGC_Plug_folder+"\\EGC_configs.py"
	local ExportfbxFile = #()
	fn Check=(
		yoursel = #()
		if selection[1] == undefined then(
			messagebox "Please choose an object fisrt"
			return false
		)
		else(
			for x in selection do(
				if classof x == Editable_Poly or classof x == Editable_Mesh then(
					append yoursel x
				)
				else(
					messagebox (x.name+" is not a Mesh or Poly")
				)
			)
			if yoursel.count==0 then(return false)
			else(return yoursel)
		)
	)

	fn Check_Path you_path=(
		if you_path[you_path.count] !="\\" then(
			if (getDirectories you_path).count == 0 then(
			messagebox ("no " + you_path + " will auto create")
			makeDir you_path
			messagebox ("created " + you_path + ",Please click again.") 
			)
			else if you_path == "" then(messageBox "Please add your location")
			else if you_path[2] == "" then(messagebox "This is not a real path")
			else if you_path[2] != ":" then(messagebox "This is not a real path")
			else(
				yourpath = getDirectories you_path
			)
		)
		else(
			forCreateFoder = substring you_path 1 (you_path.count-1)
			Sentence ="Please delete your last letter \"\\\"\n" + you_path + ">>>"+ forCreateFoder
			messagebox Sentence
			return 0
			)
		return yourpath[1]
	)
	
	fn Export_Exectue yourPath=(
		for i in Check() do(
			select i
			--FBX config for Fornite
			pluginManager.loadClass FbxExporter 
			FBXExporterSetParam "LoadExportPresetFile" "D:\\EGC_Plugins\\Fornite.fbxexportpreset"
			exportPath = yourPath + i.name +".fbx"
			exportfile exportPath #noPrompt selectedOnly:true using:FBXEXP
			append ExportfbxFile i.name
		)
	)
	
	on btn2 pressed do
	(
		if Check() != false and (Check_Path edt1.text)!=0
		then(
			Export_Exectue (Check_Path edt1.text)
			FisrtLine = "MaxMayaToUnreal = True"+"\n"
			PYfileArray = ""
			for i=1 to ExportfbxFile.count do(
				PYfileArray += "r'" + (Check_Path edt1.text) + ExportfbxFile[i] + ".FBX', "		
			)
			SecLine = "ExportedAddressFile = [" + PYfileArray + "]\n"
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
			DOSCommand "Main_Folder\\Engine\\Binaries\\Win64\\UE4Editor-Cmd.exe \"Main_Folder\\FortniteGame\\ForEGC\\EGC_Export.uproject\" -run=pythonscript -script=\"D:\\EGC_Plugins\\EGC_AutoImEx.py\""
		)
	)
)
createdialog EGC_Export style:#(#style_titlebar)
cui.RegisterDialogBar EGC_Export style:#(#cui_dock_top,#cui_max_sized,#cui_handles)
cui.DockDialogBar EGC_Export #cui_dock_top
