# BAM-integrity-hash
A short script to create an integrity hash for a full sequence genome file, tested on BAM. Currently, we use the MD5 hash algorithm.

## Quickstart
Navigate to the directory that has the BAM file. Enter in the command with the filename to show your MD5 hash.

```bash
python bam-hash.py filename.bam
```

If you did not specify one on the command line, you can enter it then. It will print out the hash.
An example of a produced hash is `da4ab4dfc16ac510e84fb466cc659441`

## Windows
In order to check the validity of this method, both Python in Linux and Powershell in Windows were utilized and returned the same result.
The corresponding command in Powershell,

```msdos
(Get-FileHash -Path $filename -Algorithm MD5).Hash.ToLower()
```
