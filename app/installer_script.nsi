Section "Instalar"

    # Carpeta de destino
    SetOutPath "$INSTDIR"

    # Incluir archivos
    File /r "*.*" ; Todos los archivos dentro de la carpeta actual
    
    # Crear accesos directos
    CreateShortcut "$DESKTOP\EditorCodigo.lnk" "$INSTDIR\editor_codigo.exe"
    CreateShortcut "$SMPROGRAMS\EditorCodigo\Uninstall.lnk" "$INSTDIR\uninstall.exe"

SectionEnd
