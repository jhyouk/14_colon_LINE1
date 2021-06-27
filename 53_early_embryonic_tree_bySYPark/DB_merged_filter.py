#Arg1: input
#Arg2: false snv list
#Arg3: nr1 cutoff


#191015 copied from DB6_merged_filter.py

import sys
in_file=open(sys.argv[1])
out_file=open(sys.argv[1]+'.fi','w')

f_file=open(sys.argv[2])
sn1_co=int(sys.argv[3])

f_line=f_file.readline().strip()
false_list=[]
while f_line:
        false_list.append(f_line)
        f_line=f_file.readline().strip()


in_line=in_file.readline().strip()
n=m=0
while in_line:
	if in_line[0]=='#':
		out_file.write(in_line+'\n')
	else:
		n +=1
		in_indi=in_line.split('\t')
		chr1=in_indi[0]
                pos1=in_indi[1]
                refnt=in_indi[3]
                altnt=in_indi[4]
		refmq=in_indi[12]
		varmq=in_indi[13]
		clipinfo=in_indi[18]
		insinfo=in_indi[19]
		delinfo=in_indi[20]
		varmm=in_indi[22]
		p1info=in_indi[25]
		p2info=in_indi[26]
		its_num=in_indi[45]
                its_sample=in_indi[46]
		sn_info=in_indi[47]
		blinfo=in_indi[48]
		idx='\t'.join([chr1,pos1,refnt,altnt])

		vclipv=float(clipinfo.split(';')[3])
		vinsv=float(insinfo.split(';')[3])
		vdelv=float(delinfo.split(';')[3])
		if p1info == 'NA':
			p1vaf=0
		else:
			p1vaf=float(p1info.split(';')[6])
		if p2info == 'NA':
			p2vaf=0
		else:
			p2vaf=float(p2info.split(';')[6])
		its_num=int(its_num)
		sn1=int(sn_info.split(';')[1])
		sn3=int(sn_info.split(';')[3])
		sn3_list=sn_info.split(';')[4:]

		if sn1-sn3 < 5 and sn3-its_num < 5 and sn1 < sn1_co and idx not in false_list:
			m+=1
			out_file.write(in_line+'\n')
	in_line=in_file.readline().strip()
print(n)
print(m)
