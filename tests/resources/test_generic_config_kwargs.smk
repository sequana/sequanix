# See test_gui_generic_snakefile_configfile.rules for details
#
# There is no configfile keyword. Yet, we use the special variable config, which 
# can be defined using:
#
#     snakemake --configfile config.yaml
#
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
