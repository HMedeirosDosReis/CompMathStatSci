%% 1 
x_0 = 5;
n = 10;
x_n = zeros(n,1);
for i=1:n
    if i == 1
        x_n(i) = mod(3*x_0,150);
    else
        x_n(i) = mod(3*x_n(i-1),150); 
    end 
end
%% *
x_0 = 5;
n = 1e4;
x_n_rand = zeros(n,1);
for i=1:n
    if i == 1
        x_n(i) = mod(3*x_0,150);
    else
        x_n(i) = mod(3*x_n(i-1),150); 
    end 
end
%% mean, var, hist
m = mean(x_n)
v = var(x_n)
hist(x_n)
% output
% m =    75
% v = 2.2502e+03
%% using rand 
x_n = rand(1e4,1);
m = mean(x_n)
v = var(x_n)
hist(x_n)
% output
% m =    0.4982
% v = 0.0831
%% 3 ------ from 0 to 1
rng('default')
a = 0;b = 1;n = 1e6;
u = rand(n,1);
t = (a+(b-a)*u);
hu = (exp(exp(t)))*(b-a);
Exhat = sum(hu)/n
% output 
%Exhat =
%    6.3191
%% 7 -------- -infty to infty
rng('default')
a = 0;b = 1;n = 1e6;
u = rand(n,1);
%u = exp(u)./(1+exp(u));
g = @(x) exp(-x.^2);  % Given function 
hu = g(log(u./(1-u))).*(1./(u.*(1-u))); %g(of transform)*jacobian
Exhat = sum(hu)/n
% output 
%Exhat =
%    1.7744
%% 9 ---- two integrals / 0 to infty and 0 to x
rng('default')
n = 1e6;u = rand(n,1);v = rand(n,1);
% Given function * indicator function from hint
g = @(x,y) exp(-(x+y)).*(y<=x);  % Given function * indicator function 
hu = g(1./u-1,1./v-1).*(1./u.^2).*(1./v.^2); %g(of transform)*jacobian
Exhat = sum(hu)/n 
% output 
%Exhat =
%    0.5000
%% 11
u = rand(n,1);
v = sqrt(1-u.^2);
my_cov = mean(u.*v)-mean(u)*mean(v);
corr = my_cov/(sqrt(var(u)*var(v)))
% output 
%corr =
%    -0.9212
%% b
u = rand(n,1);
v = sqrt(1-u.^2);
my_cov = mean(u.^2.*v)-mean(u.^2)*mean(v);
corr = my_cov/(sqrt(var(u)*var(v)))
% output 
%corr =
%    -1.0156