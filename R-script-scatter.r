args = commandArgs(trailingOnly=TRUE)

Regdata <- read.csv(args[1])
x <- Regdata$x
y <- Regdata$y

png('Script-scatterplotR.png')
plot(x, y, main = "Regex1_scatterplot_R", col = "blue")

png('Script-linearmodelingR.png')
plot(x, y, main = "Regex1_scatterplot_R_linearmodeling", col = "blue")
abline(lm(y ~ x))