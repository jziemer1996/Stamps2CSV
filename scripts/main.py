import analysis
import os


def main():
    # Set the working directory, in which the CSV file of the Stamps Visualizer output is located and where you want
    # Your reformatted output CSV to be located
    working_dir = "D:/Aktuelles/Promotion/Packages/StaMPS_Visualizer-master/input/stusi/"
    output_dir = "D:/Aktuelles/Promotion/Programmierung/R/Stamps2CSV/output/"
    stamps_csv = "stamps_tsexport_moehnesubset_5m.csv"
    output_csv = "PS_points_ts_moehnesubset_5m_R.csv"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # Executable function
    analysis.columns(working_dir, output_dir, stamps_csv, output_csv)


if __name__ == "__main__":
    main()
