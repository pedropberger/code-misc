weightedMean <- function(X, W) {
    Y = X*W
    Y=sum(Y)/sum(W)
    return(cat(format(round(Y, 1), nsmall = 1)))
}

#codes from the example

stdin <- file('stdin')
open(stdin)

n <- as.integer(trimws(readLines(stdin, n = 1, warn = FALSE), which = "both"))

vals <- strsplit(trimws(readLines(stdin, n = 1, warn = FALSE), which = "right"), " ")[[1]]
vals <- as.integer(vals)

weights <- strsplit(trimws(readLines(stdin, n = 1, warn = FALSE), which = "right"), " ")[[1]]
weights <- as.integer(weights)

weightedMean(vals, weights)

close(stdin)
