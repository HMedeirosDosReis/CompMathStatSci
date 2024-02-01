clear all;
close all;

g = @(x) (-2*x^3+1)/-6;
f = @(x) x;
hold on
fplot(g,[-2,2])
fplot(f,[-2,2])

x(1) = -1.5;
tol = 1e-7;
i = 1; 
deltax = inf;
while deltax > tol
    x(i+1) = g(x(i));
    deltax = abs(x(i+1)-x(i));
    i = i+1;
end

format long
h = 0.0001; 
derivative_g = (g(x(i)+h) - g(x(i)-h))/(2*h);

S = abs(derivative_g);

findr = [2 0 -6 -1];
root = roots(findr);

error_i1 = abs(g(x(i))-root(3));
error_i = abs(x(i)-root(3));
Sdiv = error_i1/error_i;

fprintf("First root = %.6f, S from Calc = %.6f" + ...
    ", S from errors = %.6f\n", x(i),S,Sdiv);

