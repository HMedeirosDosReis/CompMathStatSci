clear all;
close all;

f = @(P,V,n,a,b,R,T) P*V+n^2*a*n*b/V^2+n^2*a*V/V^2-P*n*b-n*R*T;
df = @(P,a,n,b,V) P-2*b*n^3*a/V^3-a*n^2/V^2;

R = 0.0820575;
T = 700;
P = 20;
n = 1;
a = 18;
b = 0.1154;

V(1) = n*R*T/P;


tol = 1e-7;
deltax = inf;
i = 1;
while deltax > tol 
    V(i+1) = V(i)-f(P,V(i),n,a,b,R,T)/df(P,a,n,b,V(i));
    deltax = abs(V(i+1)-V(i));
    i = i+1;
end

fprintf(['Algorithm converged after %d ' ...
    'iterations. \n V(final) = %.8f ' ...
    '\n f(root) = %.8f' ...
    '\n Initial guess: %.8f\n'] ...
    ,i,V(i),f(P,V(i),n,a,b,R,T),V(1))