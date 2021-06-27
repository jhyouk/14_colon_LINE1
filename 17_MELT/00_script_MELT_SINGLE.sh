sampleID=$1

java -Xms8g -Xmx12g -jar /home/users/jhyouk/tools/MELTv2.2.0/MELT.jar Single \
-bamfile /home/users/team_projects/Radiation_signature/05_bam_human_sample_GRCh37/$sampleID.bam \
-t /home/users/jhyouk/tools/MELTv2.2.0/mei_list.txt \
-h /home/users/jhyouk/99_reference/human/GRCh37/human_g1k_v37.fasta \
-n /home/users/jhyouk/tools/MELTv2.2.0/add_bed_files/1KGP_Hg19/hg19.genes.bed \
-bowtie /usr/local/bin/bowtie2 \
-samtools /usr/local/bin/samtools \
-w /home/users/jhyouk/14_colon_LINE1/17_MELT &> $1.log
