import os
h = ""
p = ""
try:

	os.system("git clone https://github.com/IqbalDev/insta_dev")
	os.system("rm -rf insta_dev.py")
	os.system("cp -f insta_dev/insta_dev.py \\.")
	os.system("rm -rf insta_dev")
	os.system("chmod 777 *")
	print h+"\n Sukses Update Tool.."+p+">_<\n"
except:
	print "\n Perangkat Tidak Suport\n"