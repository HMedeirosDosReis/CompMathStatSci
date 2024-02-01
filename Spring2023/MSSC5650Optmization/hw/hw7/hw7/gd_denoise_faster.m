%image denoising using regularized least squares
I = imread('merganser.png'); %can load your own image, too
I = rgb2gray(I);
I = im2double(I);
I = I(200:800,1:1200);
dim = size(I);
b = I(:);

% show original noisy image
fig = figure;
imshow(reshape(b,dim),[0,1]);
title('noisy image');
set(gca,'fontsize',16);
set(fig,'position',[10 100 1000 500]);
%% Define edge-preserving regularization
%define vertical and horizontal finite differences
h1 = [1 -1];
L1 = convmtx2(h1,dim); %horiztonal differences matrix
h2 = [1;-1];
L2 = convmtx2(h2,dim); %vertical differences matrix
L = [L1; L2]; %stack matrices
I = speye(prod(dim));

delta = 0.01;
phi = @(t) delta*(sqrt(1+(t/delta).^2)-1);
dphi = @(t) (1/delta)*(t./sqrt(1+(t/delta).^2));

R = @(x) sum(phi(L*x));
gradR = @(x) L'*dphi(L*x);

lambda = 0.1;
f = @(x) norm(x-b)^2 + lambda*R(x);
grad = @(x) 2*(x-b) + lambda*gradR(x);
%% Run main for-loop
x = b; %init with noisy image
maxiter = 100; 
tol = 0.05;
s = 0.5;
beta = 0.5;
alpha = 0.25;

tic
cost = f(x); %initialize cost array
for k=1:maxiter
    d = -grad(x); %steepest descent direction
    f_x = f(x);
    t = s; %initial stepsize
    while (f_x - f(x+t*d)) < t*alpha*d'*d
        t = beta*t; %shrink stepsize
    end 
    x = x + t*d;
    
    cost = [cost,f_x]; %store f(x_k) for plotting
    
    if norm(grad(x)) < tol
        fprintf('algorithm converged at iteration k=%d\n',k);
        break;
    end
end 
toc
%% plot results
figure(2);
plot(cost);

fig = figure(1);
imshow(reshape(x,dim),[0,1]);
title('denoised image');
set(gca,'fontsize',16);
set(fig,'position',[10 100 1000 500]);

