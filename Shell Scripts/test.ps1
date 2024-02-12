for ($i = 5; $i -gt 0; $i--) {
    Write-Host -NoNewline "Restarting in $i seconds... "
    Start-Sleep -Seconds 1
    Write-Host -NoNewline "`r" # Move the cursor to the beginning of the line
    Write-Host -NoNewline 
}

Write-Host ""
Write-Host "Time's up!!!"
