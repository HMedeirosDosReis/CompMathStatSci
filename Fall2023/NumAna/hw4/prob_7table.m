clear all; close all;

xl = 0;

% Display header for the table
fprintf('--------------------------------------------------------\n');
fprintf('   t       |  x_approximate  |    x_exact     |     Error\n');
fprintf('--------------------------------------------------------\n');

% Loop over different time step sizes
for dt = [0.02, 0.01, 0.005]
    dx = 0.1;

    w=heatbdn(0,1,0,1,1/dx,1/dt);

    
end

fprintf('--------------------------------------------------------\n');


function w=heatbdn(xl,xr,yb,yt,M,N)
% Exact solution
exact_solution = @(x, t) 2/pi;
x_target = 0.3;
t_target = 1;
f=@(x) sin(pi*x);
dx = 1/M; dt = 1/N;t0 = 0;
D=1; % diffusion coefficient
h=(xr-xl)/M; k=(yt-yb)/N; m=M+1; n=N;

sigma=D*k/(h*h);

a=diag(1+2*sigma*ones(m,1))+diag(-sigma*ones(m-1,1),1);
a=a+diag(-sigma*ones(m-1,1),-1); % define matrix a
a(1,:)=[1 -1 zeros(1,m-2)]; % Neumann conditions
a(m,:)=[zeros(1,m-2) -1 1];
w(:,1)=f(xl+(0:M)*h)'; % initial conditions
for j=1:n
b=w(:,j);b(1)=0;b(m)=0;
w(:,j+1)=a\b;
end

x_values = xl + (0:m + 1) * dx;
    t_values = t0 + (0:n) * dt;

    x_index = find(abs(x_values - x_target) < 1e-6);
    t_index = find(abs(t_values - t_target) < 1e-6);

    % Extract exact and approximate values
    exact_value = exact_solution(x_values(x_index), t_values(t_index));
    approximate_value = w(x_index, t_index);

    % Calculate error
    error = abs(approximate_value - exact_value);

    % Display results in the table
    fprintf('   %.3f   |    %.8f   |   %.8f   |   %.8f\n', ...
        dt, approximate_value, exact_value, error);
x=(0:M)*h;t=(0:n)*k;
surf(x,t,w') % 3-D plot of solution w
view(60,30);axis([xl xr yb yt -1 1])
end