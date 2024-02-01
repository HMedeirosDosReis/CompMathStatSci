% This program plots the phase portrait for a system of differential equations.
% Current use is for the Predator Model
clear all
close all

% Input parameters
a = 10.1; b = 1.9; m = 10; n = 2;       % Parameters
f = @(x, y) (a - b * y) * x;              % Input RHS of DE
g = @(x, y) (m - n * x) * y;              % Input RHS of DE
Tfinal = 2;                              % Time interval for solution
dt = 0.0001;                              % Deltat for solution
Nfinal = round(Tfinal / dt);             % Calculate number of points for soln

% Create a meshgrid of initial conditions
[x0, y0] = meshgrid(1:10, 1:10);

% Initialize the x and y solution matrices
x = zeros(10,10);
y = zeros(10,10);

% Calculate x and y using Euler's method for all initial conditions
for i = 1:100
    x(i, 1) = x0(i)*0.000001+4.9999;
    y(i, 1) = y0(i)*0.000001+5.3158;
    for k = 1:Nfinal
        x(i, k + 1) = x(i, k) + f(x(i, k), y(i, k)) * dt;
        y(i, k + 1) = y(i, k) + g(x(i, k), y(i, k)) * dt;
    end
end

% Plot the phase portrait
figure(1);
for i = 1:numel(x0)
    plot(x(i, 1), y(i, 1), '*k');          % Plot the initial point
    hold on;
    plot(x(i, :), y(i, :));                % Plot the solutions
end
plot(m / n, a / b, '+b');                 % Plot the equilibrium point
xlim([4.9 5.1]);
ylim([5.2 5.4]);
xlabel('x'); ylabel('y');
title('Bass-Trout Phase Portrait');



% figure(2)                               %Plot solns as a fn of t
% t = 0:dt:Tfinal;                        %Create a time vector
% plot(t,x)
% hold on
% plot(t,y)
% xlabel('Time t'), ylabel('Population Size')
% legend('x = trout','y = bass')
% title('Bass-Trout Solutions')



