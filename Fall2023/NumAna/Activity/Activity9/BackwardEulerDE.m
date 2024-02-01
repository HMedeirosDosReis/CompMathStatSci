%% Backwards Euler DE Solver
clear all;
close all;
clc;
% input
f = @(t,y) 10-10*y;
deltat = 1/5;
tfinal = 2;
N = round(tfinal/deltat);
t(1) = 0; x(1) = 1/2;

% Backward Euler steps
for i=1:N
    t(i+1) = t(i)+deltat;
    x(i+1) = (x(i)+10*deltat)/(1+10*deltat);
end

% Output

plot(t,x,"*")
xlabel("t")
ylabel("x")
title("Solution of DE")

xexact = 1-1/2*exp(-10*t);
hold on 
plot(t,xexact)

% More output
t=t';
x=x';
xexact=xexact';
table(t,x,xexact)

% Error 
error = abs(x-xexact);