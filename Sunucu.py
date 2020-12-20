from flask import Flask, request as istek, send_from_directory as dosyagonder, render_template as html
from datetime import datetime as tarihsaat
from user_agents import parse as urlget
from logging import getLogger as log
from socket import gethostbyaddr as dnslookup
from os import walk, path # ssl ipgoster 
#import cryptography
dosyalar=[]
for (yol, yoladi, dosyaadi) in walk(path.dirname(path.realpath(__file__))):
    dosyalar.extend(dosyaadi)
    break #Sadece Aynı Klasördekiler 
dosyagoster=False # GET Konu Geldiği Halde Dosya Adını Göster (Her Zaman Get Gelmediği Veya Hata Olduğu Zaman Gösterilir.)
alanadigoster=True #Varsa Alan adı Göster 
erisimgoster=True # Dosya İstenmese de Erişim Kaydını Göster
olmayandosyagoster=True
ipgoster=True# Alan Adı Varken de IP Göster YAPILACAK 0 Gösterme 1 Alan adı varken Gösterme 2 E 
favicongoster=False#Favicon.ico dosya isteklerini göster
logging=False# ayrıntılı olay kaydı
debug=False# hata ayıklama
cokluistek=False
https_adhoc=False
sunucuport=5000#tcp
saatturu="%d/%m/%Y %H:%M:%S"

sunucu=Flask(__name__)
@sunucu.errorhandler(404)
def e404(_):
    return html("Error404.html")
@sunucu.errorhandler(500)
def e500(_):
    return html("Error500.html")
@sunucu.route('/<dosya>')
def islem(dosya):
    tarayici=True
    sistem=True
    psistem=""
    pkonud=""
    durum=" açıldı."
    if (dosya=="favicon.ico" and not favicongoster) or ((not dosya in dosyalar) and ((not olmayandosyagoster))) or (dosya=="...///..." and not erisimgoster):
        #return dosyagonder(".",dosya)
        return dosyagonder(".",dosya if dosya=="favicon.ico" else "...")
    get=urlget(istek.headers.get("User-Agent"))
    eposta=istek.args.get("e")
    konu=istek.args.get("s")
    ip=istek.headers.get('X-Forwarded-For', istek.remote_addr)
    saat=f"{tarihsaat.now().strftime(saatturu)}'de"
    try:
        if alanadigoster:
            alanadi=dnslookup(ip)[0]
        else:
            alanadi=False
    except:
        alanadi=False
    if f"{get.os.family}"=="Other":
        sistem=False
    if f"{get.browser.family}"=="Other":
        tarayici=False
    if sistem==tarayici==False:
        psistem=f", "
    elif sistem==tarayici==True:
        if {get.os.version_string}=="":
            sistem=f"{get.os.family}"
        else:
            sistem=f"{get.os.family} {get.os.version_string}"
        if get.browser.version_string=="":
            tarayici=f"{get.browser.family}"
        else:
            tarayici=f"{get.browser.family} {get.browser.version_string}"
        psistem=f", {sistem} işletim sisteminden, {tarayici} üzerinden"
    elif sistem==True:
        if {get.os.version_string}=="":
            sistem=f"{get.os.family}"
        else:
            sistem=f"{get.os.family} {get.os.version_string}"
        psistem=f", {sistem} işletim sisteminden"
    elif tarayici==True:
        if get.browser.version_string=="":
            tarayici=f"{get.browser.family}"
        else:
            tarayici=f"{get.browser.family} {get.browser.version_string}"
        psistem=f", {tarayici} üzerinden"
    if not dosya=="...///...":
        if dosyagoster and konu!=None:
            pkonud=f", '{dosya}' (Konu:'{konu}')"
        elif konu!=None:
           pkonud=f", '{konu}'"
        else:
          pkonud=f", '{dosya}'"
    elif erisimgoster:
        if konu!=None:
            pkonud=f", '{konu}'"
        else:
            pkonud=f""
    if alanadi==False or alanadigoster==False:
        if eposta!=None:
            pkisi=f", {eposta} (IP: {ip}) tarafından"
        else:
            pkisi=f", {ip} tarafından"
    else:
        if eposta!=None:
            if ipgoster:
                pkisi=f", {eposta} (Adres: {alanadi}, IP: {ip}) tarafından"
            else:
                pkisi=f", {eposta} (Adres: {alanadi}) tarafından"
        else:
            if ipgoster:
                pkisi=f", {alanadi} (IP: {ip}) tarafından"
            else:
                pkisi=f", {alanadi} tarafından"
    if dosya=="...///...":
        durum=" erişildi."
    elif not dosya in dosyalar:
        durum=" istendi ancak bulunamadı."
    print(f"{saat}{pkonud}{pkisi}{psistem}{durum}")
    return dosyagonder(".",dosya if dosya in dosyalar else "...")
@sunucu.route("/")
def baglanti():
    islem("...///...")
@sunucu.after_request
def header(response):
    response.cache_control.max_age=0
    return response
if __name__=="__main__":
    if debug or logging:
        print(f"Yol: {path.realpath(__file__)}")
        print(f"Dosyalar: {dosyalar}")
    if not logging:
        log("werkzeug").disabled=True
    sunucu.run(host='0.0.0.0',port=sunucuport,threaded=cokluistek,debug=debug,ssl_context='adhoc' if https_adhoc else None) # ,ssl_context='adhoc' Sadece HTTPS # ,threaded=True Çoklu İstekd