import csv
import os

def columns(working_dir, output_dir, stamps_csv, output_csv):
    # Open stamps_csv in read mode
    with open(working_dir + stamps_csv, 'r') as file:
        reader = csv.reader(file)
        # Open output_csv in write mode
        scenes = int(input("How long is the timeseries you want to convert (number of processed scenes)? "))
        with open(output_dir + output_csv, 'w', newline='') as f:
            header = ['ID', 'Lat', 'Lon', 'Coh', 'Var', 'Trend'] + [f"Def_{i}" for i in range(1, scenes+1)]
            print(header)
            writer = csv.writer(f)
            writer.writerow(header)
            id = -2
            for row in reader:
                id += 1
                row = [id] + row[:5] + row[5:]
                writer.writerow(row)

    # Clean up output_csv
    with open(output_dir + output_csv) as rf, open(output_dir + output_csv + ".temp", "w") as wf:
        for i, line in enumerate(rf):
            if i != 1 and i != 2:  # Everything but the second and third line
                wf.write(line)

    os.replace(output_dir + output_csv + ".temp", output_dir + output_csv)