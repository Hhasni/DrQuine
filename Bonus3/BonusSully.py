import sys
import os

def function():
	i = 5
	name = 'Sully_'
	if sys.argv[0].find('_') != -1 and i >= 0:
		i -= 1
	if i >= 0:
		tmp = name + str(i) + '.py'
		of = open(tmp, 'wb')
		a="import sys\nimport os\n\ndef function():\n\ti = %d\n\tname = 'Sully_'\n\tif sys.argv[0].find('_') != -1 and i >= 0:\n\t\ti -= 1\n\tif i >= 0:\n\t\ttmp = name + str(i) + '.py'\n\t\tof = open(tmp, 'wb')\n\t\ta=%s;\n\t\tprint >> of, a %% (i,`a`)\n\t\tof.close()\n\t\tos.system('python '+tmp)\n\tsys.exit(0)\n\nfunction();";
		print >> of, a % (i,`a`)
		of.close()
		os.system('python '+tmp)
	sys.exit(0)

function();
