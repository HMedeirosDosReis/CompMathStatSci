X<-as.matrix(c(3,2,4,1,5),ncol=1)
alpha <- norm(X,"2")
e_1<- as.matrix(c(1,0,0,0,0),ncol=1)
v <- X+alpha*e_1
u <- v/norm(v, "2")


#normal method
cat("Qx = ",Qx <- (diag(length(u)) - 2*(u%*%t(u)))%*%X)
#created method
cat("Qx_alt = ",Qx_alt <- -e_1%*%norm(X, "2"))

    