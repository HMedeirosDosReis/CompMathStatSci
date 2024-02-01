clear all; close all;

% Define parameters
xl = 0; xr = 1;
t0 = 0; T = 1;
x_target = 0.3;
t_target = 1;

% Exact solution
exact_solution = @(x, t) exp(-pi * t) * sin(pi * x);

% Display header for the table
fprintf('--------------------------------------------------------\n');
fprintf('   t       |  x_approximate  |    x_exact     |     Error\n');
fprintf('--------------------------------------------------------\n');

% Loop over different time step sizes
for dt = [0.02, 0.01, 0.005]
    dx = 0.1; % Space step size
    
    M = (xr - xl) / dx; % Number of space steps
    N = (T - t0) / dt; % Number of time steps
    
    f = @(x) sin(pi * x);
    l = @(t) 0 * t;
    r = @(t) 0 * t;

    alphsq = 1; % Conduction (diffusion) coefficient
    R = alphsq * dt / (dx^2);

    m = M - 1;
    n = N;

    % Create the tridiagonal matrix 'A'
    A = diag(1 + 2 * R * ones(m, 1)) + diag(-R * ones(m - 1, 1), 1);
    A = A + diag(-R * ones(m - 1, 1), -1);

    lside = l(t0 + (0:n) * dt);
    rside = r(t0 + (0:n) * dt);

    % Adjust the size of u to match the number of space steps
    u = zeros(m, n+1);

    u(:, 1) = f(xl + (1:m) * dx)'; % Initial conditions

    for j = 1:n
        u(:, j + 1) = A \ (u(:, j) + R * [lside(j); zeros(m - 2, 1); rside(j)]);
    end

    u = [lside; u; rside]; % Attach boundary conditions

    x_values = xl + (0:m + 1) * dx;
    t_values = t0 + (0:n) * dt;

    % Find indices corresponding to x = 0.3 and t = 1
    x_index = find(abs(x_values - x_target) < 1e-6);
    t_index = find(abs(t_values - t_target) < 1e-6);

    % Extract exact and approximate values
    exact_value = exact_solution(x_values(x_index), t_values(t_index));
    approximate_value = u(x_index, t_index);

    % Calculate error
    error = abs(approximate_value - exact_value);

    % Display results in the table
    fprintf('   %.3f   |    %.8f   |   %.8f   |   %.8f\n', ...
        dt, approximate_value, exact_value, error);
end

fprintf('--------------------------------------------------------\n');
