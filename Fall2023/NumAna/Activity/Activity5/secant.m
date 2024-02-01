clear all;
close all;

f = @(x) x^4-2;
x(1) = 1;
x(2) = 1.1;

tol = 1e-7;
deltax = inf;
i = 2;
while deltax > tol
    x(i+1) = x(i)-(f(x(i))*(x(i)-x(i-1)))/(f(x(i))-f(x(i-1)));
    deltax = abs(x(i+1)-x(i));
    i = i+1;
end

fprintf(['Algorithm converged after %d ' ...
    'iterations, and the root is %.4f. ' ...
    '\n f(root) = %.8f\n'] ,i,x(i),f(x(i)))