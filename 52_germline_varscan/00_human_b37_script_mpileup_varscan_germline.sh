#!/bin/bash
set -e
sampleID=$1
bam=$2
log=$1.mpileup.log

echo "mpileup for $1" > $log
(samtools mpileup -B -Q 20 -q 20 -f /home/users/jhyouk/99_reference/human/GRCh37/human_g1k_v37.fasta $bam -o $1.mpileup) &>> $log || { c=$?;echo "Error";exit $c; }
echo "done" >> $log
echo "varscan for $1" >> $log
(java -Xmx12g -jar /home/users/tools/varscan2.4.2/VarScan.v2.4.2.jar mpileup2snp $1.mpileup --min-var-freq 0.01 --output-vcf 1 1> $1.varscan.snp.vcf) 2>> $log || { c=$?;echo "Error";exit $c; }
echo "varscan done" >> $log
echo "remove mpileup file" >> $log
rm $1.mpileup
echo "all done" >> $log
