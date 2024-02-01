clear all;
close all;


f = @(x) x^4-2;
g_1 = @(x) x/2+1/x^3;
g_2 = @(x) (2/3)*x+(2/(3*x^3));

x(1) = 1;
y(1) = 55;
tol = 1e-3;
deltax = inf;
i = 1;
while deltax > tol
    x(i+1) = g_1(x(i));
    deltax = abs(x(i+1)-x(i));
    i = i+1;
end
fprintf(['Algorithm converged after %d ' ...
    'iterations, and the root is %.4f. ' ...
    '\n f(root) = %.8f\n'] ,i,x(i),f(x(i)))

y(1) = 1;
tol = 1e-7;
deltax = inf;
i = 1;
while deltax > tol
    y(i+1) = g_2(y(i));
    deltax = abs(y(i+1)-y(i));
    i = i+1;
end


fprintf(['Algorithm converged after %d ' ...
    'iterations, and the root is %.4f. ' ...
    '\n f(root) = %.8f\n'] ,i,y(i),f(y(i)))