f = @(x) x(1).^4+x(2).^4;
grad = @(x) [4*x(1).^3;4*x(2).^3]; %define grad f(x)

x = [1;0.5];      %inital point
cost = f(x);      %initialize cost array
xar = x;          %initialize array of iterates (for plotting)
tol = 1e-16;      %exit tolerance   
for k=1:100
    t = (x(1).^2+x(2).^2)/(4*x(1).^4+4*x(2).^4); %modify this
    x = x - t*grad(x); %gradient descent with constant step-size
    
    cost = [cost,f(x)]; %store f(x_k) for plotting
    xar = [xar,x];
    
    if norm(grad(x)) < tol
        fprintf('algorithm converged at iteration k=%d\n',k);
        disp(x)
        break;
    end
end
%
% plot trajectory of iterates
figure(1);cla;
[X,Y] = meshgrid(linspace(-1.1,1.1,100),linspace(-1.1,1.1,100));
Z = zeros(size(X));
for i=1:length(X(:))
    Z(i) = f([X(i),Y(i)]);
end
hold on
contour(X,Y,Z,50);
plot(xar(1,:),xar(2,:),'.-r','markersize',15,'linewidth',1);
axis square
hold off;
set(gca,'fontsize',14);
title('trajectory of iterates x_k');