param (
    [string]$path
)

# Check if the provided path exists
if (-Not (Test-Path -Path $path)) {
    Write-Host "The specified path does not exist."
    exit
}

# Function to create zip file
function Create-ZipFile {
    param (
        [string]$folderPath,
		[string]$dirName
    )

    $zipFileName = "$folderPath\$dirName.zip"

    if (Test-Path $zipFileName) {
        Write-Host "Zip file already exists: $zipFileName"
    } else {
        Write-Host "Creating zip file: $zipFileName"
	   Compress-Archive -Path "$folderPath\*.txt" -DestinationPath $zipFileName
	   if (Test-Path "$folderPath\New Folder\"){
		   rm -Path "$folderPath\New Folder\" -Recurse
	   }else{
		   Write-Host "No folder found in $folderPath"
	   }
    }
}

# Get directories one level down from the given path
$directories = Get-ChildItem -Path $path -Directory

foreach ($dir in $directories) {
    Create-ZipFile -folderPath $dir.FullName -dirName $dir.Name
}
