# Stamps2CSV

This package serves for the conversion of StaMPS Visualizer output CSVs to analysis-ready data for the use in RStudio. 

The analysis.py script converts the input CSV into a standard R-readable CSV file of rows and columns, in which every 
row corresponds to a PS point with an ID, x coordinate, y coordinate, the deformation trend over 
the whole timeseries, as well as the deformation at a certain date. All user-dependent input can be specified in the 
main.py script.

The output file could be loaded into RStudio and analyzed by the Statistics.R script provided within this package. It is 
possible to analyze a specific parameter for all PS points (Section 1, standard R analysis format) as well as the 
analysis of all parameters for a specific PS point (Section 2).
