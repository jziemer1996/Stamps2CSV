import csv
import os

### Columns ###
## Analysis-ready RStudio CSV format ##


def columns(working_dir, output_dir, stamps_csv, output_csv):
    with open(working_dir + stamps_csv, 'r') as file:
        reader = csv.reader(file)
        n = 1
        with open(output_dir + output_csv, 'w',
                  newline='') as f:
            # You need to add every single deformation value of an PS as a new list element
            # example header = ['ID', 'Lat', 'Lon', 'Trend (mm/y)', 'Deformation X in mm at date yyyymmdd']
            header = ['ID', 'Lat', 'Lon', 'Coh', 'Var', 'Trend', 'Def_1', 'Def_2', 'Def_3', 'Def_4', 'Def_5', 'Def_6',
                      'Def_7', 'Def_8', 'Def_9', 'Def_10', 'Def_11', 'Def_12', 'Def_13', 'Def_14', 'Def_15', 'Def_16',
                      'Def_17', 'Def_18', 'Def_19', 'Def_20', 'Def_21', 'Def_22', 'Def_23', 'Def_24', 'Def_25', 'Def_26',
                      'Def_27', 'Def_28', 'Def_29', 'Def_30', 'Def_31', 'Def_32', 'Def_33', 'Def_34', 'Def_35', 'Def_36']
            writer = csv.writer(f)
            writer.writerow(header)
            # Create multiple empty lists
            list_0, list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8, list_9, list_10, list_11, list_12, \
            list_13, list_14, list_15, list_16, list_17, list_18, list_19, list_20, list_21, list_22, list_23, list_24, \
            list_25, list_26, list_27, list_28, list_29, list_30, list_31, list_32, list_33, list_34, list_35, list_36, \
            list_37, list_38, list_39, list_40 = \
                ([] for i in range(41))

            id = -2  # Point ID starts at "1", because first two rows of the STAMPS Visualizer output CSV are not useful!
            for row in reader:
                id += 1
                # If you add deformation values above, you need to append the values to a new list
                list_0.append(id), list_1.append(row[0]), list_2.append(row[1]), list_3.append(row[2]), \
                list_4.append(row[3]), list_5.append(row[4]), list_6.append(row[5]), list_7.append(row[6]), \
                list_8.append(row[7]), list_9.append(row[8]), list_10.append(row[9]), list_11.append(row[10]), \
                list_12.append(row[11]), list_13.append(row[12]), list_14.append(row[13]), list_15.append(row[14]), \
                list_16.append(row[15]), list_17.append(row[16]), list_18.append(row[17]), list_19.append(row[18]), \
                list_20.append(row[19]), list_21.append(row[20]), list_22.append(row[21]), list_23.append(row[22]),
                list_24.append(row[23]), list_25.append(row[24]), list_26.append(row[25]), list_27.append(row[26]), \
                list_28.append(row[27]), list_29.append(row[28]), list_30.append(row[29]), list_31.append(row[30]), \
                list_32.append(row[31]), list_33.append(row[32]), list_34.append(row[33]), list_35.append(row[34]), \
                list_36.append(row[35]), list_37.append(row[36]), list_38.append(row[37]), list_39.append(row[38]), \
                list_40.append(row[39])
                rows = zip(list_0, list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8, list_9, list_10,
                           list_11, list_12, list_13, list_14, list_15, list_16, list_17, list_18, list_19, list_20,
                           list_21, list_22, list_23, list_24, list_25, list_26, list_27, list_28, list_29, list_30,
                           list_31, list_32, list_33, list_34, list_35, list_36, list_37, list_38, list_39, list_40)
            for PS_point in rows:
                writer.writerow(PS_point)

    # Delete the not useful lines mentioned above to get a nice cleaned CSV file
    with open(output_dir + output_csv) as rf, open(output_dir + output_csv + ".temp", "w") as wf:
        for i, line in enumerate(rf):
            if i != 1 and i != 2:  # Everything but the second and third line
                wf.write(line)

    os.replace(output_dir + output_csv + ".temp", output_dir + output_csv)
