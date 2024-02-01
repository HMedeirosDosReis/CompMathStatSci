clear all;
close all;

g = @(x) (sin(x)-5)/6;
f = @(x) x;
hold on
fplot(g,[-1.5,-0.5])
fplot(f,[-1.5,-0.5])

x(1) = 1;
tol = 1e-8;
i = 1; 
deltax = inf;
while deltax > tol
    x(i+1) = g(x(i));
    deltax = abs(x(i+1)-x(i));
    i = i+1;
end

format long
disp(x(i))
disp(sin(x(i))-6*x(i)-5)