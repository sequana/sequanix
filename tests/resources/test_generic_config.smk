# Snakefile to be used in the GUI as a test for generic snakefile
# Note that here, we use configfile keyword so there must be a config file
# to be provided. The filename must be config.yaml as encoded in the file

# This pipeline simply creates dummy data (data rule) with a bunch of
# A, C, G, T letters as a 1-column file. Then the counter rule, just counts 
# the number of letters and save it in count.txt file.
#

configfile: "test_generic_config.yml"
N = int(config['N'])

filename = "count.txt"

rule all:
    input: filename

rule counter:
    input: temp("data.txt")
    output: filename
    run:
        import collections
        with open(input[0], "r") as fh:
            data = fh.read().split("\n")
            counter = collections.Counter(data)
            with open(output[0], "w") as fh:
                for letter in "ACGT":
                    fh.write("%s\n" % counter[letter])

rule data:
    # Create a dummy sequence
    output: temp("data.txt")
    params:
        N=N
    run:
        import random
        N = params.N
        data = "A"*N + "C"*N + "G"*N + "T"*N
        data = "\n".join(data)
        with open(output[0], "w") as fh:
            fh.write(data)

onsuccess:
    with open(filename, "r") as fh:
        data = fh.read()
        assert sum([int(x) for x in data.split("\n") if x ])
