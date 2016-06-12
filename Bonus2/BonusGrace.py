import sys

JUJU = "JUJU"
MALCHO = "MALCHO"
KAA = 'import sys\n\nJUJU = "JUJU"\nMALCHO = "MALCHO"\nKAA = %s;\n\n#\tMaster Viper\n\nfd=open("./grace_kid.py", "w+")\nfd.write(KAA%%`KAA`)\nfd.close()\n';

#	Master Viper

fd=open("./grace_kid.py", "w+")
fd.write(KAA%`KAA`)
fd.close()
