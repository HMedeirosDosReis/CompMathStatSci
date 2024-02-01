%% Finite Difference for BVPs
clear all; close all
%Solve the 1D Heat equation with Dirichlet BCs.
L = 10; Tair = 200; T0 = 300; TL = 400; w = 0.05;q0 = 0;
h = 2;
a1 = 2+w*h*h;
a2 = w*h*h*Tair;

A = [a1 -2 0 0 0;
    -1 a1 -1 0 0;
    0 -1 a1 -1 0;
    0 0 -1 a1 -1;
    0 0 0 -1 a1];
b = [w*h^2*Tair-2*h*q0 a2 a2 a2 TL+a2]';

uin = A\b;
u = [uin' 400];
x = 0:h:L;
plot(x,u)