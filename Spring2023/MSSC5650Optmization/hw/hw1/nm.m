f = @(x) 0.5*x.^2 - sin(x);
df = @(x) x - cos(x);
d2f = @(x) 1 + sin(x);

x = 0.5;

iter = 500;
f_k = [f(x)];
for k=1:iter
    xk = x;
    tau = 1/d2f(x);
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