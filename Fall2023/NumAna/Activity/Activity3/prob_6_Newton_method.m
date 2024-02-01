clear all;
close all;

f = @(x) exp(x)+x-7;
df = @(x) exp(x)+1;

x(1) = 1;

tol = 1e-8;
deltax = inf;
i = 1;
while deltax > tol 
    x(i+1) = x(i)-f(x(i))/df(x(i));
    deltax = abs(x(i+1)-x(i));
    i = i+1;
end

fprintf(['Algorithm converged after %d ' ...
    'iterations, and the root is %.4f. ' ...
    '\n f(root) = %.8f\n'] ,i,x(i),f(x(i)))