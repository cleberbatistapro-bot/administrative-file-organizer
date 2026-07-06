; ============================================================
;  Organizador de Arquivos Administrativos
;  Instalador gerado com Inno Setup 6
;  OonaTech
; ============================================================

[Setup]
AppName=Organizador de Arquivos
AppVersion=1.0.0
AppPublisher=OonaTech
SetupIconFile=interface\static\organizador.ico
DefaultDirName={autopf}\OonaTech\OrganizadorArquivos
DefaultGroupName=OonaTech\Organizador de Arquivos
OutputDir=dist\instalador
OutputBaseFilename=OrganizadorArquivos_Setup_v1.0.0
Compression=lzma2/ultra64
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=lowest
ArchitecturesInstallIn64BitMode=x64compatible

[Languages]
Name: "brazilianportuguese"; MessagesFile: "compiler:Languages\BrazilianPortuguese.isl"

[Files]
Source: "dist\OrganizadorArquivos.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Organizador de Arquivos"; Filename: "{app}\OrganizadorArquivos.exe"
Name: "{autodesktop}\Organizador de Arquivos"; Filename: "{app}\OrganizadorArquivos.exe"
Name: "{group}\Desinstalar Organizador de Arquivos"; Filename: "{uninstallexe}"

[Run]
Filename: "{app}\OrganizadorArquivos.exe"; \
  Description: "Abrir o Organizador de Arquivos agora"; \
  Flags: nowait postinstall skipifsilent
