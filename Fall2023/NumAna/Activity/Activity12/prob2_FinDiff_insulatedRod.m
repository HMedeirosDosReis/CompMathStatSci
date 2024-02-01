%% Finite Difference for BVPs
clear all; close all
L=10;
u0 = 40;
uf = 200;
h = 2;
a1 = 2;
a2 = 25*h^2;

A = [a1 -1 0 0;
     -1 a1 -1 0;
     0 -1 a1 -1;
     0 0 -1 a1];
b = [a2+u0 a2 a2 a2+uf]';

uin = A\b;
u = [u0 uin' uf];
x = 0:h:L;
plot(x,u)

%% iii
% solve the same with different h
clear all; close all
L=10;
u0 = 40;
uf = 200;
h = 0.02;
a1 = 2;
a2 = 25*h^2;

m_size = L/h-1;
A = diag(a1*ones(1,m_size)) + diag( ...
    -1*ones(1,m_size-1),1) + diag( ...
    -1*ones(1,m_size-1),-1);

b = a2+zeros(m_size,1);
b(1) = b(1)+u0;
b(end) = b(end)+uf;

uin = A\b;
u = [u0 uin' uf];
x = 0:h:L;
plot(x,u)