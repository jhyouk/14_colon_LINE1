#args1: input
#args2: bam_path_list

#191026 copied and edited from DB6 filter3 file, bam list as sys.argv[2], run_serial calling and editing, lowDp NA


import sys,os,gzip
pos_file=open(sys.argv[1])
bam_list=sys.argv[2] 
id_list_path=sys.argv[3]
sampleN=int(sys.argv[4])  # sample  number for pileup
lowDpCO=5  # minimal readcount for calculating VAF

out_file=open(sys.argv[1]+'.mpu', 'w')
pos_line=pos_file.readline().strip()
while pos_line:
	if pos_line[0]=='#':
		'blank'
	else:
		pos_indi=pos_line.split('\t')
		chr1=pos_indi[0]
		pos1=pos_indi[1]
		cmd='samtools mpileup -AB -Q 20 -q 20 -d 100000 -b '+bam_list+' -f /home/users/data/01_reference/human_g1k_v37/human_g1k_v37.fasta -r '+chr1+':'+pos1+'-'+pos1+' 2> /dev/null'
		print(cmd)
		res_file=os.popen(cmd)
		res_line=res_file.readline().strip()
		out_file.write(res_line+'\n')
	pos_line=pos_file.readline().strip()
out_file.close()

cmd='python /home/users/sypark/01_Python_files/normal_matrix/pileup_calling_snv.py '+sys.argv[1]+'.mpu '+str(sampleN)
os.system(cmd)

in_file=open(sys.argv[1])
out_file=open(sys.argv[1]+'.'+str(sampleN)+'sCall','w')
in_line=in_file.readline().strip()
n=0
nt_list=['A','G','C','T']
ref_file=open(sys.argv[1]+'.mpu.snv')
ref_line=ref_file.readline().strip()
ref_indi=ref_line.split('\t')
id_file=open(id_list_path)
id_line=id_file.readline().strip()
header_list=[]
while id_line:
	header_list=header_list+[id_line+'_dp',id_line+'_ref',id_line+'_var',id_line+'_vafpct']
	id_line=id_file.readline().strip()

if len(header_list) != sampleN*4:
	print('ERROR: inconsisten sampleN and id_list')
	sys.exit(1)

while in_line:
	in_indi=in_line.split('\t')
	if in_line[0:6]=='#CHROM':
		out_file.write(in_line+'\t'+'\t'.join(header_list)+'\n')
		in_line=in_file.readline().strip()
	elif in_line[0]=='#':
		out_file.write(in_line+'\n')
		in_line=in_file.readline().strip()
	elif ref_line=='':
		out_file.write(in_line+'\t'+'\t'.join(['NA']*sampleN)+'\n')
		in_line=in_file.readline().strip()
	elif in_indi[3] not in nt_list:
		out_file.write(in_line+'\t'+'\t'.join(['NA']*sampleN)+'\n')
		in_line=in_file.readline().strip()
	else:
		ref_indi=ref_line.split('\t')
		chr1=int(in_indi[0].replace('X','23').replace('Y','24'))
		chr2=int(ref_indi[0].replace('X','23').replace('Y','24'))
		refnt=in_indi[3]
		varnt=in_indi[4]
		ref_list=ref_indi[3:]
		if chr1==chr2:
			if int(in_indi[1])==int(ref_indi[1]):
				out_file.write(in_line)
				for info in ref_list:
					c_dp=int((info.split('dp=')[1]).split(';')[0])
					if refnt+'=' in info:
						c_ref=int((info.split(refnt+'=')[1]).split(';')[0])
					else:
						c_ref=0
					if varnt+'=' in info:
						c_var=int((info.split(varnt+'=')[1]).split(';')[0])
					else:
						c_var=0
					if c_dp==0:
						c_vaf='NA'
					else:
						c_vaf=str(round(c_var*100/float(c_dp),2))
					#c_info_list=['dp='+str(c_dp),'ref='+str(c_ref),'var='+str(c_var),'vaf='+c_vaf]
					if c_dp < lowDpCO:
						c_vaf='NA'
					c_info_list=[str(c_dp), str(c_ref), str(c_var), str(c_vaf)]
					c_info='\t'.join(c_info_list)
					out_file.write('\t'+c_info)
				out_file.write('\n')
				in_line=in_file.readline().strip()
				ref_line=ref_file.readline().strip()
				n+=1
			elif int(in_indi[1])>int(ref_indi[1]):
				ref_line=ref_file.readline().strip()
				n+=1
			elif int(in_indi[1])<int(ref_indi[1]):
				out_file.write(in_line+'\t'+'\t'.join(['NA']*sampleN)+'\n')
				in_line=in_file.readline().strip()
		elif chr1>chr2:
			ref_line=ref_file.readline().strip()
			n+=1
		elif chr1<chr2:
			out_file.write(in_line+'\t'+'\t'.join(['NA']*sampleN*4)+'\n')
			in_line=in_file.readline().strip()
	if n!=0 and n%10000000==0:
		print(n)
