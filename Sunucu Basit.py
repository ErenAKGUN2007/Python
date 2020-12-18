from flask import Flask, request, send_from_directory
from datetime import datetime
from user_agents import parse
from logging import getLogger
#import cryptography
sunucu=Flask(__name__)
@sunucu.route('/<dosya>')
def get_file(dosya):
    eposta=request.args.get("e")
    konu=request.args.get("s")
    get=parse(request.headers.get("User-Agent"))
    ip=request.headers.get('X-Forwarded-For', request.remote_addr)
    tarayici=f"{get.browser.family} {get.browser.version_string}"
    sistem=f"{get.os.family} {get.os.version_string}"
    saat=datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    if dosya!="favicon.ico":
        if konu !=None and eposta !=None:
            print(f"{saat}'de '{konu}', {eposta} (IP: {ip}) tarafindan, {sistem} isletim sisteminde, {tarayici} uzerinden acildi.")
        elif konu !=None and eposta==None:
            print(f"{saat}'de '{konu}', {ip} tarafindan, {sistem} isletim sisteminde, {tarayici} uzerinden acildi.")
        elif konu==None and eposta !=None:
            print(f"{saat}'de '{dosya}', {eposta} (IP: {ip}) tarafindan, {sistem} isletim sisteminde, {tarayici} uzerinden acildi.")
        else:
            print(f"{saat}'de '{dosya}', {ip} tarafindan, {sistem} isletim sisteminde, {tarayici} uzerinden acildi.")
    return send_from_directory(".", dosya)
@sunucu.after_request
def add_header(response):
    response.cache_control.max_age=0
    return response
if __name__=="__main__":
    getLogger("werkzeug").disabled=True
    sunucu.run(host='0.0.0.0',port=5000,threaded=True) # ,ssl_context='adhoc' Sadece HTTPS # ,threaded=True Çoklu İstek