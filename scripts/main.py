import analysis
import user_analysis
import os


def main():
    # Set the working directory, in which the CSV file of the Stamps Visualizer output is located and where you want
    # Your reformatted output CSV to be located
    working_dir = "C:/Users/ni82xoj/Desktop/KI4KI/Daten/10_PSI_Zeitreihen/S1_asc_short/"
    output_dir = "C:/Users/ni82xoj/Desktop/KI4KI/Daten/10_PSI_Zeitreihen/S1_asc_short/analysis/"
    stamps_csv = "Ennepe_asc_short_stamps_export_coh_var_disp_ts.csv"
    output_csv = "PS_points_Ennepe_asc_short_stamps_export_coh_var_disp_ts_GPT.csv"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # Executable function
    user_analysis.columns(working_dir, output_dir, stamps_csv, output_csv)


if __name__ == "__main__":
    main()
