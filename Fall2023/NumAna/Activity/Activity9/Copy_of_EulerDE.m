%% Euler DE Solver
clear all;
close all;
clc;
% input
f = @(t,y) -21*y+exp(-t);
deltat = 0.1;
tfinal = 2;
N = round(tfinal/deltat);
t(1) = 0; x(1) = 0;

% Euler steps
for i=1:N
    t(i+1) = t(i)+deltat;
    x(i+1) = x(i)+f(t(i),x(i))*deltat;
end

% Output

plot(t,x,"*")
xlabel("t")
ylabel("x")
title("Solution of DE")

xexact = 1/20*exp(-t)-1/20*exp(-21*t);
hold on 
plot(t,xexact)

% More output
t=t';
x=x';
xexact=xexact';
table(t,x,xexact)

% Error 
error = abs(x-xexact);