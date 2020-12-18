@echo off
powershell curl -UseBasicParsing "http://127.0.0.1:5000/?s=HTTP%%20Yerel"
powershell curl -UseBasicParsing "http://ddnseren.duckdns.org:5000/?s=HTTP%%20Uzak"
powershell curl -UseBasicParsing "https://127.0.0.1:5000/?s=HTTPS%%20Yerel"
powershell curl -UseBasicParsing "https://ddnseren.duckdns.org:5000/?s=HTTPS%%20Uzak"
exit