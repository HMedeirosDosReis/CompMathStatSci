gamma = 0.05;
f = @(x) 0.5*(gamma*x(1)^2 + x(2)^2); %define f(x)
grad = @(x) [gamma*x(1);x(2)];        %define grad f(x)

t0 = 0.05;      %constant stepsize
x = [1;-0.05];  %initial point x0
cost = f(x);    %initialize cost array
xar = x;        %initialize array of iterates (for plotting)
for k=1:100
    if norm(grad(x)) < 1e-16
     break;
    end
    d = -[1/gamma, 0; 0,1]*grad(x); %steepest descent
    t = t0;   
    x = x + t*d;
    cost = [cost,f(x)];
    xar = [xar,x];
end

% plot trajectory of iterates
figure(1);cla;
[X,Y] = meshgrid(linspace(-1.1,1.1,100),linspace(-0.1,0.1,100));
Z = zeros(size(X));
for i=1:length(X(:))
    Z(i) = f([X(i),Y(i)]);
end
hold on
contour(X,Y,Z,50);
plot(xar(1,:),xar(2,:),'.-r','markersize',15,'linewidth',1);
hold off;
set(gca,'fontsize',14);
title('trajectory of iterates x_k');