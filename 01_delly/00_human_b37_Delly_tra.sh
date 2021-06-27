bam_pwd=$1
tumor=$2
normal=$3

(bcftools concat -a -O v -o $tumor.delly.vcf $tumor.DEL.bcf $tumor.DUP.bcf $tumor.INS.bcf $tumor.INV.bcf $tumor.TRA.bcf) &> $2.concat.out
#/home/users/tools/delly-0.7.6/delly/src/delly call -t TRA -q 15 -o $tumor.TRA.bcf -g /home/users/jhyouk/99_reference/human/GRCh37/human_g1k_v37.fasta $bam_pwd/$tumor.s.md.bam $bam_pwd/$normal.s.md.bam &> $tumor.TRA.out

