import click
import pandas as pd
import os
from collections import defaultdict

@click.command()
@click.argument("run_file")
@click.option("--output_folder", default="runs")
def main(run_file, output_folder):
    run_data = pd.read_csv(run_file,sep="\t")
    
    files_codes = defaultdict(list)
    
    for i, row in run_data.iterrows():
        files_codes[row["filename"]].append(row["code"])
    
    dataframe_lines = []
    for k,v in files_codes.items():
        #print(k)
        #print(v)
        dataframe_lines.append([k,"+".join(map(str,v))])
    
    run3_dataframe = pd.DataFrame(dataframe_lines, columns=["filename","code"])
    
    basename_run_file = os.path.basename(run_file)
    
    run3_dataframe.to_csv(os.path.join(output_folder, basename_run_file), sep="\t", index=False)
    
if __name__ == '__main__':
    main()