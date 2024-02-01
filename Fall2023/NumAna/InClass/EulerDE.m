%% Euler DE Solver
clear all;
close all;
clc;
% input
f = @(t,x) 1/x^2;
deltat = 0.05;
tfinal = 5;
N = round(tfinal/deltat);
t(1) = 0; x(1) = 1;

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

xexact = (3.*t+1).^(1/3);
hold on 
plot(t,xexact)

% More output
t=t';
x=x';
xexact=xexact';
table(t,x,xexact)

% Error 
error = abs(x-xexact);