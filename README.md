# BAM-integrity-hash
A cryptographic method to create an integrity hash for a full sequence genome file, tested on BAM. This implementation utilizes the SHA-3 512 bits hash algorithm for enhanced security and reduced collision probabilities.

## Quickstart
Install the requirements with `pip install requirements.txt`. Navigate to the directory that has the BAM file. Enter in the command with the filename to show your SHA-3 hash.

```bash
python bam-hash.py filename.bam
```

If you did not specify one on the command line, you can enter it then. It will print out the hash.
An example of a produced hash is
`bbd2111ebb10bdb5bb0ade64f35a2e1522a27dcfd25c0edf12470f54410873674d29fb4848cf43b18292ab434ce94531b7a4d98b83995aec6f9092d7e3c90b51`