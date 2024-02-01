clear all;
close all;

f = @(x) exp(x)+x-7;

a = 1;
b = 2;
x(1) = b;
tol = 1e-8;
deltax = inf;
i = 1;
while deltax > tol  
    c = (b*f(a)-a*f(b))/(f(a)-f(b));
    if c==0
        x(i+1) = c;
        break;
    end
    if f(a)*f(c) < 0
        b = c;
        x(i+1) = b;
    else
        a = c;
        x(i+1) = a;
    end
    deltax = abs(x(i+1)-x(i));
    i = i+1;
end

fprintf(['Algorithm converged after %d ' ...
    'iterations, and the root is %.4f. ' ...
    '\n f(root) = %.8f\n'] ,i,x(i),f(x(i)))