
mkdir -p bioinformatics_project

mkdir -p bioinformatics_project/data
mkdir -p bioinformatics_project/scripts
mkdir -p bioinformatics_project/results

touch bioinformatics_project/scripts/generate_fasta.py
touch bioinformatics_project/scripts/dna_operations.py
touch bioinformatics_project/scripts/find_cutsites.py

touch bioinformatics_project/results/cutsite_summary.txt

touch bioinformatics_project/data/random_sequence.fasta

echo "# Bioinformatics Project" > bioinformatics_project/README.md
echo "The project's structure is as follows:" >> bioinformatics_project/README.md
echo "1. **data/** - Contains data inputs" >> bioinformatics_project/README.md
echo "   - random_sequence.fasta: Bioinformatics data sequence [example]" >> bioinformatics_project/README.md
echo "2. **scripts/** - Contains scripts to analyze data" >> bioinformatics_project/README.md
echo "   - generate_fasta.py: Script to generate FASTA sequences." >> bioinformatics_project/README.md
echo "   - dna_operations.py: Script to perform DNA-related operations." >> bioinformatics_project/README.md
echo "   - find_cutsites.py: Script to find restriction enzyme cut sites in DNA sequences." >> bioinformatics_project/README.md
echo "3. **results/** - Contains results of data processing" >> bioinformatics_project/README.md
echo "   - cutsite_summary.txt: Results stored [in .txt; example]" >> bioinformatics_project/README.md

echo "Bioinformatics project structure created successfully!"
