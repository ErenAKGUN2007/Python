from flask import Flask, request, send_from_directory
from datetime import datetime
from user_agents import parse
from logging import getLogger
from os import walk, path
dosyalar=[]
sunucu=Flask(__name__)
@sunucu.route('/<dosya>')
def islem(dosya):
    for (yol, yoladi, dosyaadi) in walk(path.dirname(path.realpath(__file__))):
        dosyalar.extend(dosyaadi)
        break
    eposta=request.args.get("e")
    konu=request.args.get("s")
    get=parse(request.headers.get("User-Agent"))
    ip=request.headers.get('X-Forwarded-For', request.remote_addr)
    tarayici=f"{get.browser.family} {get.browser.version_string}"
    sistem=f"{get.os.family} {get.os.version_string}"
    saat=datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    if dosya!="favicon.ico" and (dosya in dosyalar)==True:
        if konu !=None and eposta !=None:
            print(f"{saat}'de '{konu}', {eposta} (IP: {ip}) tarafindan, {sistem} isletim sisteminde, {tarayici} uzerinden acildi.")
        elif konu !=None and eposta==None:
            print(f"{saat}'de '{konu}', {ip} tarafindan, {sistem} isletim sisteminde, {tarayici} uzerinden acildi.")
        elif konu==None and eposta !=None:
            print(f"{saat}'de '{dosya}', {eposta} (IP: {ip}) tarafindan, {sistem} isletim sisteminde, {tarayici} uzerinden acildi.")
        else:
            print(f"{saat}'de '{dosya}', {ip} tarafindan, {sistem} isletim sisteminde, {tarayici} uzerinden acildi.")
        return send_from_directory(".", dosya)
    elif dosya!="favicon.ico" and (dosya in dosyalar)==False:
        if konu !=None and eposta !=None:
            print(f"{saat}'de '{dosya}' (Konu:'{konu}'), {eposta} (IP: {ip}) tarafindan, {sistem} isletim sisteminde, {tarayici} uzerinden istenirken dosya bulunamadi.")
        elif konu !=None and eposta==None:
            print(f"{saat}'de '{dosya}' (Konu:'{konu}'), {ip} tarafindan, {sistem} isletim sisteminde, {tarayici} uzerinden istenirken dosya bulunamadi.")
        elif konu==None and eposta !=None:
            print(f"{saat}'de '{dosya}', {eposta} (IP: {ip}) tarafindan, {sistem} isletim sisteminde, {tarayici} uzerinden istenirken dosya bulunamadi.")
        else:
            print(f"{saat}'de '{dosya}', {ip} tarafindan, {sistem} isletim sisteminde, {tarayici} uzerinden istenirken dosya bulunamadi.")
        return send_from_directory(".", "...")
    elif dosya=="favicon.ico":
        return send_from_directory(".", dosya)
@sunucu.after_request
def header(response):
    response.cache_control.max_age=0
    return response
if __name__=="__main__":
    getLogger("werkzeug").disabled=True
    sunucu.run(host='0.0.0.0',port=5000,threaded=True)