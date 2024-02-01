clear all;
close all;

g = @(x) 5/(16*(x+1));
f = @(x) x;
hold on
fplot(g,[-2,2])
fplot(f,[-2,2])

x(1) = 800;
tol = 1e-6;
i = 1; 
deltax = inf;
while deltax > tol
    x(i+1) = g(x(i));
    deltax = abs(x(i+1)-x(i));
    i = i+1;
end

disp(x)