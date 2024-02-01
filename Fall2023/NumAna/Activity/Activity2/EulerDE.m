%% Euler DE Solver
clear all;
close all;
clc;
% input
f = @(t,x) 1/x^2;
deltat = 0.1*2.^(-(0:5));
tfinal = 5;

error = zeros(size(deltat));

% Euler steps
for j=1:size(deltat,2)
    t(1) = 0; x(1) = 1;
    N = round(tfinal/deltat(j));
    for i=1:N
        t(i+1) = t(i)+deltat(j);
        x(i+1) = x(i)+f(t(i),x(i))*deltat(j);
    end
    % Error
    x_exact = (3*t+1).^(1/3);
    error(j) = abs(x(end) - x_exact(end));
end
% Plot error vs deltat
loglog(deltat,error,'-o');
xlabel('deltat');
ylabel('Error');
title('Euler Error vs Step Size');

