f = @(x) x.^4-x.^3+2;
df = @(x) 4*x.^3-3*x.^2;

x = 0.5;
tau = 0.1;

iter = 500;
f_k = [f(x)];
for k=1:iter
    xk = x;
    x = x - tau*df(x);
    f_k(end+1) = f(x);
    if abs(x - xk) < 10e-6
        break;
    end
end
disp(x);
disp("    iter:" + k)

figure(1);
plot(f_k,'linewidth',2);
ylabel('cost');
xlabel('iteration');
set(gca,'fontsize',18);
set(gca,'linewidth',2);