import random
log_list=[]
pas_list=[]
def login(n: str,l:list):
    """Sisestatud kasutaja nimi otsing 

    Tagastab olemasolek järjendis bool formaadis
    :param str n: otsitav sõna
    :param list l: järjend
    :rtype: bool 

   """
    if n in l:
        t=True 
    else:
        t=False 
    return t

def auto_reg():
    """Salasõna genireerimine
    
     Tagastab salasõna str formaadis
    
     :rtype: str
   
     """
    str0=".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0+str1+str2+str3
    ls=list(str4)
    random.shuffle(ls)
    pas = ''.join([random.choice(ls) for x in range(12)]) # Извлекаем из списка 12 произвольных значений
    return pas
p=auto_reg()
print(p)

def ise_reg():
    pass

def avtor(l: list, p:list):
    n=input('Sisesta oma kasutaja nimi autoriseerimiseks: ')
    t=login(n,l)
    while t!=True:
        n=input('Sisesta veel kord oma nimi:')
        t=login(n,l)
    pas=input('Sisesta salasõna')
    t=login(pas,p)
    if t==True and l.index(n)==p.index(pas):
        t=True
    else:
        t=False
    return t 

def reg(v: str,l: list, p: list):
    """Inimeste registreerimine

    Tagastab loginide ja salasõnade listid 

    :param str v: kasutaja parooli loomise viis
    :rtype: list,list
   
    """
    


   
    t=login(input('Sisesta oma kasutaja nimi:'))
   
    while True:
        try:
            t=login(input('Sisesta veel kord oma kasutaja nimi, andmebaasis on selline nimi:'))
        except:
        
        if v=='a':
            pas=auto_reg()
        else:
            ise_reg()
        return l,p

while 1:
    print('Regisreerimine, autoriseerimine või välja')
    v=input('Sinu valik:')
    if v=='r':
        reg(input('Auto või ise ?'),log_list,pas_list)
    elif v=='a':
        t=avtor(log_list,pas_list) #True,false
        if t():
            print('Tere tulemast!')
        else:
            v=input('Kas tahad registreerida?')
            if v=='jah':
                print('Registreerimine')
                reg(input('Auto või ise?'),log_list,pas_list)
            else:
                pass
    else:
        break
