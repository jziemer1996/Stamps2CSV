import csv
import os

### Columns ###
## Analysis-ready RStudio CSV format ##


def columns(working_dir, stamps_csv, output_csv):
    with open(working_dir + stamps_csv, 'r') as file:
        reader = csv.reader(file)
        n = 1
        with open(working_dir + output_csv, 'w',
                  newline='') as f:
            # You need to add every single deformation value of an PS as a new list element
            # example header = ['ID', 'Lat', 'Lon', 'Trend (mm/y)', 'Deformation X in mm at date yyyymmdd']
            header = ['ID', 'Lat', 'Lon', 'Trend', 'Def_1', 'Def_2', 'Def_3', 'Def_4', 'Def_5', 'Def_6', 'Def_7',
                      'Def_8', 'Def_9', 'Def_10']
            writer = csv.writer(f)
            writer.writerow(header)
            # Create multiple empty lists
            list_0, list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8, list_9, list_10, list_11, list_12, \
            list_13 = ([] for i in range(14))

            id = -2  # Point ID starts at "1", because first two rows of the STAMPS Visualizer output CSV are not useful!
            for row in reader:
                id += 1
                # If you add deformation values above, you need to append the values to a new list
                list_0.append(id), list_1.append(row[0]), list_2.append(row[1]), list_3.append(row[2]), \
                list_4.append(row[3]), list_5.append(row[4]), list_6.append(row[5]), list_7.append(row[6]), \
                list_8.append(row[7]), list_9.append(row[8]), list_10.append(row[9]), list_11.append(row[10]), \
                list_12.append(row[11]), list_13.append(row[12])
                rows = zip(list_0, list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8, list_9, list_10,
                           list_11, list_12, list_13)
            for PS_point in rows:
                writer.writerow(PS_point)

    # Delete the not useful lines mentioned above to get a nice cleaned CSV file
    with open(working_dir + output_csv) as rf, open(working_dir + output_csv + ".temp", "w") as wf:
        for i, line in enumerate(rf):
            if i != 1 and i != 2:  # Everything but the second and third line
                wf.write(line)

    os.replace(working_dir + output_csv + ".temp", working_dir + output_csv)
