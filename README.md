# Stamps2CSV

*StaMPS (Stanford Method for Persistent Scatterers)* is a software package that allows to extract ground displacements from time series of synthetic aperture radar (SAR) acquisitions (https://github.com/dbekaert/StaMPS). Since statistical analyses (deformation mean, median, standard deviation etc.) of PS points in a timeseries are not possible within the *Stamps Visualizer* (https://github.com/thho/StaMPS_Visualizer) itself, the analysis has to be done manually. 

This package serves for the conversion of *StaMPS Visualizer* output CSVs into analysis-ready data for the use in RStudio. For further information on the working steps see the documentation below. 

1) The *analysis.py* script converts the input CSV into a standard R-readable CSV file of rows and columns, in which every 
row corresponds to a PS point with an ID, x coordinate, y coordinate, the deformation trend over 
the whole timeseries, as well as the deformation at a certain date. All user-dependent input can be specified in the 
*main.py* script.

2) The output file could be loaded into RStudio and analyzed by the *statistics.R* script provided within this package. It is 
possible to analyze a specific parameter for all PS points (Section 1, standard R analysis format) as well as the 
analysis of all parameters for a specific PS point (Section 2).
