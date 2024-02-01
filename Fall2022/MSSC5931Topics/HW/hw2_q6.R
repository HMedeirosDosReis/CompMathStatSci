#given variables
A
ytilde


#run 15 times, and remove i from A and ytilde and test it 
for(i in 1:15){
  y_test_i <- ytilde[-i]
  A_test_i <- A[-i,]
  cat("i = ", i, ", result:  ", 
      qr(cbind(A_test_i,y_test_i))$rank == qr(A)$rank+1, "\n")
}
##Output
#i =  1 , result:   TRUE 
#i =  2 , result:   TRUE 
#i =  3 , result:   TRUE 
#i =  4 , result:   TRUE 
#i =  5 , result:   TRUE 
#i =  6 , result:   TRUE 
#i =  7 , result:   TRUE 
#i =  8 , result:   TRUE 
#i =  9 , result:   TRUE 
#i =  10 , result:   TRUE 
#i =  11 , result:   FALSE 
#i =  12 , result:   TRUE 
#i =  13 , result:   TRUE 
#i =  14 , result:   TRUE 
#i =  15 , result:   TRUE 