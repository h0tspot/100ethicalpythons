import subprocess
import optparse
import re

def get_arguments():
   parser = optparse.OptionParser()
   parser.add_option("-i", "--interface",dest = "interface",help = "enter the interface")
   parser.add_option("-m", "--mac",dest = "new_mac",help = "enter the new mac address")
   (options, arguments) = parser.parse_args()
   if not options.interface :
   	 parser.error("[-] Please specify an interface,use --help for more info")
   elif not options.new_mac :
     parser.error("[-] Please specify a mac address,use --help for more info")
   return options


def change_mac(interface,new_mac) :
   subprocess.call(["ifconfig", interface ,"down"])
   subprocess.call(["ifconfig", interface ,"hw","ether",new_mac])
   subprocess.call(["ifconfig", interface , "up"]) 

def get_current_mac(interface):
  ifconfig_check = subprocess.check_output(["ifconfig",interface])
  mac_checker = re.compile(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w').search(ifconfig_check)
  if mac_checker:
	  return mac_checker.group(0)
  else:
      print("[] Could not find the mac address")	


options = get_arguments()

current_mac = get_current_mac(options.interface)
print ("The current mac = " + str(current_mac))

change_mac(options.interface,options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
   print("The mac address was changed to" + current_mac)
else:
   print("mac address did not change")


