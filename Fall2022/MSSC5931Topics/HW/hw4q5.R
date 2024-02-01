A = matrix(rnorm(9), ncol=3)

lambda = eigen(A)
fA = (diag(3)+A)%*%solve(diag(3)-A) 

eigFA = eigen(fA)

lambda_fA_spectral_map <- (1+lambda$values)/((1-lambda$values))

eigFA$values
lambda_fA_spectral_map