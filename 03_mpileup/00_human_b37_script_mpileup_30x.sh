#!/bin/bash
set -e
sampleID=$1
log=$1.mpileup.log

echo "mpileup for $1" > $log
(samtools mpileup -B -Q 20 -q 20 -f /home/users/jhyouk/99_reference/human/GRCh37/human_g1k_v37.fasta /home/users/team_projects/colon_LINE1/02_bam/$1.s.md.bam -o $1.mpileup) &>> $log || { c=$?;echo "Error";exit $c; }
echo "done" >> $log

echo "get coverage" >> $log
(python 05_hg19_get_coverage.py $1.mpileup) &>> $log || { c=$?;echo "Error";exit $c; }
echo "done" >> $log
echo "calculate stats"
(python 06_calculate_stats.py $1.mpileup.100kbcov) &>> $log || { c=$?;echo "Error";exit $c; }
(mv $1.mpileup.100kbcov ../04_sequenza) &>> $log || { c=$?;echo "Error";exit $c; }
(mv $1.mpileup.100kbcov.covstat ../04_sequenza) &>> $log || { c=$?;echo "Error";exit $c; }
(rm $1.mpileup) &>> $log || { c=$?:echo "Error";exit $c; }
echo "finish" >> $log
