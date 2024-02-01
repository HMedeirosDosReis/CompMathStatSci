f = @(x) 0.5*x.^2 - sin(x);
df = @(x) x - cos(x);

x = 0.5;
tau = 0.1;

iter = 500;
cost = [f(x)];
for k=1:iter
    xk = x;
    x = x - tau*df(x);
    cost(end+1) = f(x);
    if abs(x - xk) < 10e-6
        break;
    end
end
disp(x);
disp(k)
figure(1);
plot(cost,'linewidth',2);
ylabel('cost');
xlabel('iteration');
set(gca,'fontsize',18);
set(gca,'linewidth',2);