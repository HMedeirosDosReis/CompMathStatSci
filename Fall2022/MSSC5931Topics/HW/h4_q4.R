set.seed(1)#set seed for consistent results 
A=matrix(rnorm(100),nr=10)
eigDec <- eigen(A)

eigDec$values
#------------Output---------
#[1] -2.6820626+0.000000i -1.0060561+2.268741i -1.0060561-2.268741i
#[4]  1.5343031+0.938029i  1.5343031-0.938029i  0.7624088+1.153254i
#[7]  0.7624088-1.153254i -0.3368476+1.107465i -0.3368476-1.107465i
#[10] -0.0569953+0.000000i
#we can see that the eigenvalues 1,10 are real
#So lets arrange them

S <- matrix(0,10,10)
S[,1] <- eigDec$vectors[,1] #the first real eigenvector 
S[,2] <- eigDec$vectors[,10] #the last real eigenvector
# now we can start to populate S with the complex eigenvectors, by separating their 
# real and complex part, by pairs, since they are always two that are the same. 
S[,3] <- Re(eigDec$vectors[,2])
S[,4] <- Im(eigDec$vectors[,2])
S[,5] <- Re(eigDec$vectors[,4])  
S[,6] <- Im(eigDec$vectors[,4])
S[,7] <- Re(eigDec$vectors[,6])  
S[,8] <- Im(eigDec$vectors[,6])
S[,9] <- Re(eigDec$vectors[,8])
S[,10] <- Im(eigDec$vectors[,8])

solution <- solve(S)%*%A%*%S
round(solution)
#------------Output---------
#[,1] [,2]  [,3]  [,4]  [,5] [,6]  [,7] [,8]  [,9] [,10]
#[1,] -3+0i 0+0i  0+0i  0+0i  0+0i 0+0i  0+0i 0+0i  0+0i  0+0i
#[2,]  0+0i 0+0i  0+0i  0+0i  0+0i 0+0i  0+0i 0+0i  0+0i  0+0i
#[3,]  0+0i 0+0i -1+0i  2+0i  0+0i 0+0i  0+0i 0+0i  0+0i  0+0i
#[4,]  0+0i 0+0i -2+0i -1+0i  0+0i 0+0i  0+0i 0+0i  0+0i  0+0i
#[5,]  0+0i 0+0i  0+0i  0+0i  2+0i 1+0i  0+0i 0+0i  0+0i  0+0i
#[6,]  0+0i 0+0i  0+0i  0+0i -1+0i 2+0i  0+0i 0+0i  0+0i  0+0i
#[7,]  0+0i 0+0i  0+0i  0+0i  0+0i 0+0i  1+0i 1+0i  0+0i  0+0i
#[8,]  0+0i 0+0i  0+0i  0+0i  0+0i 0+0i -1+0i 1+0i  0+0i  0+0i
#[9,]  0+0i 0+0i  0+0i  0+0i  0+0i 0+0i  0+0i 0+0i  0+0i  1+0i
#[10,]  0+0i 0+0i  0+0i  0+0i  0+0i 0+0i  0+0i 0+0i -1+0i  0+0i

