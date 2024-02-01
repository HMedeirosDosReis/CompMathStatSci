clear all;
close all;
%% f
n = 100;
e = ones(n,1);
A = spdiags([e -2*e e],-1:1,n,n);
b = 1;
a = 0;
h = (b-a)/(n+1);

u0 = 0; uf = 0;
b_vec = 1/2*h.^2*ones(n,1);
b_vec(1) = b_vec(1)+u0;
b_vec(end) = b_vec(end)+uf;

u = A\b_vec;
u = [u0 u' uf];
x = 0:h:1;
plot(x,u)
%%
f = @(x) 1/6*(x.^3-x);
figure;
fplot(f,[0 1])