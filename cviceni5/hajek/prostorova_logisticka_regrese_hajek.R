# Logisticka regrese s prostorovymi daty
# Autor: Hajek
#
# Skript je pripraveny pro spusteni v RStudiu.
# Vstupni data:
#   d:/UPOL/2_Semestr/POGEO/regrese/rastry/*.tif
#   d:/UPOL/2_Semestr/POGEO/regrese/sesuvy.xls

library(terra)
library(readxl)

data_dir <- "d:/UPOL/2_Semestr/POGEO/regrese"
raster_dir <- file.path(data_dir, "rastry")
output_dir <- file.path(data_dir, "vystupy")

dir.create(output_dir, showWarnings = FALSE, recursive = TRUE)

# 1) Nacteni rastru s charakteristikami povrchu
DMR <- rast(file.path(raster_dir, "DMR.tif"))
curvature <- rast(file.path(raster_dir, "curvature.tif"))
flowD <- rast(file.path(raster_dir, "flowD.tif"))
flowA <- rast(file.path(raster_dir, "flowA.tif"))
slope <- rast(file.path(raster_dir, "slope.tif"))

names(DMR) <- "DMR"
names(curvature) <- "curvature"
names(flowD) <- "flowD"
names(flowA) <- "flowA"
names(slope) <- "slope"

DMR
summary(DMR)

# 2) Vizualizace DMR
png(file.path(output_dir, "01_DMR.png"), width = 900, height = 650)
plot(DMR, main = "DMR")
dev.off()

# Pri praci primo v RStudiu se graf vykresli i v panelu Plots.
plot(DMR, main = "DMR")

# 3) Nacteni lokalit sesuvu a vykresleni bodu nad DMR
sesuvy <- read_excel(file.path(data_dir, "sesuvy.xls"), sheet = "List1")
lokality <- vect(sesuvy, geom = c("X", "Y"), crs = crs(DMR))

png(file.path(output_dir, "02_DMR_lokality.png"), width = 900, height = 650)
plot(DMR, main = "Lokality sesuvu")
points(lokality, pch = 16, col = "red", cex = 0.5)
dev.off()

plot(DMR, main = "Lokality sesuvu")
points(lokality, pch = 16, col = "red", cex = 0.5)

# 4) Extrakce hodnot rastru do bodu a priprava tabulky pro model
hodnoty <- extract(c(DMR, curvature, flowA, flowD, slope), lokality)
sesuvy <- cbind(sesuvy, hodnoty[, -1])
sesuvy <- na.omit(as.data.frame(sesuvy))

write.csv(
  sesuvy,
  file.path(output_dir, "sesuvy_s_hodnotami_rastru.csv"),
  row.names = FALSE
)

# 5) Logisticka regrese se vsemi prediktory
modelSesuv <- glm(
  VYSKYT ~ DMR + curvature + flowA + flowD + slope,
  data = sesuvy,
  family = binomial
)

summary(modelSesuv)

# 6) Druhy model pouze z vyznamnych prediktoru podle zadani
modelSesuv2 <- glm(
  VYSKYT ~ DMR + flowA + slope,
  data = sesuvy,
  family = binomial
)

summary(modelSesuv2)

capture.output(
  {
    cat("Model se vsemi prediktory\n")
    print(summary(modelSesuv))
    cat("\nModel pouze z vybranych prediktoru\n")
    print(summary(modelSesuv2))
  },
  file = file.path(output_dir, "souhrn_modelu.txt")
)

# 7) Predikce rizika sesuvu do rastru
rastryPredikce <- c(DMR, flowA, slope)
names(rastryPredikce) <- c("DMR", "flowA", "slope")

risk <- predict(rastryPredikce, modelSesuv2, type = "response")
names(risk) <- "risk"

# Predikce i ze vsech rastru pro porovnani, stejne jako ve vzorovem zadani
rastryPredikce2 <- c(DMR, flowA, slope, flowD, curvature)
names(rastryPredikce2) <- c("DMR", "flowA", "slope", "flowD", "curvature")

risk2 <- predict(rastryPredikce2, modelSesuv, type = "response")
names(risk2) <- "risk_vsechny_prediktory"

png(file.path(output_dir, "03_predikce_rizika.png"), width = 1200, height = 600)
par(mfrow = c(1, 2))
plot(risk, main = "Risk - vyznamne prediktory")
plot(risk2, main = "Risk - vsechny prediktory")
dev.off()

par(mfrow = c(1, 2))
plot(risk, main = "Risk - vyznamne prediktory")
plot(risk2, main = "Risk - vsechny prediktory")
par(mfrow = c(1, 1))

# 8) Export vyslednych rastru pro dalsi zpracovani v GIS
writeRaster(risk, file.path(output_dir, "risk.tif"), overwrite = TRUE)
writeRaster(risk2, file.path(output_dir, "risk_vsechny_prediktory.tif"), overwrite = TRUE)

cat("Hotovo. Vystupy jsou ulozene ve slozce:", output_dir, "\n")
