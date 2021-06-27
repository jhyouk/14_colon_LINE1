sampleID=$1
bam=$2

/home/users/tools/gatk/gatk-4.0.0.0/gatk HaplotypeCaller -R /home/users/jhyouk/99_reference/human/GRCh37/human_g1k_v37.fasta -I $bam -O $sampleID.hc.snp.indel.vcf -mbq 20 -RF MappingQualityReadFilter --java-options '-Xms8g -Xmx12g' &> $sampleID.out
