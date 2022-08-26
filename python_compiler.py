import marshal, time
#colors
BLACK   = '\033[30m'
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = '\033[39m'
def py():
    a=input("\033[32mtype file name :\033[39m ")
    x=open(a).read()
    b=compile(x,'','exec')
    c=marshal.dumps(b)
    d=open("encryptedByDEVH"+a,'w')
    d.write('import marshal\n')
    d.write('exec(marshal.loads('+repr(c)+'))')
    d.close()
    print("please wait....")
    time.sleep(3)
    print("File encrypted name: encryptedByDEVH_"+a)
    print('\033[36mThank you for using Follow me on my instagram : \033[31mhh__y')
print('''\033[33m
 ▄▄▄· ▄· ▄▌▄▄▄▄▄ ▄ .▄       ▐ ▄      ▄▄·       • ▌ ▄ ·.  ▄▄▄·▪  ▄▄▌  ▄▄▄ .▄▄▄  
▐█ ▄█▐█▪██▌•██  ██▪▐█▪     •█▌▐█    ▐█ ▌▪▪     ·██ ▐███▪▐█ ▄███ ██•  ▀▄.▀·▀▄ █·
 ██▀·▐█▌▐█▪ ▐█.▪██▀▐█ ▄█▀▄ ▐█▐▐▌    ██ ▄▄ ▄█▀▄ ▐█ ▌▐▌▐█· ██▀·▐█·██▪  ▐▀▀▪▄▐▀▀▄ 
▐█▪·• ▐█▀·. ▐█▌·██▌▐▀▐█▌.▐▌██▐█▌    ▐███▌▐█▌.▐▌██ ██▌▐█▌▐█▪·•▐█▌▐█▌▐▌▐█▄▄▌▐█•█▌
.▀     ▀ •  ▀▀▀ ▀▀▀ · ▀█▄▀▪▀▀ █▪    ·▀▀▀  ▀█▄▀▪▀▀  █▪▀▀▀.▀   ▀▀▀.▀▀▀  ▀▀▀ .▀  ▀
\033[31mMy website : \033[34mhttps://alhelfi.sofr.app  \033[36m |    \033[31mMy instagram : \033[34mhh__y ''')
py()
