clear all;
close all;
% input 
f = @(x) sin(x)-6*x+5;

fplot(f,[0,1])

a = 0;
b = 1;

c = (b-a)/2;
N = ceil(((-log((1/2*10^-6)/(b-a)))+log(1)/log(2))-1);

% Method
for i = 1:100
    c = (b-a)/2;
    if f(a)*f(c) < 0
        b=c;
    else
        c=a;
    end
end
c = (b-a)/2;
disp(c)
