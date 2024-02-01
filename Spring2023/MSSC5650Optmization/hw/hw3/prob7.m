%% Define a function f(X), that takes as input a column vector 
f = @(x) exp(1)^(-norm(x)^2);
%% Helper funcions
grad = @(x) -2*x*exp(-norm(x)^2);
Hessian = @(x) -2*eye(10)* ...
    exp(1)^(-norm(x)^2)+4*x*x'*exp(1)^(-norm(x)^2);
%% Define a function Q(x,x0), that the output is the equation * 
Q = @(x,x0) f(x0)+grad(x0)'* ...
    (x-x0)+1/2*(x-x0)'*Hessian(x0)*(x-x0);
%%
x0 = ones(10,1);
rng(1); %fix random seed
d = randn(10,1);
d = d/norm(d);
err = [];
%%
for k=1:200
    ep = 1/k;
    x = x0+ep*d;
    err(end+1)= abs(f(x)-Q(x,x0))/ep^2;
end
%%
semilogy(err);


