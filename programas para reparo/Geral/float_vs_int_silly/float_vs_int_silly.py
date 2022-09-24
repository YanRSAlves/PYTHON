#!/usr/bin/env python

import whrandom, fpformat, math

def round(input):
    "return a float rounded to the nearest integer."
    remainder = math.ceil(input) - input
    if remainder > 0.5:
        result = math.ceil(input)
    else:
        result = math.floor(input)
    return result


def mangler(input, math_style="FLOAT", repeats=100):
    output = input
    rescale_factor = 1
    for i in range(repeats):
        factor = whrandom.uniform(0.01, 100)
        if math_style=="TRUNCATE":
            output = int(output * factor)
            output = int(output / factor)
        elif math_style=="FLOAT":
            output = output * factor
            output = output / factor
        elif math_style=="ROUND":
            output = round(output * factor)
            output = round(output / factor)
        #rescale_factor = rescale_factor * (1 / factor)
    # rescaled = int(output * rescale_factor)
    rescaled = output
    return (input, rescaled, math_style, repeats) 


def run_mangler(runs, repeats, verbose=1):
    '''
    A bit of terminology:
    "run" is the number of times to compare the algorithms.
    "repeats" is the number of multiplications to perform
    during each run.
    '''
    results = {"FLOAT": [], "ROUND": [], "TRUNCATE": []}
    for i in range(runs):
        input = int(whrandom.uniform(1, 2L ** 16))
        for math_style in results.keys():
            # We want different numbers each run, but same
            # random sequence for the various math approaches.
            seed_seeder = int(whrandom.uniform(1, 256))
            whrandom.seed(seed_seeder, seed_seeder, seed_seeder)
            resultlist = results[math_style]
            resultlist.append(mangler(input, math_style, repeats))
            if verbose:
                # Give reports along the way.
                input, output, math_style, repeats = resultlist[-1]
                print "After", repeats, "repeats", math_style, "style:"
                print "\tInput:", input, "output:", output
                error = output - input
                if error: print "\terror of:", error
                else: print "\tNo error!"
        if verbose: print "-------------------"

    print " ---- SUMMARY OF RESULTS ---"
    for math_style in results.keys():
        result_list = results[math_style]
        input1, output1, unused, repeats = result_list[0]
        # initialize the errors...
        min_error = max_error = avg_error = abs(input1 - output1)
        print runs, "runs of", math_style, "at", repeats, "operations"
        total_error = 0
        for result in result_list:
            input, output = result[:2]
            error = abs( input - output)
            min_error = min(min_error, error)
            max_error = max(max_error, error)
            total_error = total_error + error
        avg_error = float(total_error) / len(result_list)
        if not min_error: 
            min_error = "ZERO!"

        if math_style=="FLOAT":
            if min_error != "ZERO!":
                min_error = "%9.21f" % min_error
            max_error = "%9.11f" % max_error
            avg_error = "%9.11f" % avg_error
            
        print "Deviation: min:", min_error, "max:", max_error, "avg:", avg_error
        print "  -----------  "
        
if __name__ == "__main__":
    run_mangler(100, 100)



