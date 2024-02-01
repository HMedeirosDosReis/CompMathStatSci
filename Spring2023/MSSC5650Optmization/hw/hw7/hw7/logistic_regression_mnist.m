%logistic regression on mnist 3's and 8's
load mnist38

Ntrain = 50; %number of training examples
dim = [20,20]; %image dimensions

A0 = reshape(threes_train(:,:,1:Ntrain),[prod(dim),Ntrain]);
A1 = reshape(eights_train(:,:,1:Ntrain),[prod(dim),Ntrain]);
A = [A0, A1];
meanim = mean(A,2);
A = A-meanim; %center data;
b = [zeros(Ntrain,1); ones(Ntrain,1)]; %labels;

sigma = @(x) 1./(1+exp(-x));
lambda = 1.5;
% TASK: edit the two lines below 
% to implement *regularized* logistic regression
f = @(x) -sum(b.*log(sigma(A'*x))+(1-b).*log(1-sigma(A'*x)))+lambda*norm(x);
grad = @(x) A*(sigma(A'*x)-b)+lambda*2*x;

rng(1);
x = randn(prod(dim),1); %random initialization

t0 = 0.001;
tol = 1; %convergence tolerance

cost = f(x); %initialize cost array
gradx = grad(x);
for k=1:1000
    x = x - t0*gradx;
    fx = f(x);
    gradx = grad(x);
    
    if isnan(fx)
        fprintf('cost diverged to -Inf; exiting\n');
        break;
    end
    
    if norm(gradx) < tol
        fprintf('converged at iteration k=%d\n',k);
        break;
    end
    
    cost = [cost,fx];
end
%
figure(1);
plot(cost);
set(gca,'fontsize',14);
title('cost vs. iteration','fontsize',18);

% prediction accuracy on training set
predvec = double(sigma(A'*x) >= 0.5);
fprintf('percent correct on training set = %2.2f %%\n',(1-sum(abs(b-predvec))/length(b))*100)
%
figure(2);
imshow(imresize(reshape(x,[20,20]),20,'nearest'),[]); colorbar;
title('learned weights x','fontsize',18);
%
Ntest = 100;
A0t = reshape(threes_test,[prod(dim),Ntest]);
A1t = reshape(eights_test,[prod(dim),Ntest]);
At = [A0t, A1t];
At = At-meanim; %center data;
bt = [zeros(Ntest,1); ones(Ntest,1)]; %labels;

predvec = double(sigma(At'*x) >= 0.5);
fprintf('percent correct on test set = %2.2f %%\n',(1-sum(abs(bt-predvec))/length(b))*100)