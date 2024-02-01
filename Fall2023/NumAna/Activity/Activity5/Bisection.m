clear all;
close all;
% input 
f = @(x) x^4-2;

fplot(f,[0,2])

a = 0.8;
b= 1.2;
p =8;
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

fprintf(['Algorithm converged after %d ' ...
    'iterations, and the root is %.4f. ' ...
    '\n f(root) = %.8f\n'] ,N,c,f(c))
