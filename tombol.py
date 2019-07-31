import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
print(a+'\t  Shorcut untuk memunculkan tombol tersembunyi')
print(b+'\t    Hack-G')
print('\t Cyber Tapin')
print(a+'+'*40)
print('\nTunggu Sedang Proses..')
sleep(1)
print(b+'\n[!] making termux properties directory..')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[!]Success !')
sleep(1)
print(b+'\n[!] Making setup file..')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
print(a+'[!] Success !')
sleep(1)
print(b+'\n[!] Setting up..')
sleep(2)
os.system('termux-reload-settings')
print(a+'[!] Successfully !! ^^'+c+'\n\nSELAMAT MENJALANKAN TERMUX DENGAN TOMBOL TERSEMBUNYI :*\n\n')

echo $me"    ───────████████──────██████████████████"
echo $me"    ──────█────────█─────█▓███▓██▓█▓█▓█▓▓▓█"
echo $me"    ─────█─▄▀█──█▀▄─█────█▓███▓██▓█▓▓██▓▓██"
echo $me"    ────▐▌──────────▐▌───█▓███▓▓█▓█▓█▓█▓▓▓█"
echo $me"    ────█▌▀▄──▄▄──▄▀▐█───██████████████████"
echo $me"    ───▐██──▀▀──▀▀──██▌──█▓█▓██▓██▓▓█▓█▓███"
echo $me"    ──▄████▄──▐▌──▄████▄─█▓▓▓█▓▓▓█▓██▓▓████"
echo $me"    ─████████▄──▄█████████▓█▓█▓█▓█▓▓█▓█▓███"
echo $me"    ─██████████████████████████████████████"
echo $cy "╔═══════════════════•ೋೋ•════════════════════╗"
echo $i  "  Penulis        : Cyber Tapin"
echo $i  "  Whatsapp       : 081258581861"
echo $i  "  YOUTUBE        : Hack G (Jangan Lupa Subscribe)"
echo $i  "   Hack G (Cyber Tapin) Anonymous Indonesia"
echo $cy "╚═══════════════════•ೋೋ•════════════════════╝"

#SILAHKAN KALIAN KETIK "EXIT" LALU ENTER
#ATAU KELUAR DARI TERMUX LALU MASUK KEMBALI
#LIHAT DIBAGIAN TOMBOL DIATAS
