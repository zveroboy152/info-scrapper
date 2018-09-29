Set-Location C:\temp
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
Invoke-WebRequest https://chocolatey.org/install.ps1 -UseBasicParsing | Invoke-Expression 
choco install -y python3 -force
(new-object System.Net.WebClient).DownloadFile('https://github.com/zveroboy152/Remote-VM-Creation-HyperV/blob/master/info-scrapper.py', 'c:\temp\info-scrapper.py')
python c:\temp\info-scrapper.py
#Remove-Item "c:\temp\*" -force
#dev
Pause