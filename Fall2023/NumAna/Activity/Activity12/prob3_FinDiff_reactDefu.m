%% Finite Difference for BVPs
clear all; close all
L=100;
k=5;
D=1.5;
u0 = 0.1;
uf = 1;
h = 20;

a1 = 2*D/h^2+k;
a2 = 0;
c = D/h^2;
A = [a1 -c 0 0;
     -c a1 -c 0;
     0 -c a1 -c;
     0 0 -c a1];
b = [a2+u0*D/h^2 a2 a2 a2+uf*D/h^2]';

uin = A\b;
u = [u0 uin' uf];
x = 0:h:L;
plot(x,u)

%% iii
% solve the same with different h
L=100;
k=5;
D=1.5;
u0 = 0.1;
uf = 1;
h = 2;

a1 = 2*D/h^2+k;
a2 = 0;
c = D/h^2;

m_size = L/h-1;
A = diag(a1*ones(1,m_size)) + diag( ...
    -c*ones(1,m_size-1),1) + diag( ...
    -c*ones(1,m_size-1),-1);

b = a2+zeros(m_size,1);
b(1) = b(1)+u0*D/h^2;
b(end) = b(end)+uf*D/h^2;

uin = A\b;
u = [u0 uin' uf];
x = 0:h:L;
plot(x,u)