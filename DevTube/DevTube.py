from time import time
import os
from pytube import YouTube
import time
import subprocess

os.makedirs("C:\YouTube Downloaded",exist_ok=True)
os.chdir("C:\YouTube Downloaded")
print(f"Twój bierzący katalog to ${os.getcwd()}")
#Wstęp
print("Witaj w programie DevTube - YouTube Downloader Dev Studio 2022")
time.sleep(3)
#Wybieranie filmu
print("Wklej Link z YouTube")
link = input()
yt = YouTube(link)
print("Czy film jaki chcesz pobrać to")
print(yt.title)
print("Wpisz tak lub nie")
inputPytanie = input()
if  inputPytanie == str("tak"):
    print("ok")

else:
    print("Program zostanie uruchomiony ponownie za 5 sekund")
    os.system("python main.py")
    time.sleep(5)
    exit()
# Ustawianie Jakości
print("Wybierz Cyfre")
time.sleep(0.3)
print("1 - Najwyższa Dostępna jakość (mp4)")
time.sleep(0.3)
print("2 - Najniższa dostępna jakość (mp4)")
time.sleep(0.3)
print("3 - Tylko audio (mp3)")
InputJakość = input("")
if InputJakość == str("1"):
    ytvideodownload = yt.streams.get_highest_resolution()
if InputJakość == str("2"):
    ytvideodownload = yt.streams.get_lowest_resolution()
if InputJakość == str("3"):
    ytvideodownload = yt.streams.get_audio_only()

# Skrypt Pobierający
ytvideodownload.download()
print("Twój film został pobrany!")
time.sleep(0.1)
subprocess.Popen('explorer "C:\YouTube Downloaded"')
time.sleep(0.1)
print("Po więcej informacji na temat Dev Studio")
time.sleep(0.1)
print("lub w celu zobaczenia kanału YouTube/wysłania donejta")
time.sleep(0.1)
print("wejdź na stronę www.devstudio.com.pl")
input("wciśnij dowolny przycisk aby wyłączyć aplikacje")





