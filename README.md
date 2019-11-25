# ExportFBX_Tool
2019-11-24: Update for Epic Shanghai Studio, Now you don't need to open Unreal. And Automation will export it
            Please update your unreal to 4.23 at least.
            If you are not in Shanghai Studio. Please edit script by yourself.
            For example:  in EGC_Export.ms
            
            DOSCommand "Main_Folder\\Engine\\Binaries\\Win64\\UE4Editor-Cmd.exe \"Main_Folder\\FortniteGame\\ForEGC\\EGC_Export.uproject\" -run=pythonscript -script=\"D:\\EGC_Plugins\\EGC_AutoImEx.py\"">>>
            DOSCommand "Main_Folder\\Engine\\Binaries\\Win64\\UE4Editor-Cmd.exe -run=pythonscript -script=\"D:\\EGC_Plugins\\EGC_AutoImEx.py\""
