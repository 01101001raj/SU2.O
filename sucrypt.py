import maincode as mc
import colorama as c
from colorama import Fore, Back, Style

c.init(autoreset=True)

print(Fore.RED  + Style.BRIGHT  + """
                                                            
 ___      _   _              
/ __|    | | | |    
\__ \    | |_| |
|___/     \__,_|    2.O   
                                 
                                                          """)

ch=int(input("1 for encryption and 2 for decryption"))
if ch==1:
  mc.encrypt()
elif ch==2:
  mc.decrypt()
else:
  print("enter only 1 and 2 no other elements")
