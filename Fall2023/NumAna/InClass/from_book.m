clear all; close all;

dx = 0.1;
dt = 0.1;
xl = 0; xr = 1;
yt = 1;

M = (xr - xl) / dx; % Number of space steps
N = yt / dt; % Number of time steps

f = @(x) sin(pi * x);

D = 1 / pi; % Diffusion coefficient

m = M+1;
n = N;

sigma = D * dt / (dx^2);

% Create the tridiagonal matrix 'a'
a = diag(1 - 2 * sigma * ones(m, 1)) + diag(sigma * ones(m - 1, 1), 1);
a = a + diag(sigma * ones(m - 1, 1), -1);

a(1,:)=[1 -1 zeros(1,m-2)]; %left side
a(m,:)=[zeros(1,m-2) -1 1]; %right side 

w(:, 1) = f(xl + (0:M) * dx)'; % Initial conditions

for j = 1:n
    w(:, j + 1) = a * w(:, j) + sigma * [0; zeros(m - 2, 1); 0];
end

%w = [lside; w; rside]; % Attach boundary conditions

x = (0:m -1) * dx;
t = (0:n) * dt;

% Plot the solution
figure;
surf(x, t, w');
title('Solution to the PDE');
xlabel('x');
ylabel('t');
zlabel('solution u(x,t)');
