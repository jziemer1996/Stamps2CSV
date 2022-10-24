import descending
import os


def main():
    # Set the working directory, in which the CSV file of the Stamps Visualizer output is located and where you want
    # Your reformatted output CSV to be located
    working_dir = "D:/Aktuelles/Promotion/Packages/StaMPS_Visualizer-master/input/stusi/"
    output_dir = "D:/Aktuelles/Promotion/Programmierung/R/Stamps2CSV/output/"
    stamps_csv = "Lister_final_stamps_export_coh_var_disp_ts.csv"
    output_csv = "Lister_PS_points_ts_R.csv"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # Executable function
    descending.columns(working_dir, output_dir, stamps_csv, output_csv)


if __name__ == "__main__":
    main()
