import analysis


def main():
    # Set the working directory, in which the CSV file of the Stamps Visualizer output is located and where you want
    # Your reformatted output CSV to be located
    working_dir = "C:/Users/ni82xoj/Desktop/StaMPS_Visualizer-master/input/stusi/"
    stamps_csv = "stamps_tsexport.csv"
    output_csv = "PS_points_ts_R.csv"

    # Executable function
    analysis.columns(working_dir, stamps_csv, output_csv)


if __name__ == "__main__":
    main()
