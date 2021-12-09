import glob
import pathlib
import os
import pandas as pd
import time

from calc.calculator import Calculator

cwd = os.getcwd()  #Get folder
files = os.listdir(cwd)  #Get files
print("Files in %r: %s" % (cwd, files)) #Print

def process(files):
    for file in files:
        basename = os.path.basename(file)

        if basename == "addition.csv":
            print("Processing CSV Addition")
            df = pd.read_csv(file)
            results_arr = []
            for index, row in df.iterrows():
                temp = Calculator.add_number(row['value1'], row['value2'])
                with open("logs/results.txt", "a") as fp:
                    fp.write(f"Time: {time.time()}, File: {file}, "
                             f"Record Number: {index}, " f"Operation: add, Result: {temp}\n")
                    fp.close()
                results_arr.append(temp)
            df["result"] = results_arr
            with open(f"outputs/{basename}", "w") as fp:
                df.to_csv(fp)

        if basename == "subtraction.csv":
            print("Processing CSV Subtraction")
            df = pd.read_csv(file)
            results_arr = []
            for index, row in df.iterrows():
                temp = Calculator.subtract_number(row['value1'], row['value2'])
                with open("logs/results.txt", "a") as fp:
                    fp.write(
                        f"Time: {time.time()}, File: {file}, Record Number: {index}, "
                        f"Operation: subtract, Result: {temp}\n")
                    fp.close()
                results_arr.append(temp)
            df["result"] = results_arr
            with open(f"outputs/{basename}", "w") as fp:
                df.to_csv(fp)

        if basename == "multiplication.csv":
            print("Processing CSV Multiplication")
            df = pd.read_csv(file)
            results_arr = []
            for index, row in df.iterrows():
                temp = Calculator.multiply_numbers(row['value1'], row['value2'])
                with open("logs/results.txt", "a") as fp:
                    fp.write(
                        f"Time: {time.time()}, File: {file}, Record Number: {index}, "
                        f"Operation: multiply, Result: {temp}\n")
                    fp.close()
                results_arr.append(temp)
            df["result"] = results_arr
            with open(f"outputs/{basename}", "w") as fp:
                df.to_csv(fp)

        if basename == "division.csv":
            print("Processing CSV Division")
            df = pd.read_csv(file)
            results_arr = []
            # Loop through records
            for index, row in df.iterrows():
                #Division error
                if row['value2'] == 0:
                    with open("logs/exceptions.txt", "a") as fp:
                        fp.write(f"File: {file}, Record Number: {index}\n")
                        fp.close()
                    results_arr.append("NaN")
                else:
                    #Operation
                    temp = Calculator.divide_numbers(row['value1'], row['value2'])
                    #Write to log fle
                    with open("logs/results.txt", "a") as fp:
                        fp.write(f"Time: {time.time()}, File: {file}, Record Number: {index}, "
                                 f"Operation: divide, Result: {temp}\n")
                        fp.close()
                    results_arr.append(temp)

            #Create export CSVs
            df["result"] = results_arr
            with open(f"outputs/{basename}", "w") as fp:
                df.to_csv(fp)

    return 0


def main():
    path = pathlib.Path(__file__).parent / "inputs"
    # print ("path: " + str(path))
    files = glob.glob(str(path) + "/*")
    # print(files)
    files_len = len(files)
    while True:
        if files_len != 0:
            print("Processing...")
            done = process(files)
            files_len = done
        else:
            print("Running...", end="\r")

        return True

main()