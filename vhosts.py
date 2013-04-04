import os
import sys

#Path to httpd-vhosts.conf
vhostsPath = "/etc/apache2/extra/httpd-vhosts-test.conf"

#Path to hosts file
hostsFilePath = "/etc/hosts-test"

#Code snippet taken from
#http://stackoverflow.com/questions/5222333/authentication-in-python-script-to-run-as-root
euid = os.geteuid()
if euid != 0:
    print "You need to be the Superuser to make changes to these files..."
    args = ['sudo', sys.executable] + sys.argv + [os.environ]
    os.execlpe('sudo', *args)
#####

print("\n===== Example =====\n")
print("NameVirtualHost example.localhost:80")
print("<VirtualHost example.localhost:80>")
print("\tServerAdmin admin@localhost")
print("\tDocumentRoot \"/Users/Example/Sites/Example\"")
print("\tServerName example.localhost")
print("\tServerAlias example.localhost")
print("</VirtualHost>")
print("\n=====   END   =====\n")

domainName = raw_input("\nEnter the NameVirtualHost:\n")

serverAdmin = raw_input("\nEnter the server admin\n")

documentRoot = raw_input("\nEnter the path of your document root (without \'\"\'):\n")

serverName = raw_input("\nEnter the ServerName:\n")

serverAlias = raw_input("\nEnter the ServerAlias:\n")

with open(vhostsPath, "a") as myfile:
	myfile.write("\nNameVirtualHost " + domainName + "\n")
	myfile.write("<VirtualHost " + domainName + ">\n")
	myfile.write("\tServerAdmin " + serverAdmin + "\n")
	myfile.write("\tDocumentRoot \"" + documentRoot + "\"\n")
	myfile.write("\tServerName " + serverName + "\n")
	myfile.write("\tServerAlias " + serverAlias + "\n")
	myfile.write("</VirtualHost>\n")

print("\n=====\nVHosts Configured\n=====")

serverIP = raw_input("\nEnter the IP address for your server:\nEXAMPLE: 127.0.0.1\n")

with open(hostsFilePath, "a") as hostsFile:
	hostsFile.write("\n" + serverIP + " " + serverAlias)
	
print("\n=====\nEntry added to hosts file\n=====\n")

def shouldRestart():
	answer = raw_input('Would you like to restart Apache? yes/no\n')
	
	if answer == "Yes" or answer == "Y" or answer == "yes" or answer == "y":
		print("\n=====\nRestarting Apache\n=====")
		os.system('sudo apachectl restart')
	elif answer == "No" or answer =="N" or answer == "no" or answer == "n":
		print("\n=====\nYou should probably restart your Apache server\n=====")
	else :
		print("\n=====\nThat was a wierd response...\n=====\n")
		shouldRestart()

shouldRestart()
