clear all;
close all;

%% Composite trap
f = @(x) x.^2.*log(x);
int_f = @(x) (x.^3.*(3.*log(x)-1))./9;
m(1) = 0;
for i=1:8
    m(i+1)=2.^i;
end
a = 1;
b = 3;
m_size = size(m);
error(1) = 0;
for i = 0:m_size(2)-1
error(i+1) = composite_simp(f,int_f,m(i+1),a,b);
end
h = (b-a)./m;
h(1) = (b-a);
loglog(h,error)

slope = (log(error(8))-log(error(7)) ...
    )/(log(h(8))-log(h(7)));
fprintf('Slope = %.8f', slope)

%% Define the function so we can use it future problems
function error = composite_simp(f,int_f,m,a,b)
    for i = m
        if i==0
            h=(b-a);
        else
            h = (b-a)/(2*i);
        end
        x_i = a+h:h:b-h;
        
        intg = h/3*( ...
            f(a)+4*sum(f(x_i(1:2:end)))+ ...
            2*(sum(f(x_i(2:2:end-1))))+f(b));
        
        exact = int_f(b)-int_f(a);
        error = abs(exact-intg);
    end
end