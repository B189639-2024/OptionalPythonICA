# Introduction

This manual will guide you on how to use the program and interpret the output. This program is a tool designed for the analysis of protein sequences. By specifying protein families and taxonomic groups, the program automatically downloads relevant protein sequences, which are processed for analysis, such as sequence conservation analysis and motif detection.

**GitHub Repository:** [https://github.com/B189639-2024/OptionalPythonICA](https://github.com/Bxxxxxx-2024/OptionalPythonICA)
**Decryption Key:** optionalpass

### **How to Use the Programme**

### **1.** Environment required

The programme runs on **Python 3**. **EMBOSS tools** used for conservation analysis and motif detection. **EDirect tools** uesd to retrieve protein sequences from NCBI.

### **2. Running the Programme**

The programme is run from the command line. Use the following command template:

```bash
python script.py --protein_family "<Protein Family>" --taxonomy "<Taxonomic Group>" --output_path <Output Directory>
# example input, to analyze glucose-6-phosphatase sequences in birds (Aves)
python script.py --protein_family "glucose-6-phosphatase" --taxonomy "Aves" --output_path ./outputs
```

During running, if the program pauses and prompts the user for input, it means that the program's tools are asking the user to specify parameters (or enter to accept the default value)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/8e0198fd-44c9-4c1c-98de-821bf586d8fd/af114a93-a88b-4bfe-8026-55413513b931/image.png)

### **3. Outputs (with examples)**

Once the programme runs successfully, it generates the following files in the specified output directory: 

**<Protein Family>_<Taxonomic Group>_sequences.fasta**: The downloaded protein sequences.

**filtered_sequences.fasta**: Filtered sequences based on length.

**conservation_plot.png**: A graphical representation of sequence conservation.

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/8e0198fd-44c9-4c1c-98de-821bf586d8fd/88a236cf-6374-4149-93a1-19b8fd060d15/image.png)

**prosite_scan_results.txt**: Results of motif detection from the PROSITE database.

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/8e0198fd-44c9-4c1c-98de-821bf586d8fd/68a9d93a-2e55-4da2-8561-1be809777dd7/image.png)
