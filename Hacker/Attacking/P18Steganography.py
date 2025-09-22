
from PIL import Image
import wave
import sys
import os
import os

def CheckFile(file):
    if not os.path.isfile(file):
        print("[X] Please enter a correct file path.")
        return False

    if not file.lower().endswith((".png", ".bmp")):
        print("[X] Please enter a file with .png or .bmp format!")
        return False

    return True

def CheckA(file):
    if not os.path.isfile(file):
        print("[X] Please enter a correct file path.")
        return False

    if not file.lower().endswith(".wav"):
        print("[X] Please enter a file with .wav format!")
        return False

    return True

def HideData(Ipath, message, outp):
	print("Worked")
	img=Image.open(Ipath)
	pix=img.load()
	message+=chr(0)
	bit = ''.join(format(ord(c), '08b') for c in message)	
	w,h=img.size
	c=0
	for y in range(h):
		for x in range(w):
			r,g,b=pix[x,y]
			print(r,g,b)
			nc = []
			for color in [r,g,b]:
				if c < len(bit):
					color = (color & ~1 ) | int(bit[c])
					c+=1
				nc.append(color)
			pix[x, y] = tuple(nc)
			if c >= len(bit):
				break
		if c >= len(bit):
			break
	img.save(outp)
	print("[*] Message hidden in image:", outp)
def DecodeI(ImgData):
	img=Image.open(ImgData)
	pix=img.load()
	w,h=img.size
	bit=""
	c=0
	char=[]
	for y in range(h):
		for x in range(w):
			r,g,b=pix[x,y]
			for color in [r,g,b]:
				bit+=str(color & 1)
	for i in range(0,len(bit),8):
		byte=bit[i:i+8]
		if len(byte) < 8:
			break
		c=chr(int(byte,2))
		if c == chr(0):
			break
		char.append(c)
	print("[**] Hidden MSG: ","".join(char))

def AudioD(AuF,mes,AuO):
	mes+=chr(0)
	bit = ''.join(format(ord(c), '08b') for c in mes)
	c=0
	with wave.open(AuF,"rb") as audio:
		par=audio.getparams()
		frames=bytearray(audio.readframes(audio.getnframes()))
	for i in range(len(frames)):
		if c < len(bit):
			frames[i] = (frames[i] & ~1) | int(bit[c])
			c+=1
		else:
		 	break
	with wave.open(AuO,"wb") as save:
		save.setparams(par)
		save.writeframes(frames)
	print("[**] Message hidden in audio:", AuO)

def DecodeAudio(AuF):
	with wave.open(AuF,"rb") as audio:
		frames=bytearray(audio.readframes(audio.getnframes()))
		bit=''
		for b in frames:
			bit+=str(b & 1)
		MES=[]
		for i in range(0,len(bit),8):
			b=bit[i:i+8]
			if len(b) < 8:
				break
			c = chr(int(b,2))
			if c == chr(0):
				break
			MES.append(c)
		print("[**] Hidden MSG: ","".join(MES))
def SryphtoSecretData():
    print("====== Sryphto Secret Data ======")
    print("1. Hide message in Image")
    print("2. Decode message from Image")
    print("3. Hide message in Audio")
    print("4. Decode message from Audio")
    print("4. Decode message from Audio")
    print("0. Exit")
    while True:
        choice = input("Choose option (0-4): ").strip()

        if choice == "1":
            file = input("Enter image file path: ").strip()
            if CheckFile(file):
                secret = input("Enter your secret message: ").strip()
                output = os.path.splitext(file)[0] + "-Out.png"
                HideData(file, secret, output)

        elif choice == "2":
            file = input("Enter encoded image file: ").strip()
            if CheckFile(file):
                DecodeI(file)

        elif choice == "3":
            file = input("Enter WAV file path: ").strip()
            if CheckA(file):
                secret = input("Enter your secret message: ").strip()
                output = os.path.splitext(file)[0] + "-Out.wav"
                AudioD(file, secret, output)

        elif choice == "4":
            file = input("Enter encoded WAV file: ").strip()
            if CheckA(file):
                DecodeAudio(file)
        elif choice == "":
        	continue
        elif choice == "0":
            print("[*] Exiting...")
            break

        else:
            print("[X] Invalid choice!")
