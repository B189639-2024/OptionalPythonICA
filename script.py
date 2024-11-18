import os
import subprocess
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="OptionalPythonICA: Generic sequence analysis tool")
    parser.add_argument("--protein_family", required=True, help="Specify the protein family")
    parser.add_argument("--taxonomy", required=True, help="Specify the taxonomic group")
    parser.add_argument("--output_path", required=True, help="Path to save output files")
    return parser.parse_args()

def main():
    args = parse_args()
    os.makedirs(args.output_path, exist_ok=True)
    print(f"Working directory created at {args.output_path}")

if __name__ == "__main__":
    main()

