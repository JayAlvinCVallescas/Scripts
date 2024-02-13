$asciiArt = @"
 ____                  _      _                     
/ ___|___  _   _ _ __ | |_ __| | _____      ___ __  
| |   / _ \| | | | '_ \| __/ _` |/ _ \ \ /\ / / '_ \ 
| |__| (_) | |_| | | | | || (_| | (_) \ V  V /| | | |
\____\___/ \__,_|_| |_|\__\__,_|\___/ \_/\_/ |_| |_|
                                                                                                        
"@

Write-Host $asciiArt `n` `n` `n`

                                                     
for ($i = 5; $i -gt 0; $i--) {
    Write-Host -NoNewline "Restarting in $i seconds..."
    Start-Sleep -Seconds 1
    Write-Host -NoNewline "`r" # Move the cursor to the beginning of the line
    Write-Host -NoNewline 
}

Write-Host ""
Write-Host "Time's up!!!" `n`
