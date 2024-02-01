clear all;
close all;
%%
f = @(x) (x+1)./2.*exp((x+1)./2).*(1/2);
c_i_n3 = [5/9 8/9 5/9];
x_i_n3 = [-sqrt(3/5) 0 sqrt(3/5)];
approx = sum(c_i_n3.*f(x_i_n3));

fprintf('Integral is approximatelly = %.4f\n',approx)