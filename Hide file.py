import ctypes

attributes = 0x02

#hide_file = input('Text the directory here: ')

ret = ctypes.windll.kernel32.SetFileAttributesW(r'D:\cursopython' , attributes)

if ret:
    print('The file was hided')
else:
    raise ctypes.WinError()
