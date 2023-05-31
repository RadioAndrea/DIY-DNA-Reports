import sys
import json
from collections import defaultdict
from tabulate import tabulate


def default_value():
    return "--"


class bcolors:
    OK = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


class Snp:
    def __init__(self, snpid, name, ideal):
        self.snpid = snpid
        self.name = name
        self.ideal = ideal


class Report:
    def __init__(self):
        self.report_list = []

    def add(self, snp, alleles):
        allele_result = ""
        if alleles != "--":
            for allele in alleles:
                if snp.ideal == allele:
                    allele_result += "-"
                else:
                    allele_result += "+"
                
            if allele_result.count("+") == 0:
                allele_result = bcolors.OK + allele_result + bcolors.ENDC
            elif allele_result.count("+") == 1 and len(allele_result) == 2:
                allele_result = bcolors.WARNING + allele_result + bcolors.ENDC
            else:
                allele_result = bcolors.FAIL + allele_result + bcolors.ENDC
        else:
            allele_result = "??"
        self.report_list.append([snp.snpid, snp.name, alleles, allele_result])
       
    def print(self):
        columns = ["SNP", "Gene/Variation Name", "Alleles", "Result"]
        print(tabulate(self.report_list, headers=columns, tablefmt="grid"))          


if len(sys.argv) < 3:
    print("Usage: python script.py <file1> <file2>")
    sys.exit(1)

file1 = sys.argv[1]
file2 = sys.argv[2]

report_snp_targets = []

input_genome = defaultdict(default_value)

try:
    with open(file1, 'r') as f1:
        reportjson = json.load(f1)
        report_snp_json_list = reportjson['snps']
        for jsonblock in report_snp_json_list:
            report_snp_targets.append(Snp(jsonblock['snp_id'], jsonblock['gene_name'], jsonblock['ideal']))
        
    with open(file2, 'r') as f2:
        data_started = False
        
        for line in f2:
            if data_started:
                tokens = line.strip().split()
                input_genome[tokens[0]] = tokens[3]
    
            if line.strip() == "# rsid	chromosome	position	genotype":
                data_started = True

except FileNotFoundError:
    print("One or both of the files does not exist.")

except IOError as e:
    print("Error:", str(e))
    
report = Report()
for target in report_snp_targets:
    report.add(target, input_genome[target.snpid])

report.print()
