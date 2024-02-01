clear all; close all;

dx = 0.1;
dt = 0.01;
xl = 0; xr = 1;
yb = 0; yt = 1;

M = (xr - xl) / dx; % Number of space steps
N = (yt - yb) / dt; % Number of time steps

f = @(x) sin(pi * x);

alphsq = 1 / pi; % Conduction (diffusion) coefficient

m = M - 1;
n = N;

R = alphsq * dt / (dx^2);

% Create the tridiagonal matrix 'A'
A = diag(1 + 2 * R * ones(m, 1)) + diag(-R * ones(m - 1, 1), 1);
A = A + diag(-R * ones(m - 1, 1), -1);

lside = zeros(1, n+1);
rside = zeros(1, n+1);

u(:, 1) = f(xl + (1:m) * dx)'; % Initial conditions

for j = 1:n
    u(:, j + 1) = A \ (u(:, j) + R * [0; zeros(m - 2, 1); 0]);
end

u = [lside; u; rside]; % Attach boundary conditions

x = (0:m + 1) * dx;
t = (0:n) * dt;

% Plot the solution
figure;
surf(x, t, u');
title('Solution to the PDE (Backward Difference)');
xlabel('x');
ylabel('t');
zlabel('solution u(x,t)');
