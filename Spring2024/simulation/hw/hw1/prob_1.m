%% n=4 
a=0;b=1;n=4;
dx = (b-a)/n;
xpts = (a+dx/2:dx:b)';
gpts = exp(exp(xpts));
Exhat = dx*sum(gpts)
% output 
%Exhat =
%    6.2194
%% n=100
a=0;b=1;n=100;
dx = (b-a)/n;
xpts = (a+dx/2:dx:b)';
gpts = exp(exp(xpts));
Exhat = dx*sum(gpts)
% output 
%Exhat =
%    6.3164