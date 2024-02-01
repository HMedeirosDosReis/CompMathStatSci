A_bar <- 1/K*rowSums(A, dim=2)
x_ln <-  t(A_bar)%*%solve((A_bar%*%t(A_bar)))%*%y_des


total_left <- 0
total_right <- 0 
for (i in 1:K) 
{
  total_left <- total_left+ (t(A[,,i])%*%A[,,i])
  total_right <- total_right+(t(A[,,i])%*%y_des)
  
}
total_left <- solve(total_left)
x_mmse <- total_left%*%total_right

#residual norm
norm(A_bar%*%x_ln -y_des, "2")

y_tilde_des <- rep(y_des, K)
A_tilde<-A[,,i]
for(i in 2:K)
{
  A_tilde <- rbind(A_tilde, A[,,i])
}
1/sqrt(K)*norm(y_tilde_des - A_tilde%*%x_mmse, "2")
