# DIY DNA Reporting
## Introduction
Some people have been working with online uploader tools like GeneticGenie dot com in order to quickly look for SNPs in their data from commercial services like 23andMe.
Unfortunately this means that there is a more than trivial chance that sensitive genetic data could be harvested for unwanted uses.

To help fix this I have made a script that accomplishes the same goal entirely offline, on your own computer.

# What is this?
The roughest draft of a tool to quickly make reports from your raw 23andMe data. It ONLY works with 23andMe raw data right now.

# What does it do?
There are reports pre-made for:

  - Methylation
    - This is as similar to a report to GeneticGenie dot com as I can make without access to their backend code; consider this a sort of clean-room reverse engineering
    - This report reports instances of "risk alleles" based on [SNPedia's article on Yasko Methylation](https://www.snpedia.com/index.php/Yasko_Methylation)
    - The Yasko Methylation theory isn't really proven one way or another, so you should consider this report as simply a demo file for this program
  - Methylation Extended
	- This is a report that goes beyond the standard report based on aforementioned site and covers more methylation SNPs
	- This covers all the SNPs listed in the [SNPedia article on Yasko Methylation](https://www.snpedia.com/index.php/Yasko_Methylation)
    - The Yasko Methylation theory isn't really proven one way or another, so you should consider this report as simply a demo file for this program

You can make your own reports using the same JSON structure to test your own suspicions/claims/hunches.

# How do I run it?

You need Python 3, if you're on Windows you'll need to get it unless you already downloaded it.

Requires tabulate, install with `pip install tabulate`


I use the latest of each, but most likely any version would work

Run the diyDnaReport.py from the command line with `python diyDnaReport.py <report.json> <23andMeData.txt>`