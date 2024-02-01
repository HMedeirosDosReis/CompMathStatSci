clear all; 
close all;
%% Adaptive Simpson quadrature

f = @(x) x.*exp(x);
a = 0;
b = 1;
tol = 0.5*1e-8;
[n,int] = adapquad(f,a,b,tol);

fprintf(['Integral is approximatelly = %.8f ' ...
            'when n = %d\n '],int,n);

function [subint,int] =adapquad(f,a0,b0,tol0)
    int=0; n=1; a(1)=a0; b(1)=b0; tol(1)=tol0; 
    app(1)=simpson(f,a,b);
    subint = 1;
    while n>0 % n is current position at end of the list
        c=(a(n)+b(n))/2; oldapp=app(n);
        app(n)=simpson(f,a(n),c);
        app(n+1)=simpson(f,c,b(n));
        if abs(oldapp-(app(n)+app(n+1)))<10*tol(n)
            int=int+app(n)+app(n+1); % success
            n=n-1; % done with interval
        else % divide into two intervals
            b(n+1)=b(n); b(n)=c; % set up new intervals
            a(n+1)=c;
            tol(n)=tol(n)/2; tol(n+1)=tol(n);
            n=n+1; % go to end of list, repeat
        end
        subint = subint+1;
     end
end
function s=simpson(f,a,b)
s=(f(a)+f(b)+4*f((a+b)/2))*(b-a)/6;
end