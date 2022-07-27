setwd("C:/Users/ni82xoj/Desktop/StaMPS_Visualizer-master/input/stusi")
r <- read.csv("PS_points_ts_R.csv", sep=",", dec=".")

#### SECTION 1: TO ANALYZE A SPECIFIC PARAMETER FOR ALL PS POINTS (COLUMNS), PROCEED HERE! ####

#### SECTION 2: TO ANALYZE A ALL PARAMETERS FOR A SPECIFIC PS POINT OVER TIME (ROWS), PROCEED HERE! ####
# Read the CSV table as rows, select number of rows to be read (n = ...)
rows <- readLines(paste("PS_points_ts_R.csv", sep = ""),
                  n = 2)

### Select a specific PS point ###
# Note that rows[1] displays parameter names only, PS selection starts with rows[2]!
# We recommend to always analyze only one PS
v1 <- c(rows[2]) # PS with ID 1

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