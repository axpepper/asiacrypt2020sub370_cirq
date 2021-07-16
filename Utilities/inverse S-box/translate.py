import re
import sys

filename = sys.argv[1]

with open('preamble.py', 'r') as file1:
	data1=file1.read().replace('\n\n','\n')
	print(data1)


with open(filename, 'r') as file:
	data = file.readlines()

for i in data:
	#i = re.sub(r";.*$",'',i)
	#DELETES all following ;
	i = re.sub(r"#.*$",'',i)
	i = i.replace(";",'') #smi-colon handling
	if "//" in i:
		i,cmt = i.split('//') 
		print("    #" + cmt) #comment handling
	i = i.replace("/*", "'''")
	i = i.replace("*/", "'''")
	if "j = 1" in i:
		i=''
	if " = j" in i:
		print(re.sub(r"([A-Z].*\])", r"circuit.append(cirq.X(" + r"\1"+"))", i.split('=')[0]))
	if "void" in i:
		i = i.replace("void", "def")
		i = i.replace("[]", "")
		i = i.replace("int ", "")
		i = i.replace(", j", "")
		i = i.replace(")","):")
		print(i)
	else:
		if '*' not in i and 'void' not in i:
			if '^' in i and '&' not in i:
				temp = i.replace(" ", "").replace("\n",'')
				temp = temp.split('=')[1]
				gates = temp.split('^')
				for j in gates[1:]:
					print('    '+'circuit.append(cirq.CNOT({},{}))'.format(j,gates[0]))
			if '^' in i and '&' in i:
				temp=i.replace("(", "").replace("\n",'')
				temp=temp.replace(")", "").replace("\n",'')
				temp=temp.replace(" ", "").replace("\n",'')
				target,inputs = temp.split('=')
				Toffoli_inputs = inputs.split('^')[0].split('&')
				cnot_inputs = inputs.split('^')[1:-1]
				print('    '+'circuit.append(cirq.TOFFOLI({},{},{}))'.format(Toffoli_inputs[0], Toffoli_inputs[1], target))
				for j in cnot_inputs:
					print('    '+'circuit.append(cirq.CNOT({},{}))'.format(j,target))
				
		else:
			if i != '':
				print(i)

with open('postamble.py', 'r') as file2:
	data2=file2.read().replace('\n\n','\n')
	print(data2)