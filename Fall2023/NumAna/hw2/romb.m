%%
clear all
close all
%% Romberg
f = @(x) x.^2.*log(x);
int_f = @(x) (x.^3.*(3.*log(x)-1))./9;

tol = 0.5*1e-8;
a = 1;
b = 3;
n = 2;
R = romberg(f,a,b,n);
count = 0;
while count<2
    n=n+1;
    R= romberg(f,a,b,n);
    if R(n,n)-R(n-1,n-1)>tol
        R_prev = R;
        count = 0;
    else
        count = count+1;
    end
end
error = R(n,n) - (int_f(b)-int_f(a));
fprintf(['Integral is approximatelly = %.6f ' ...
            'when n = %d\n Error = %d\n'] ...
            ,R(n,n),n,error);
function r = romberg(f,a,b,n)
    h = (b-a)./(2.^(0:n-1));
    r(1,1)=(b-a)*(f(a)+f(b))/2;
    for j=2:n
        subtotal = 0;
        for i=1:2^(j-2)
            subtotal = subtotal + f(a+(2*i-1)*h(j));
        end
        r(j,1) = r(j-1,1)/2+h(j)*subtotal;
        for k=2:j
            r(j,k) = ( ...
                4^(k-1)*r(j,k-1)-r(j-1,k-1))/(4^(k-1)-1);
        end
    end
end