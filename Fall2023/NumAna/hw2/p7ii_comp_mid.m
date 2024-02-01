clear all;
close all;

%% Composite midpoint rule
f = @(x) x.^2;
int_f = @(x) x.^3./3;
m = [1 2 4];
a = 0;
b = 1;
composite_midpoint(f,int_f,m,a,b)

%% Define the function so we can use it future problems 
function composite_midpoint(f,int_f,m,a,b)
    for i = m
        h = (b-a)/i;
        x_i = a + h/2 : h : b - h/2; % Midpoints
        
        intg = h * sum(f(x_i));
        
        exact = int_f(b) - int_f(a);
        error = abs(exact - intg);
        fprintf(['Integral is approximately = %.6f ' ...
            'when m = %d\n Error = %.6f\n'] ...
            , intg, i, error);
    end
end