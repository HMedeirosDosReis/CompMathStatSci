clear all;
close all;

g_1 = @(x) -3/2*x +5/2;
g_2 = @(x) -1/2*x +3/2;

x(1) = 0.8;
y(1) = 0.8;
N = 1000;
for i=1:N
    x(i+1) = g_1(x(i));
    y(i+1) = g_2(y(i));
end
x(N)
y(N)