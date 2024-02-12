
$old_name = $env:COMPUTERNAME
$new_name = Read-Host "Enter your name: "

Write-Host "Do you want to add domain?"

Write-Host " [1] Yes"
Write-Host " [2] No"

$choice = Read-Host

# Add domain
if ($choice -eq "1") {
    $new_domain = Read-Host "Enter Domain name: "
    Add-Computer -DomainName $new_domain
}

#Renaming the Computer
Rename-Computer -Name $old_name -NewName $new_name -Force

Write-Host "Current Name: $old_name"
Write-Host "New Name: $new_name"

# This will force close all the running application
Get-Process | Stop-Process -Force

#8 seconds countdown
for ($i = 8; $i -gt 0; $i--) {
    Write-Host -NoNewline "Restarting in $i seconds... "
    Start-Sleep -Seconds 1
    Write-Host -NoNewline "`r" 
    Write-Host -NoNewline 
}

#Computer will force restart
Restart-Computer -Force
