clear all; close all;
m = 50;
n=10;
T = 10;
alpha = 0.1;
gi = @(w) 1;%sin(pi*w);

dt = T/(m-1);
dx = 1/(n-1);
R = alpha*alpha*dt/(dx^2);
u = zeros(m,n);

u(1, 1:n) = 0;
u(1:m,1) = 0;

for i=1:m-1
    for j=2:n-1
        u(i+1,j)=u(i,j)+R*(u(i,j+1)-2*u(i,j)+u(i,j-1));
    end
    u(i+1,n) = (u(i+1,n-1)+dx*gi((i+1)*dx))/(1+dx);
end

x = (0:n-1)*dx;
t=(0:m-1)*dt;
surf(x,t,u)


xlabel('Spatial Position (x)')
ylabel('Time (t)')
zlabel('Solution u(x, t)')
title('Heat Equation Solution over Space and Time')