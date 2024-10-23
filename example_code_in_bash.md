bash setup_project.sh

cd bioinformatics_project/

python scripts/generate_fasta.py 1000000

python scripts/dna_operations.py data/random_sequence.fasta

python scripts/find_cutsites.py data/random_sequence.fasta "G|GATCC"
