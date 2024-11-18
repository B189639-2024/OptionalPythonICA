import os
import subprocess
import argparse
from Bio import SeqIO

def scan_prosite(input_fasta, output_file):
    command = f"patmatmotifs -sequence {input_fasta} -outfile {output_file}"
    print(f"Running command: {command}")
    subprocess.run(command, shell=True, check=True)
    print(f"PROSITE scan results saved to {output_file}")

def analyze_conservation(input_fasta, output_plot):
    command = f"plotcon -sequence {input_fasta} -graph png -goutfile {output_plot}"
    print(f"Running command: {command}")
    subprocess.run(command, shell=True, check=True)
    print(f"Conservation plot saved to {output_plot}")

def filter_sequences(input_fasta, output_fasta, min_length=100, max_length=2000):
    with open(input_fasta, "r") as infile, open(output_fasta, "w") as outfile:
        for record in SeqIO.parse(infile, "fasta"):
            if min_length <= len(record.seq) <= max_length:
                SeqIO.write(record, outfile, "fasta")
    print(f"Filtered sequences saved to {output_fasta}")

def download_sequences(protein_family, taxonomy, output_path):
    file_name = protein_family+'_'+taxonomy+'_sequences.fasta'
    fasta_file = os.path.join(output_path, file_name)
    command = (
        f"esearch -db protein -query '{protein_family}[PROTEIN] AND {taxonomy}[ORGANISM]' | "
        f"efetch -format fasta > {fasta_file}"
    )
    print(f"esearch {protein_family} {taxonomy}")
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
    try:
        download_sequences(args.protein_family, args.taxonomy, args.output_path)
    except subprocess.CalledProcessError as e:
        print(f"downloding error: {e}")
        with open(os.path.join(output_path, "error.log"), "a") as log_file:
            log_file.write(str(e) + "\n")
    filtered_fasta = os.path.join(args.output_path, "filtered_sequences.fasta")
    seq_file = args.protein_family+'_'+args.taxonomy+'_sequences.fasta'
    try:
        filter_sequences(os.path.join(args.output_path, seq_file), filtered_fasta)
    except subprocess.CalledProcessError as e:
        print(f"filter error: {e}")
        with open(os.path.join(output_path, "error.log"), "a") as log_file:
            log_file.write(str(e) + "\n")
    try:
        conservation_plot = os.path.join(args.output_path, "conservation_plot.png")
        analyze_conservation(filtered_fasta, conservation_plot)
    except subprocess.CalledProcessError as e:
        print(f"conservation plot error: {e}")
        with open(os.path.join(output_path, "error.log"), "a") as log_file:
            log_file.write(str(e) + "\n")
    try:
        prosite_output = os.path.join(args.output_path, "prosite_scan_results.txt")
        scan_prosite(filtered_fasta, prosite_output)
    except subprocess.CalledProcessError as e:
        print(f"scan prosite error: {e}")
        with open(os.path.join(output_path, "error.log"), "a") as log_file:
            log_file.write(str(e) + "\n")


if __name__ == "__main__":
    main()

