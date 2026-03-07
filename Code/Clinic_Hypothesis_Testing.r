
####FUNCTION APPLICATION############

# We apply the bonferroni method function
bonferroni <- function(pVals, fwerBound) {
  threshold <- fwerBound/length(pVals)
  rejectNulls <- sum(pVals < threshold)
  if (rejectNulls  == 0) {
    return (NULL)
  } else{
    return (rejectNulls)
  }
}

# We apply the Benjamini Hochberg process
bh <- function(pVals,fdrBound){
  idx <- order(pVals)     # we get the array that sorts
  sorted_pVals <- pVals[idx]  # sorted array
  original_positions <- idx
  lengthPvalues <- length(pVals)
  largestIndex <- 0 # to prevent overshooting by 1
  for(i in 1:lengthPvalues){
    if(sorted_pVals[i] <= (fdrBound*i)/length(sorted_pVals)){
      largestIndex <- i # find the largest index until this happens
    }
  }
  if(largestIndex == 0){ # we reject nothing here
    return(NULL)
  } else {
    original_indices <- idx[1:largestIndex] # we obtain the values
    return(original_indices)
  }
}


#########SOME TESTING ON CSVS#########

# change file address 
df <- read.csv("dataSheetsUsed/ashe_sims_Asheboro BoE Bachelors Degree_Cam.csv",check.names = FALSE)
is_sep <- is.na(df$Candidate) | df$Candidate == ""
block_id <- cumsum(is_sep) + 1  # we add for separators
df$block_id <- block_id

df2 <- df[!is_sep, ]

block_pval <- function(d) {
  # Drop any remaining blanks in results
  d <- d[d$`Plurality Result` != "" & d$`STV Result` != "", ]
  
  PL  <- d$`Plurality Result` == "True"
  STV <- d$`STV Result` == "True"
  
  x <- sum(PL & !STV)   # PL=True, STV=False (discordant outcomes)
  y <- sum(!PL & STV)   # PL=False, STV=True
  N <- x + y
  
  if (N == 0) return(1)               # no discordant pairs
  binom.test(x, N, p = 0.5)$p.value   # exact McNemar
}

# --- 3) p-value per block (election) ---
blocks <- split(df2, df2$block_id)
pVals <- sapply(blocks, block_pval)

pVals   # Array of pVals

bonferroni(pVals, fwerBound = 0.05)
bh(pVals, fdrBound = 0.05)



df <- read.csv("dataSheetsUsed/char_sims_Charlotte Board of Education White_PL.csv",
               check.names = FALSE, stringsAsFactors = FALSE)

sep_col <- df[[1]]
is_sep <- is.na(sep_col) | trimws(sep_col) == ""

# Create block ids for ALL rows
block_id <- cumsum(is_sep) + 1
df$block_id <- block_id

# Keep only non-separator rows
df2 <- df[!is_sep, , drop = FALSE]

# Exact McNemar p-value for one block
block_pval <- function(d) {
  ok <- !is.na(d$`Plurality Result`) & !is.na(d$`STV Result`) &
    trimws(d$`Plurality Result`) != "" & trimws(d$`STV Result`) != ""
  d <- d[ok, , drop = FALSE]
  
  PL  <- trimws(d$`Plurality Result`) == "True"
  STV <- trimws(d$`STV Result`) == "True"
  
  x <- sum(PL & !STV)
  y <- sum(!PL & STV)
  N <- x + y
  if (N == 0) return(1)
  binom.test(x, N, p = 0.5)$p.value
}

blocks <- split(df2, df2$block_id)
pVals <- sapply(blocks, block_pval)

pVals
bonferroni(pVals, fwerBound = 0.05)
bh(pVals, fdrBound = 0.05)


