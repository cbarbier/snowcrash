import sys
t = [0x66, 0x34, 0x6b, 0x6d, 0x6d, 0x36, 0x70, 0x7c, 0x3d, 0x82, 0x7f, 0x70, 0x82, 0x6e, 0x83, 0x82, 0x44, 0x42, 0x83, 0x44, 0x75, 0x7b, 0x7f, 0x8c, 0x89]

i = 0

while (i < len(t)):
	sys.stdout.write( chr(t[i] - i))
	i +=1