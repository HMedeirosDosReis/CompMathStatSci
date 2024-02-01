invXXT = solve(X%*%t(X))
A_hat = Y%*%t(X)%*%invXXT

N <- ncol(X)


norm(A_hat%*%X[,1]-Y[,1], "2") #top
norm(Y[,1], "2") #bottom
sum<-0
for (i in c(1:N))
{
  top<-norm(A_hat%*%X[,i]-Y[,i], "2") #top
  bot<-norm(Y[,i], "2") #bottom
  sum<-sum+ (top/bot)
}
result <- sum/N

