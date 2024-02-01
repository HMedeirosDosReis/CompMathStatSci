clear all;
close all;
% input 
f = @(x) exp(x-2) + x.^3 - x;

fplot(f,[0.3,1.3])

a = 0.3;
b= 1.3;
p =6;
N = ceil(((-log2((1/2*10^-p)/(b-a)))+log2(1)/log2(2))-1);
% Method
for i = 1:N
    c = (b+a)/2;
    if f(a)*f(c) < 0
        b=c;
    else
        a=c;
    end
end
c = (b+a)/2;

fprintf('Root = %.6f and f(Root) = %.6f\n', c, f(c))
% Output -> Root = 0.788942 and f(Root) = 0.000000
