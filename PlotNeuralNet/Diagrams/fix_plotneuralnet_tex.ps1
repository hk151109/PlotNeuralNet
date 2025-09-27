# PowerShell script to fix PlotNeuralNet .tex files for modern TikZ

Param(
    [string]$TexFile = ""
)

if ($TexFile -eq "") {
    Write-Host "Usage: .\fix_plotneuralnet_tex.ps1 <filename.tex>"
    exit
}

if (-Not (Test-Path $TexFile)) {
    Write-Host "File '$TexFile' not found."
    exit
}

# Read the original file
$content = Get-Content $TexFile -Raw

# 1. Wrap shift=(x,y,z) coordinates in braces
$content = $content -replace 'shift=\(([^)]*)\)', 'shift={($1)}'

# 2. Wrap at (x,y,z) coordinates in braces
$content = $content -replace ' at \(([^)]*)\)', ' at {($1)}'

# 3. Fix LaTeX \input paths for Layers folder if necessary
#    (optional: uncomment if your Layers folder path is wrong)
# $content = $content -replace '\\input\{..\\Layers/', '\\input{../Layers/'

# Write fixed file
$fixedFile = [System.IO.Path]::GetFileNameWithoutExtension($TexFile) + ".fixed.tex"
Set-Content $fixedFile $content -Encoding UTF8

Write-Host "✅ Fixed file created: $fixedFile"
Write-Host "Compile with: pdflatex -shell-escape $fixedFile"
