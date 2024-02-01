#define given variables
t <- seq (1:1000) ;
z <- 5 * sin ( t / 10+2) + 0.1 * sin ( t ) + 0.1 * sin (2 *t -5) ;
c = matrix(c(3,-3,1), nrow=1)
#create a function that will calculate zhat 
zhat <- function(c_param, zt, zt_minus_1, zt_minus_2) {
  zmatrix <- matrix(c(zt,zt_minus_1, zt_minus_2), ncol=1)
  return(c_param%*%zmatrix)
}
#declare empty vector for zhat
zhat_vector<-c(0,0,0)
#compute all zhats
for(i in 4:1000){
  zhat_vector[i]<- zhat(c, z[i-1],z[i-2],z[i-3])
}
#take out the first 4 elements of the arrays, since sum starts at j=4
zhat_vector<- tail(zhat_vector, 997)
z<- tail(z, 997)

RMS <- sqrt(((1/997)*sum((zhat_vector-z)^2))/((1/997)*sum((z)^2)))
        
cat('RMS = ',RMS)
#output => RMS =  0.09724805
