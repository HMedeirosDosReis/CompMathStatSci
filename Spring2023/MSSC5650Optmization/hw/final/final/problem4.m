load problem4_data.mat 
%loads variables t and y, both are m-by-1 vectors with m=50.
g = @(t,a,b,c) a*exp(-b*(t-c).^2); %define vector-valued function g(x)

a = 0;
b = 0;
c = 0;
x = [a;b;c]; %initialize optimization variable
epsilon = 1e-8;
for k=1:20
    a = x(1);
    b = x(2);
    c = x(3);
    
    r = g(t,a,b,c) - y; %residual vector
    
    % fill in rest of the algorithm
    % J = ... define the Jacobian
    J = [exp(-b*(t-c).^2);
        -a*(t-c).^2.*exp(-b*(t-c).^2);
        2*b*a*(t-c).*exp(-b*(t-c).^2)];
    % EXPLAIN 
    J = reshape(J,[50,3]);
    n = size(J);
    n = n(2);
    % x = ... define the x update
    x = x - (J'*J+epsilon*eye(n))\(J'*(g(t,a,b,c)-y));
end
% plot for part (d)
a = x(1);
b = x(2);
c = x(3);
fprintf("Best parameters \na=%.8f\nb=%.8f\nc=%.8f\n",a,b,c)
figure(1);
cla
hold all
scatter(t,y);
plot(-8:0.01:8,g(-8:0.01:8,a,b,c),'linewidth',1);
hold off
legend('y','G(t)');
set(gca,'fontsize',16);