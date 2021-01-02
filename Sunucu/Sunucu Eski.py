from flask import Flask, request, send_from_directory
from datetime import datetime
from user_agents import parse
from logging import getLogger
from socket import gethostbyaddr
from os import walk, path # ssl ipgoster 
#import cryptography
dosyalar=[]
for (yol, yoladi, dosyaadi) in walk(path.dirname(path.realpath(__file__))):
    dosyalar.extend(dosyaadi)
    break #Sadece Aynı Klasördekiler 
dosyagoster=False # GET Konu Geldiği Halde Dosya Adını Göster (Her Zaman Get Gelmediği Veya Hata Olduğu Zaman Gösterilir.)
alanadigoster=True #Varsa Alan adı Göster 
erisimgoster=True # Dosya İstenmese de Erişim Kaydını Göster
ipgoster=True# Alan Adı Varken de IP Göster YAPILACAK
favicongoster=False#Favicon.ico dosya isteklerini göster
logging=False# ayrıntılı olay kaydı
debug=False# hata ayıklama
sunucuport=5000
sunucu=Flask(__name__)
@sunucu.route('/<dosya>')
def islem(dosya):
    eposta=request.args.get("e")
    konu=request.args.get("s")
    get=parse(request.headers.get("User-Agent"))
    ip=request.headers.get('X-Forwarded-For', request.remote_addr)
    try:
        if alanadigoster:
            alanadi=gethostbyaddr(ip)[0]
        else:
            alanadi=False
    except:
        alanadi=False
    if f"{get.os.family}"=="Other":
        sistem=None
    elif get.os.version_string=="":
        sistem=f"{get.os.family}"
    else:
        sistem=f"{get.os.family} {get.os.version_string}"
    if f"{get.browser.family}"=="Other":
        tarayici=None
    elif get.browser.version_string=="":
        tarayici=f"{get.browser.family}"
    else:
        tarayici=f"{get.browser.family} {get.browser.version_string}"
    saat=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    if dosya=="favicon.ico" and not favicongoster:
        return send_from_directory(".", dosya)
    elif tarayici!=None and sistem!=None and (alanadi==False or alanadigoster==False):
        if dosyagoster==False and (dosya in dosyalar):
            if konu !=None and eposta !=None:
                print(f"{saat}'de '{konu}', {eposta} (IP: {ip}) tarafından, {sistem} işletim sisteminde, {tarayici} üzerinden açıldı.")
            elif konu !=None and eposta==None:
                print(f"{saat}'de '{konu}', {ip} tarafından, {sistem} işletim sisteminde, {tarayici} üzerinden açıldı.")
            elif konu==None and eposta !=None:
               print(f"{saat}'de '{dosya}', {eposta} (IP: {ip}) tarafından, {sistem} işletim sisteminde, {tarayici} üzerinden açıldı.")
            else:
                print(f"{saat}'de '{dosya}', {ip} tarafından, {sistem} işletim sisteminde, {tarayici} üzerinden açıldı.")
            return send_from_directory(".", dosya)
        elif dosyagoster and (dosya in dosyalar):
            if konu !=None and eposta !=None:
                print(f"{saat}'de '{dosya}' (Konu:'{konu}'), {eposta} (IP: {ip}) tarafından, {sistem} işletim sisteminde, {tarayici} üzerinden açıldı.")
            elif konu !=None and eposta==None:
                print(f"{saat}'de '{dosya}' (Konu:'{konu}'), {ip} tarafından, {sistem} işletim sisteminde, {tarayici} üzerinden açıldı.")
            elif konu==None and eposta !=None:
                print(f"{saat}'de '{dosya}', {eposta} (IP: {ip}) tarafından, {sistem} işletim sisteminde, {tarayici} üzerinden açıldı.")
            else:
                print(f"{saat}'de '{dosya}', {ip} tarafından, {sistem} işletim sisteminde, {tarayici} üzerinden açıldı.")
            return send_from_directory(".", dosya)
        elif dosya=="...///...":
            if not erisimgoster:
                None
            elif konu !=None and eposta !=None:
                print(f"{saat}'de '{konu}', {eposta} (IP: {ip}) tarafından, {sistem} işletim sisteminde, {tarayici} üzerinden erişildi.")
            elif konu !=None and eposta==None:
                print(f"{saat}'de '{konu}', {ip} tarafından, {sistem} işletim sisteminde, {tarayici} üzerinden erişildi.")
            elif konu==None and eposta !=None:
                print(f"{saat}'de {eposta} (IP: {ip}) tarafından, {sistem} işletim sisteminde, {tarayici} üzerinden erişildi.")
            else:
                print(f"{saat}'de {ip} tarafından, {sistem} işletim sisteminde, {tarayici} üzerinden erişildi.")
            return send_from_directory(".", "...")
        elif not (dosya in dosyalar):
            if konu !=None and eposta !=None:
                print(f"{saat}'de '{dosya}' (Konu:'{konu}'), {eposta} (IP: {ip}) tarafından, {sistem} işletim sisteminde, {tarayici} üzerinden istendi ancak bulunamadı.")
            elif konu !=None and eposta==None:
                print(f"{saat}'de '{dosya}' (Konu:'{konu}'), {ip} tarafından, {sistem} işletim sisteminde, {tarayici} üzerinden istendi ancak bulunamadı.")
            elif konu==None and eposta !=None:
                print(f"{saat}'de '{dosya}', {eposta} (IP: {ip}) tarafından, {sistem} işletim sisteminde, {tarayici} üzerinden istendi ancak bulunamadı.")
            else:
                print(f"{saat}'de '{dosya}', {ip} tarafından, {sistem} işletim sisteminde, {tarayici} üzerinden istendi ancak bulunamadı.")
            return send_from_directory(".", "...")
    elif tarayici==None and sistem!=None and (alanadi==False or alanadigoster==False):
        if dosyagoster==False and (dosya in dosyalar):
            if konu !=None and eposta !=None:
                print(f"{saat}'de '{konu}', {eposta} (IP: {ip}) tarafından, {sistem} işletim sisteminden açıldı.")
            elif konu !=None and eposta==None:
                print(f"{saat}'de '{konu}', {ip} tarafından, {sistem} işletim sisteminden açıldı.")
            elif konu==None and eposta !=None:
               print(f"{saat}'de '{dosya}', {eposta} (IP: {ip}) tarafından, {sistem} işletim sisteminden açıldı.")
            else:
                print(f"{saat}'de '{dosya}', {ip} tarafından, {sistem} işletim sisteminden açıldı.")
            return send_from_directory(".", dosya)
        elif dosyagoster and (dosya in dosyalar):
            if konu !=None and eposta !=None:
                print(f"{saat}'de '{dosya}' (Konu:'{konu}'), {eposta} (IP: {ip}) tarafından, {sistem} işletim sisteminden açıldı.")
            elif konu !=None and eposta==None:
                print(f"{saat}'de '{dosya}' (Konu:'{konu}'), {ip} tarafından, {sistem} işletim sisteminden açıldı.")
            elif konu==None and eposta !=None:
                print(f"{saat}'de '{dosya}', {eposta} (IP: {ip}) tarafından, {sistem} işletim sisteminden açıldı.")
            else:
                print(f"{saat}'de '{dosya}', {ip} tarafından, {sistem} işletim sisteminden açıldı.")
            return send_from_directory(".", dosya)
        elif dosya=="...///...":
            if not erisimgoster:
                None
            elif konu !=None and eposta !=None:
                print(f"{saat}'de '{konu}', {eposta} (IP: {ip}) tarafından, {sistem} işletim sisteminden erişildi.")
            elif konu !=None and eposta==None:
                print(f"{saat}'de '{konu}', {ip} tarafından, {sistem} işletim sisteminden erişildi.")
            elif konu==None and eposta !=None:
                print(f"{saat}'de {eposta} (IP: {ip}) tarafından, {sistem} işletim sisteminden erişildi.")
            else:
                print(f"{saat}'de {ip} tarafından, {sistem} işletim sisteminden erişildi.")
            return send_from_directory(".", "...")
        elif not (dosya in dosyalar):
            if konu !=None and eposta !=None:
                print(f"{saat}'de '{dosya}' (Konu:'{konu}'), {eposta} (IP: {ip}) tarafından, {sistem} işletim sisteminden istendi ancak bulunamadı.")
            elif konu !=None and eposta==None:
                print(f"{saat}'de '{dosya}' (Konu:'{konu}'), {ip} tarafından, {sistem} işletim sisteminden istendi ancak bulunamadı.")
            elif konu==None and eposta !=None:
                print(f"{saat}'de '{dosya}', {eposta} (IP: {ip}) tarafından, {sistem} işletim sisteminden istendi ancak bulunamadı.")
            else:
                print(f"{saat}'de '{dosya}', {ip} tarafından, {sistem} işletim sisteminden istendi ancak bulunamadı.")
            return send_from_directory(".", "...")
    elif tarayici!=None and sistem==None and (alanadi==False or alanadigoster==False):
        if dosyagoster==False and (dosya in dosyalar):
            if konu !=None and eposta !=None:
                print(f"{saat}'de '{konu}', {eposta} (IP: {ip}) tarafından, {tarayici} üzerinden açıldı.")
            elif konu !=None and eposta==None:
                print(f"{saat}'de '{konu}', {ip} tarafından, {tarayici} üzerinden açıldı.")
            elif konu==None and eposta !=None:
               print(f"{saat}'de '{dosya}', {eposta} (IP: {ip}) tarafından, {tarayici} üzerinden açıldı.")
            else:
                print(f"{saat}'de '{dosya}', {ip} tarafından, {tarayici} üzerinden açıldı.")
            return send_from_directory(".", dosya)
        elif dosyagoster and (dosya in dosyalar):
            if konu !=None and eposta !=None:
                print(f"{saat}'de '{dosya}' (Konu:'{konu}'), {eposta} (IP: {ip}) tarafından, {tarayici} üzerinden açıldı.")
            elif konu !=None and eposta==None:
                print(f"{saat}'de '{dosya}' (Konu:'{konu}'), {ip} tarafından, {tarayici} üzerinden açıldı.")
            elif konu==None and eposta !=None:
                print(f"{saat}'de '{dosya}', {eposta} (IP: {ip}) tarafından, {tarayici} üzerinden açıldı.")
            else:
                print(f"{saat}'de '{dosya}', {ip} tarafından, {tarayici} üzerinden açıldı.")
            return send_from_directory(".", dosya)
        elif dosya=="...///...":
            if not erisimgoster:
                None
            elif konu !=None and eposta !=None:
                print(f"{saat}'de '{konu}', {eposta} (IP: {ip}) tarafından, {tarayici} üzerinden erişildi.")
            elif konu !=None and eposta==None:
                print(f"{saat}'de '{konu}', {ip} tarafından, {tarayici} üzerinden erişildi.")
            elif konu==None and eposta !=None:
                print(f"{saat}'de {eposta} (IP: {ip}) tarafından, {tarayici} üzerinden erişildi.")
            else:
                print(f"{saat}'de {ip} tarafından, {tarayici} üzerinden erişildi.")
            return send_from_directory(".", "...")
        elif not (dosya in dosyalar):
            if konu !=None and eposta !=None:
                print(f"{saat}'de '{dosya}' (Konu:'{konu}'), {eposta} (IP: {ip}) tarafından, {tarayici} üzerinden istendi ancak bulunamadı.")
            elif konu !=None and eposta==None:
                print(f"{saat}'de '{dosya}' (Konu:'{konu}'), {ip} tarafından, {tarayici} üzerinden istendi ancak bulunamadı.")
            elif konu==None and eposta !=None:
                print(f"{saat}'de '{dosya}', {eposta} (IP: {ip}) tarafından, {tarayici} üzerinden istendi ancak bulunamadı.")
            else:
                print(f"{saat}'de '{dosya}', {ip} tarafından, {tarayici} üzerinden istendi ancak bulunamadı.")
            return send_from_directory(".", "...")
    elif tarayici==None and sistem==None and (alanadi==False or alanadigoster==False):
        if dosyagoster==False and (dosya in dosyalar):
            if konu !=None and eposta !=None:
                print(f"{saat}'de '{konu}', {eposta} (IP: {ip}) tarafından üzerinden açıldı.")
            elif konu !=None and eposta==None:
                print(f"{saat}'de '{konu}', {ip} tarafından üzerinden açıldı.")
            elif konu==None and eposta !=None:
               print(f"{saat}'de '{dosya}', {eposta} (IP: {ip}) tarafından üzerinden açıldı.")
            else:
                print(f"{saat}'de '{dosya}', {ip} tarafından üzerinden açıldı.")
            return send_from_directory(".", dosya)
        elif dosyagoster and (dosya in dosyalar):
            if konu !=None and eposta !=None:
                print(f"{saat}'de '{dosya}' (Konu:'{konu}'), {eposta} (IP: {ip}) tarafından açıldı.")
            elif konu !=None and eposta==None:
                print(f"{saat}'de '{dosya}' (Konu:'{konu}'), {ip} tarafından açıldı.")
            elif konu==None and eposta !=None:
                print(f"{saat}'de '{dosya}', {eposta} (IP: {ip}) tarafından üzerinden açıldı.")
            else:
                print(f"{saat}'de '{dosya}', {ip} tarafından üzerinden açıldı.")
            return send_from_directory(".", dosya)
        elif dosya=="...///...":
            if not erisimgoster:
                None
            elif konu !=None and eposta !=None:
                print(f"{saat}'de '{konu}', {eposta} (IP: {ip}) tarafından üzerinden erişildi.")
            elif konu !=None and eposta==None:
                print(f"{saat}'de '{konu}', {ip} tarafından üzerinden erişildi.")
            elif konu==None and eposta !=None:
                print(f"{saat}'de {eposta} (IP: {ip}) tarafından üzerinden erişildi.")
            else:
                print(f"{saat}'de {ip} tarafından üzerinden erişildi.")
            return send_from_directory(".", "...")
        elif not (dosya in dosyalar):
            if konu !=None and eposta !=None:
                print(f"{saat}'de '{dosya}' (Konu:'{konu}'), {eposta} (IP: {ip}) tarafından istendi ancak bulunamadı.")
            elif konu !=None and eposta==None:
                print(f"{saat}'de '{dosya}' (Konu:'{konu}'), {ip} tarafından üzerinden istendi ancak bulunamadı.")
            elif konu==None and eposta !=None:
                print(f"{saat}'de '{dosya}', {eposta} (IP: {ip}) tarafından üzerinden istendi ancak bulunamadı.")
            else:
                print(f"{saat}'de '{dosya}', {ip} tarafından üzerinden istendi ancak bulunamadı.")
            return send_from_directory(".", "...")
    elif tarayici!=None and sistem!=None:
        if dosyagoster==False and (dosya in dosyalar):
            if konu !=None and eposta !=None:
                print(f"{saat}'de '{konu}', {eposta} (Adres: {alanadi}, IP: {ip}) tarafından, {sistem} işletim sisteminde, {tarayici} üzerinden açıldı.")
            elif konu !=None and eposta==None:
                print(f"{saat}'de '{konu}', {alanadi} (IP: {ip}) tarafından, {sistem} işletim sisteminde, {tarayici} üzerinden açıldı.")
            elif konu==None and eposta !=None:
               print(f"{saat}'de '{dosya}', {eposta} (Adres: {alanadi}, IP: {ip}) tarafından, {sistem} işletim sisteminde, {tarayici} üzerinden açıldı.")
            else:
                print(f"{saat}'de '{dosya}', {alanadi} (IP: {ip}) tarafından, {sistem} işletim sisteminde, {tarayici} üzerinden açıldı.")
            return send_from_directory(".", dosya)
        elif dosyagoster and (dosya in dosyalar):
            if konu !=None and eposta !=None:
                print(f"{saat}'de '{dosya}' (Konu:'{konu}'), {eposta} (Adres: {alanadi}, IP: {ip}) tarafından, {sistem} işletim sisteminde, {tarayici} üzerinden açıldı.")
            elif konu !=None and eposta==None:
                print(f"{saat}'de '{dosya}' (Konu:'{konu}'), {alanadi} (IP: {ip}), {sistem} işletim sisteminde, {tarayici} üzerinden açıldı.")
            elif konu==None and eposta !=None:
                print(f"{saat}'de '{dosya}', {eposta} (Adres: {alanadi}, IP: {ip}) tarafından, {sistem} işletim sisteminde, {tarayici} üzerinden açıldı.")
            else:
                print(f"{saat}'de '{dosya}', {alanadi} (IP: {ip}), {sistem} işletim sisteminde, {tarayici} üzerinden açıldı.")
            return send_from_directory(".", dosya)
        elif dosya=="...///...":
            if not erisimgoster:
                None
            elif konu !=None and eposta !=None:
                print(f"{saat}'de '{konu}', {eposta} (Adres: {alanadi}, IP: {ip}) tarafından, {sistem} işletim sisteminde, {tarayici} üzerinden erişildi.")
            elif konu !=None and eposta==None:
                print(f"{saat}'de '{konu}', {alanadi} (IP: {ip}), {sistem} işletim sisteminde, {tarayici} üzerinden erişildi.")
            elif konu==None and eposta !=None:
                print(f"{saat}'de {eposta} (Adres: {alanadi}, IP: {ip}) tarafından, {sistem} işletim sisteminde, {tarayici} üzerinden erişildi.")
            else:
                print(f"{saat}'de {alanadi} (IP: {ip}), {sistem} işletim sisteminde, {tarayici} üzerinden erişildi.")
            return send_from_directory(".", "...")
        elif not (dosya in dosyalar):
            if konu !=None and eposta !=None:
                print(f"{saat}'de '{dosya}' (Konu:'{konu}'), {eposta} (Adres: {alanadi}, IP: {ip}) tarafından, {sistem} işletim sisteminde, {tarayici} üzerinden istendi ancak bulunamadı.")
            elif konu !=None and eposta==None:
                print(f"{saat}'de '{dosya}' (Konu:'{konu}'), {alanadi} (IP: {ip}), {sistem} işletim sisteminde, {tarayici} üzerinden istendi ancak bulunamadı.")
            elif konu==None and eposta !=None:
                print(f"{saat}'de '{dosya}', {eposta} (Adres: {alanadi}, IP: {ip}) tarafından, {sistem} işletim sisteminde, {tarayici} üzerinden istendi ancak bulunamadı.")
            else:
                print(f"{saat}'de '{dosya}', {alanadi} (IP: {ip}), {sistem} işletim sisteminde, {tarayici} üzerinden istendi ancak bulunamadı.")
            return send_from_directory(".", "...")
    elif tarayici==None and sistem!=None:
        if dosyagoster==False and (dosya in dosyalar):
            if konu !=None and eposta !=None:
                print(f"{saat}'de '{konu}', {eposta} (Adres: {alanadi}, IP: {ip}) tarafından, {sistem} işletim sisteminden açıldı.")
            elif konu !=None and eposta==None:
                print(f"{saat}'de '{konu}', {alanadi} (IP: {ip}), {sistem} işletim sisteminden açıldı.")
            elif konu==None and eposta !=None:
               print(f"{saat}'de '{dosya}', {eposta} (Adres: {alanadi}, IP: {ip}) tarafından, {sistem} işletim sisteminden açıldı.")
            else:
                print(f"{saat}'de '{dosya}', {alanadi} (IP: {ip}), {sistem} işletim sisteminden açıldı.")
            return send_from_directory(".", dosya)
        elif dosyagoster and (dosya in dosyalar):
            if konu !=None and eposta !=None:
                print(f"{saat}'de '{dosya}' (Konu:'{konu}'), {eposta} (Adres: {alanadi}, IP: {ip}) tarafından, {sistem} işletim sisteminden açıldı.")
            elif konu !=None and eposta==None:
                print(f"{saat}'de '{dosya}' (Konu:'{konu}'), {alanadi} (IP: {ip}), {sistem} işletim sisteminden açıldı.")
            elif konu==None and eposta !=None:
                print(f"{saat}'de '{dosya}', {eposta} (Adres: {alanadi}, IP: {ip}) tarafından, {sistem} işletim sisteminden açıldı.")
            else:
                print(f"{saat}'de '{dosya}', {alanadi} (IP: {ip}), {sistem} işletim sisteminden açıldı.")
            return send_from_directory(".", dosya)
        elif dosya=="...///...":
            if not erisimgoster:
                None
            elif konu !=None and eposta !=None:
                print(f"{saat}'de '{konu}', {eposta} (Adres: {alanadi}, IP: {ip}) tarafından, {sistem} işletim sisteminden erişildi.")
            elif konu !=None and eposta==None:
                print(f"{saat}'de '{konu}', {alanadi} (IP: {ip}), {sistem} işletim sisteminden erişildi.")
            elif konu==None and eposta !=None:
                print(f"{saat}'de {eposta} (Adres: {alanadi}, IP: {ip}) tarafından, {sistem} işletim sisteminden erişildi.")
            else:
                print(f"{saat}'de {alanadi} (IP: {ip}), {sistem} işletim sisteminden erişildi.")
            return send_from_directory(".", "...")
        elif not (dosya in dosyalar):
            if konu !=None and eposta !=None:
                print(f"{saat}'de '{dosya}' (Konu:'{konu}'), {eposta} (Adres: {alanadi}, IP: {ip}) tarafından, {sistem} işletim sisteminden istendi ancak bulunamadı.")
            elif konu !=None and eposta==None:
                print(f"{saat}'de '{dosya}' (Konu:'{konu}'), {alanadi} (IP: {ip}), {sistem} işletim sisteminden istendi ancak bulunamadı.")
            elif konu==None and eposta !=None:
                print(f"{saat}'de '{dosya}', {eposta} (Adres: {alanadi}, IP: {ip}) tarafından, {sistem} işletim sisteminden istendi ancak bulunamadı.")
            else:
                print(f"{saat}'de '{dosya}', {alanadi} (IP: {ip}), {sistem} işletim sisteminden istendi ancak bulunamadı.")
            return send_from_directory(".", "...")
    elif tarayici!=None and sistem==None:
        if dosyagoster==False and (dosya in dosyalar):
            if konu !=None and eposta !=None:
                print(f"{saat}'de '{konu}', {eposta} (Adres: {alanadi}, IP: {ip}) tarafından, {tarayici} üzerinden açıldı.")
            elif konu !=None and eposta==None:
                print(f"{saat}'de '{konu}', {alanadi} (IP: {ip}), {tarayici} üzerinden açıldı.")
            elif konu==None and eposta !=None:
               print(f"{saat}'de '{dosya}', {eposta} (Adres: {alanadi}, IP: {ip}) tarafından, {tarayici} üzerinden açıldı.")
            else:
                print(f"{saat}'de '{dosya}', {alanadi} (IP: {ip}), {tarayici} üzerinden açıldı.")
            return send_from_directory(".", dosya)
        elif dosyagoster and (dosya in dosyalar):
            if konu !=None and eposta !=None:
                print(f"{saat}'de '{dosya}' (Konu:'{konu}'), {eposta} (Adres: {alanadi}, IP: {ip}) tarafından, {tarayici} üzerinden açıldı.")
            elif konu !=None and eposta==None:
                print(f"{saat}'de '{dosya}' (Konu:'{konu}'), {alanadi} (IP: {ip}), {tarayici} üzerinden açıldı.")
            elif konu==None and eposta !=None:
                print(f"{saat}'de '{dosya}', {eposta} (Adres: {alanadi}, IP: {ip}) tarafından, {tarayici} üzerinden açıldı.")
            else:
                print(f"{saat}'de '{dosya}', {alanadi} (IP: {ip}), {tarayici} üzerinden açıldı.")
            return send_from_directory(".", dosya)
        elif dosya=="...///...":
            if not erisimgoster:
                None
            elif konu !=None and eposta !=None:
                print(f"{saat}'de '{konu}', {eposta} (Adres: {alanadi}, IP: {ip}) tarafından, {tarayici} üzerinden erişildi.")
            elif konu !=None and eposta==None:
                print(f"{saat}'de '{konu}', {alanadi} (IP: {ip}), {tarayici} üzerinden erişildi.")
            elif konu==None and eposta !=None:
                print(f"{saat}'de {eposta} (Adres: {alanadi}, IP: {ip}) tarafından, {tarayici} üzerinden erişildi.")
            else:
                print(f"{saat}'de {alanadi} (IP: {ip}), {tarayici} üzerinden erişildi.")
            return send_from_directory(".", "...")
        elif not (dosya in dosyalar):
            if konu !=None and eposta !=None:
                print(f"{saat}'de '{dosya}' (Konu:'{konu}'), {eposta} (Adres: {alanadi}, IP: {ip}) tarafından, {tarayici} üzerinden istendi ancak bulunamadı.")
            elif konu !=None and eposta==None:
                print(f"{saat}'de '{dosya}' (Konu:'{konu}'), {alanadi} (IP: {ip}), {tarayici} üzerinden istendi ancak bulunamadı.")
            elif konu==None and eposta !=None:
                print(f"{saat}'de '{dosya}', {eposta} (Adres: {alanadi}, IP: {ip}) tarafından, {tarayici} üzerinden istendi ancak bulunamadı.")
            else:
                print(f"{saat}'de '{dosya}', {alanadi} (IP: {ip}), {tarayici} üzerinden istendi ancak bulunamadı.")
            return send_from_directory(".", "...")
    elif tarayici==None and sistem==None:
        if dosyagoster==False and (dosya in dosyalar):
            if konu !=None and eposta !=None:
                print(f"{saat}'de '{konu}', {eposta} (Adres: {alanadi}, IP: {ip}) tarafından üzerinden açıldı.")
            elif konu !=None and eposta==None:
                print(f"{saat}'de '{konu}', {alanadi} (IP: {ip}) üzerinden açıldı.")
            elif konu==None and eposta !=None:
               print(f"{saat}'de '{dosya}', {eposta} (Adres: {alanadi}, IP: {ip}) tarafından üzerinden açıldı.")
            else:
                print(f"{saat}'de '{dosya}', {alanadi} (IP: {ip}) üzerinden açıldı.")
            return send_from_directory(".", dosya)
        elif dosyagoster and (dosya in dosyalar):
            if konu !=None and eposta !=None:
                print(f"{saat}'de '{dosya}' (Konu:'{konu}'), {eposta} (Adres: {alanadi}, IP: {ip}) tarafından açıldı.")
            elif konu !=None and eposta==None:
                print(f"{saat}'de '{dosya}' (Konu:'{konu}'), {alanadi} (IP: {ip}) açıldı.")
            elif konu==None and eposta !=None:
                print(f"{saat}'de '{dosya}', {eposta} (Adres: {alanadi}, IP: {ip}) tarafından üzerinden açıldı.")
            else:
                print(f"{saat}'de '{dosya}', {alanadi} (IP: {ip}) üzerinden açıldı.")
            return send_from_directory(".", dosya)
        elif dosya=="...///...":
            if not erisimgoster:
                None
            elif konu !=None and eposta !=None:
                print(f"{saat}'de '{konu}', {eposta} (Adres: {alanadi}, IP: {ip}) tarafından üzerinden erişildi.")
            elif konu !=None and eposta==None:
                print(f"{saat}'de '{konu}', {alanadi} (IP: {ip}) üzerinden erişildi.")
            elif konu==None and eposta !=None:
                print(f"{saat}'de {eposta} (Adres: {alanadi}, IP: {ip}) tarafından üzerinden erişildi.")
            else:
                print(f"{saat}'de {alanadi} (IP: {ip}) üzerinden erişildi.")
            return send_from_directory(".", "...")
        elif not (dosya in dosyalar):
            if konu !=None and eposta !=None:
                print(f"{saat}'de '{dosya}' (Konu:'{konu}'), {eposta} (Adres: {alanadi}, IP: {ip}) tarafından istendi ancak bulunamadı.")
            elif konu !=None and eposta==None:
                print(f"{saat}'de '{dosya}' (Konu:'{konu}'), {alanadi} (IP: {ip}) üzerinden istendi ancak bulunamadı.")
            elif konu==None and eposta !=None:
                print(f"{saat}'de '{dosya}', {eposta} (Adres: {alanadi}, IP: {ip}) tarafından üzerinden istendi ancak bulunamadı.")
            else:
                print(f"{saat}'de '{dosya}', {alanadi} (IP: {ip}) üzerinden istendi ancak bulunamadı.")
            return send_from_directory(".", "...")
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
        getLogger("werkzeug").disabled=True
    key=('Sunucu.crt', 'Sunucu.key')
    sunucu.run(host='0.0.0.0',port=sunucuport,threaded=True,debug=debug) # ,ssl_context='adhoc' Sadece HTTPS # ,threaded=True Çoklu İstekd