close all;
clear all;

global L w Tair uL u0
L = 2;          
w = 4;          
Tair = 5;       
uL = 10;        % Boundary condition u(L) = 10
u0 = 0;         % Boundary condition u(0) = 0

% Solve the boundary value problem using the shooting method
param_solution = fzero(@heat_equation, [0 20]);

initial_conditions = [param_solution; 0]; % Updated initial conditions

heat = @(x, u) [u(2); -w * (Tair - u(1))];
[x_sol, u_sol] = ode45(heat,[0 L],[u0 param_solution]);

plot(x_sol, u_sol(:, 1));
xlabel('Position (x)');
ylabel('Temperature (u)');
title('Solution of the Heat Equation');

% Define the heat equation function
function error = heat_equation(param)
global L w Tair uL u0
    % Define the ODE for the heat equation
    heat_ode = @(x, u) [u(2); -w * (Tair - u(1))];
    
    % Define the initial conditions
    initial_conditions = [u0,param];
    
    % Define the spatial domain
    t_span = [0, L];
    
    % Solve the ODE using ODE45
    [x, u] = ode45(heat_ode, t_span, initial_conditions);
    
    % Calculate the error in meeting the boundary condition
    error = u(end, 1) - uL;
end