#arg1: input
#arg2: total CE id list (id1 \n id2 \n id3 \n ...) 
#arg3: excluded id list (id1 \n id2 \n id3 \n ...)

import sys
print(sys.argv[1])

id_file=open(sys.argv[2])
id_line=id_file.readline().strip()
id_list=[]
while id_line:
	id_list.append(id_line)
	id_line=id_file.readline().strip()


ex_list=[]
ex_file=open(sys.argv[3])
ex_line=ex_file.readline().strip()
while ex_line:
	ex_list.append(ex_line)
	ex_line=ex_file.readline().strip()

in_file=open(sys.argv[1])
out_file=open(sys.argv[1]+'.g_fi','w')
in_line=in_file.readline().strip()
n=0; m=0
while in_line:
	if in_line[0]=='#':
		out_file.write(in_line+'\n')
	else:
		n +=1
		in_indi=in_line.split('\t')
		nr_info=in_indi[47]
		loh_info=in_indi[49]
		nr3=int(nr_info.split(';')[3])
		nr3_ids=nr_info.split(';')[4:]
		loh_ids=loh_info.split(';')
		if len(set(id_list) - set(ex_list) -set(nr3_ids) - set(loh_ids)) == 0:
			'blank'
		else:
			m +=1
			out_file.write(in_line+'\n')
	in_line = in_file.readline().strip()

print(n)
print(m)
