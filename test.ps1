$ok = $true
Get-ChildItem 'assets\*.svg' | ForEach-Object {
    try {
        [xml]$null = Get-Content $_.FullName -Raw
        Write-Output "VALID  $($_.Name)"
    } catch {
        $ok = $false
        Write-Output "BROKEN $($_.Name) -> $($_.Exception.Message)"
    }
}
if ($ok) { Write-Output 'ALL SVGs VALID' } else { Write-Output 'SOME SVGs INVALID' }
