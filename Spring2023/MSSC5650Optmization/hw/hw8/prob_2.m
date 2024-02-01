%% define variables 
f=@(x)sqrt(1+x(1)^2)+sqrt(1+x(2)^2);
grad=@(x)[x(1)/sqrt(x(1)^2+1);x(2)/sqrt(x(2)^2+1)];
hessian = @(x)diag([1/(x(1)^2+1)^1.5,1/(x(2)^2+1)^1.5]);

%% Run main for-loop
% CONVERGING X
x = [1;1]; 
maxiter = 1000; 
tol = 1e-7;


cost = f(x); %initialize cost array
for k=1:maxiter
    x = x - hessian(x)\grad(x);
    cost = [cost,f(x)]; 
    
    if norm(grad(x)) < tol
        fprintf('algorithm converged at iteration k=%d,\nx1=%e\nx2=%e\n',k,x(1),x(2));
        break;
    end
end 
%% plot cost
plot(cost);


%% Run main for-loop
% DIVERGING X
x = [7;7]; %init with noisy image
maxiter = 1000; 
tol = 1e-7;


cost = f(x); %initialize cost array
for k=1:maxiter
    x = x - hessian(x)\grad(x);
    cost = [cost,f(x)]; %store f(x_k) for plotting
    
    if norm(grad(x)) < tol
        fprintf('algorithm converged at iteration k=%d,\nx1=%e\nx2=%e\n',k,x(1),x(2));
        break;
    end
end 
%% plot cost
plot(cost);
