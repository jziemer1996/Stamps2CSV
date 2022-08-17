# Set working directory
#setwd("C:/Users/ni82xoj/Desktop/StaMPS_Visualizer-master/input/stusi")
setwd("C:/Users/ni82xoj/Desktop/KI4KI/Daten/Sorpe/CSV")
# Read reformatted CSV file
orig <- read.csv("PS_points_ts_sorpesubset_5m_orig_selected.csv", sep=",", dec=".")
cle1 <- read.csv("PS_points_ts_sorpesubset_5m_Cle1_selected.csv", sep=",", dec=".")
cle2 <- read.csv("PS_points_ts_sorpesubset_5m_Cle2_selected.csv", sep=",", dec=".")
cle3 <- read.csv("PS_points_ts_sorpesubset_5m_Cle3_selected.csv", sep=",", dec=".")
cle4 <- read.csv("PS_points_ts_sorpesubset_5m_Cle4_selected.csv", sep=",", dec=".")

#### SECTION 1: TO ANALYZE A SPECIFIC PARAMETER FOR ALL PS POINTS (COLUMNS), PROCEED HERE! ####

#### SECTION 2: TO ANALYZE A ALL PARAMETERS FOR A SPECIFIC PS POINT OVER TIME (ROWS), PROCEED HERE! ####
# Read the CSV table as rows, select number of rows to be read (n = ...)
rows <- readLines(paste("PS_points_ts_sorpesubset_5m_Cle2_selected.csv", sep = ""),
                  n = 18)

### Select a specific PS point ###
# Note that rows[1] displays parameter names only, PS selection starts with rows[2]!
# We recommend to always analyze only one PS 
v1 <- c(rows[16]) # PS with ID 1, change n = ... in line 16 for more rows!

### Convert the parameter values to numerics ###
v2 <- as.list(strsplit(v1, ",")[[1]])
v3 <- unlist(v2)
v4 <- as.numeric(v3)

### Statistical analysis ###
## Trend (mm/y)
v4[4]
## TS analysis
# Trend (mm/TS) --> Should be almost equal with the annual trend
mean(v4[5:14])
# Plot TS
y <- (v4[5:14])
# Connected scatter plot
plot(y, type = "b", col=4, pch=19,
     xlab = "Time", ylab = "Deformation (mm)")