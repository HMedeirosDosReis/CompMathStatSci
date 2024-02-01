% Program 8.2 Backward difference method for heat equation 
% input: space interval [xl,xr], time interval [t0,T], 
%     number of space steps M, number of time steps N 
% output: solution u 
% Example usage: u=heatbd(0,1,0,1,10,10) 

u=heatbd(0,1,0,1,10,10);
%%
function u=heatbd(xl,xr,t0,T,Mx,Nt) 
f=@(x) sin(pi*x);   %Initial Condition
l=@(t) 0*t;         %Boundary Condition at xl
r=@(t) 0*t;         %Boundary Condition at xr
alphsq=1;           %Conduction (diffusion) coefficient 
dx=(xr-xl)/Mx; dt=(T-t0)/Nt; m=Mx-1; n=Nt; 
R=alphsq*dt/(dx*dx); 
A=diag(1+2*R*ones(m,1))+diag(-R*ones(m-1,1),1); 
A=A+diag(-R*ones(m-1,1),-1);   % define matrix A 
lside=l(t0+(0:n)*dt); rside=r(t0+(0:n)*dt); 
u(:,1)=f(xl+(1:m)*dx)';             % initial conditions 
for j=1:n 
  u(:,j+1)=A\(u(:,j)+R*[lside(j);zeros(m-2,1);rside(j)]); 
end 
u=[lside;u;rside];                 % attach boundary conds 
x=(0:m+1)*dx;t=(0:n)*dt; 
surf(x,t,u')                       % 3-D plot of solution u 
view(60,30);axis([xl xr t0 T -1 1]) 
end