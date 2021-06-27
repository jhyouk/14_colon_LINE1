#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os, sys
temp_list = os.listdir("/home/users/jhyouk/14_colon_LINE1/51_haplotypecaller/")
file_list = []
pre_list = []
for i in temp_list:
    if 'HC15-' not in i and '.out' not in i and '.idx' not in i and '-' in i and '.hc.snp.indel.vcf' in i:
        pre_list.append(i)
print len(pre_list)

for input_fn in pre_list:
    print input_fn
    input_file = file("/home/users/jhyouk/14_colon_LINE1/51_haplotypecaller/%s" % input_fn)
    output_file =file("/home/users/jhyouk/14_colon_LINE1/51_haplotypecaller/%s" % input_fn.replace(".indel",""), 'w')
    output_indel_file =file("/home/users/jhyouk/14_colon_LINE1/51_haplotypecaller/%s" % input_fn.replace(".snp",""), 'w')
    
    input_line = input_file.readline().strip()
    while input_line[0:2] == '##':
        input_line = input_file.readline().strip()
    while input_line[0:1] == '#':
        output_file.write(input_line+'\n')
        output_indel_file.write(input_line+'\n')
        input_line = input_file.readline().strip()
        
    while input_line:
        input_split = input_line.split('\t')
        
        if len(input_split[3]) == len(input_split[4]):
            output_file.write(input_line+'\n')
        else:
            output_indel_file.write(input_line+'\n')
            
        input_line = input_file.readline().strip()            
            
        
    input_file.close()
    output_file.close()
    output_indel_file.close()
print 'THE END'

