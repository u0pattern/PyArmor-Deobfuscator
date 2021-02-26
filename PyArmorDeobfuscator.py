import argparse,sys,os,uncompyle6,py_compile

def find_pytransform__init__file(file): # please make sure you have _pytransform.dll and __init__.py in /dist/pytransform/ directory !!!
	if os.path.isfile(file):
		dir = os.path.dirname(os.path.realpath(file))
		if os.path.isfile(dir + '/dist/pytransform/_pytransform.dll'):
			if os.path.isfile(dir + '/dist/pytransform/__init__.py'):
				return "True"
			else:
				return "[-] __init__.py file not found [-]"
		else:
			return "[-] _pytransform.dll file not found [-]"

parser = argparse.ArgumentParser(description="[+] PyArmor Deobfuscator by u0pattern (Mohammed Muteb) [+]")
parser.add_argument('-f', required=True, default=None, help='Add the Armor file [ex: obfuscated.py]')
parser.add_argument('-o', required=True, default=None, help='Add the Output file [ex: deobfuscated.py]')
args = vars(parser.parse_args())
result = find_pytransform__init__file(args['f'])
if result == "True":
	# Compile to Byte Code
	# https://docs.python.org/2/library/py_compile.html
	# https://docs.python.org/3/library/py_compile.html
	py_compile.compile(args['f'])
	
	with open(args['o'], 'w') as output:
		# decompile the bytecode file using uncompyle6
		# https://pypi.org/project/uncompyle6/
		# decompile_file function :-
		#      https://github.com/rocky/python-uncompyle6/blob/master/uncompyle6/main.py#L166
		theDecompiler = uncompyle6.decompile_file(args['f']+'c', output)
		os.remove(args['f']+'c')
		print("[+] the deobfuscated code saved here "+os.path.dirname(os.path.realpath(args['o']))+"/"+args['o']+" [+]")
		
else:
	print(result)
