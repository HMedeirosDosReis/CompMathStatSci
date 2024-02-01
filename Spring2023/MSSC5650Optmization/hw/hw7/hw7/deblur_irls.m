% Deblurring using a non-quadratic regularizer
% min_x ||Ax-b||^2 + lambda*R(Lx)
% where R(y) = \sum_{i=1}^n phi(y_i) 
% for some scalar "potential function" phi(t)
%% load and view blurry image
I = imread('robin.png');
I = rgb2gray(I);
I = im2double(I);
I = imresize(I,0.5);
I = padarray(I,[2,2]);
dim = size(I);
b = I(:);

%visualize blurry image
fig = figure(1);
imshow(reshape(b,dim),[0,1]);
title('blurry image');
set(gca,'fontsize',16);
set(fig,'position',[10 100 500 400]);
%% definitions
h = fspecial('gaussian',5,1); 
A = convmtx2(h,dim-[4,4]); %% A matrix

%define vertical and horizontal finite differences
h1 = [1 -1];
L1 = convmtx2(h1,dim-[4,4]); %horiztonal differences matrix
h2 = [1;-1];
L2 = convmtx2(h2,dim-[4,4]); %vertical differences matrix
L = [L1; L2]; %stack matrices

delta = 0.01;
phi = @(t) delta*(sqrt(1+(t/delta).^2)-1);
omega = @(t) (1/delta)*(1./sqrt(1+(t/delta).^2));
%% run IRLS alg
x = zeros(size(A,2),1); %initialize x
lambda = 0.001;
maxiter = 10;
cost = 0.5*norm(A*x-b)^2+lambda*sum(phi(L*x)); %initialize cost array
for k=1:maxiter
    left = (A'*A+lambda*L'*spdiag(omega(L*x))*L);
    x = left\(A'*b);
    cost = [cost,0.5*norm(A*x-b)^2+lambda*sum(phi(L*x))]; %store f(x_k) for plotting
end 
%% visualize result
fig = figure(2);
subplot(1,2,1);
imshow(reshape(b,dim),[0,1]);
title('original image');
set(gca,'fontsize',16);
subplot(1,2,2);
imshow(reshape(x,dim-[4,4]),[0,1]);
title('deblurred image');
set(gca,'fontsize',16);
set(fig,'position',[10 100 1200 400]);

figure(3)
plot(cost)