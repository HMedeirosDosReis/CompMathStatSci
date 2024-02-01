%% a
a=-100;
b=200;
n=200;
dx = (b-a)/n;
xpts = (a+dx/2:dx:b)';
ypts = xpts;
mu1 = 10;mu2 = 5; sig1 = 2; sig2 = 3;
f = @(x,y) exp(-((x-mu1).^2)./(2*sig1.^2))./(sqrt(2*pi*sig1.^2))...
    .*exp(-((y-mu2).^2)./(2*sig2.^2))./(sqrt(2*pi*sig2.^2));
gpts = zeros(n,1);
for i=1:n
    gpts(i) = sum(xpts.*f(xpts, ypts(i)));%function
end
Exhat = dx*dx*sum(gpts)
% output 
%Exhat =
%    10.0000
%%
clear all;
%% b
rng('default')
n = 1e7;
u = rand(n,1);
v = rand(n,1);
mu1 = 10;mu2 = 5; sig1 = 2; sig2 = 3;
% need to transform mu and sigma?
mu1 = exp(mu1)/(1+exp(mu1));
mu2 = exp(mu2)/(1+exp(mu2));
sig1 = exp(sig1)/(1+exp(sig1));
sig2 = exp(sig2)/(1+exp(sig2));
% the function and the jacobian are correct
g = @(x,y) x.*exp(-((x-mu1).^2)./(2*sig1.^2))./(sqrt(2*pi*sig1.^2))...
    .*exp(-((y-mu2).^2)./(2*sig2.^2))./(sqrt(2*pi*sig2.^2));  % Given function 
hu = g(log(u./(1-u)),log(v./(1-v)))...
    .*(1./((u-u.^2).*(v-v.^2))); %g(of transform)*jacobian 
% this is returning 1, and it should return 10?
Exhat = sum(hu)/n
%% try 2 b 
rng('default')
n = 1e7;
u = rand(n,1);
v = rand(n,1);
mu1 = 10;mu2 = 5; sig1 = 2; sig2 = 3;
% the function and the jacobian are correct
g = @(x) x.*exp(-((x-mu1).^2)./(2*sig1.^2))./(sqrt(2*pi*sig1.^2));
f = @(y) exp(-((y-mu2).^2)./(2*sig2.^2))./(sqrt(2*pi*sig2.^2));
    %.*exp(-((y-mu2).^2)./(2*sig2.^2))./(sqrt(2*pi*sig2.^2));  % Given function 
hu = g(log(u./(1-u))).*(1./((u-u.^2))); %g(of transform)*jacobian 
hu = g(log(v./(1-v))).*(1./((v-v.^2))); %g(of transform)*jacobian 
% this is returning 1, and it should return 10?
Exhat = sum(hu)/n
% output 
%Exhat =
%    9.8575