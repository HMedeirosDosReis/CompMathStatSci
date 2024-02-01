%define cost function and gradient
fa = @(x,a) exp(-norm(x-a)^2);
ga = @(x,a) -2*exp(-norm(x-a)^2)*(x-a);
A = [1 1 -1 -1;...
     1 -1 1 -1];
b = [1 -1 -1 1];

f = @(x) 0.25*(b(1)*fa(x,A(:,1))+b(2)*fa(x,A(:,2))+b(3)*fa(x,A(:,3))+b(4)*fa(x,A(:,4)));
grad = @(x) 0.25*(b(1)*ga(x,A(:,1))+b(2)*ga(x,A(:,2))+b(3)*ga(x,A(:,3))+b(4)*ga(x,A(:,4)));


x = [0.5;0.5]; %initial point
t = 0.01; %GD stepsize

xar = x; %initialize x-array
cost = f(x); %initialize cost array
for k=1:1000
    i = randi(4);
    a = A(:,i);
    b_i = b(i);
    x = x - t*b_i*ga(x,a); %GD update
    
    xar = [xar,x];
    cost = [cost,f(x)];
end

figure(1); %plot trajectories
hold on
[X,Y] = meshgrid(-2:0.01:2,-2:0.01:2);
Z = zeros(size(X));
for i=1:numel(X)
    x = [X(i);Y(i)];
    Z(i) = f(x);
end
figure(1);
surf(X,Y,Z);
shading interp
scatter3(xar(1,:),xar(2,:),cost); view(-15,50);
hold off

%%
figure(2)
plot(cost)
