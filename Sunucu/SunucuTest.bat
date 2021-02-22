@echo off
powershell curl -UseBasicParsing "http://127.0.0.1:5000/?s=HTTP%%20Yerel"
powershell curl -UseBasicParsing "http://ddnseren.duckdns.org:5000/?s=HTTP%%20Uzak%%20DDNS"
powershell curl -UseBasicParsing -k "https://127.0.0.1:5000/?s=HTTPS%%20Yerel"
powershell curl -UseBasicParsing -k "https://ddnseren.duckdns.org:5000/?s=HTTPS%%20Uzak%%DDNS"
exit