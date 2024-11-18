import os
import subprocess
import argparse

def download_sequences(protein_family, taxonomy, output_path):
    file_name = protein_family+'_'+taxonomy+'_sequences.fasta'
    fasta_file = os.path.join(output_path, file_name)
    command = (
        f"esearch -db protein -query '{protein_family}[PROTEIN] AND {taxonomy}[ORGANISM]' | "
        f"efetch -format fasta > {fasta_file}"
    )
    print(f"esearch {protein_family}")
    subprocess.run(command, shell=True, check=True)
    print(f"Sequences saved to {fasta_file}")

def parse_args():
    parser = argparse.ArgumentParser(description="OptionalPythonICA: Generic sequence analysis tool")
    parser.add_argument("--protein_family", required=True, help="Specify the protein family")
    parser.add_argument("--taxonomy", required=True, help="Specify the taxonomic group")
    parser.add_argument("--output_path", required=True, help="Path to save output files")
    return parser.parse_args()

def main():
    args = parse_args()
    os.makedirs(args.output_path, exist_ok=True)
    print(f"Output directory: {args.output_path}")
    download_sequences(args.protein_family, args.taxonomy, args.output_path)



if __name__ == "__main__":
    main()

