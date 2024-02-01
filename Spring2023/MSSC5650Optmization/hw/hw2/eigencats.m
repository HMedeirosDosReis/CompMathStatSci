%% load dataset
load cat_faces_subset %each row of X is a vectorized 64x64 image
dim = [64,64]; %image dimensions
%% compute eigenvalues & eigenvectors of covariance matrix
mu = mean(X);         %mean image as row vector
Y = X-mu;             %de-mean every image
C = (Y'*Y)/size(Y,1); %data covariance matrix
[V, D] = eig(C);      %V = eigenvectors
eigval = diag(D);     %eigenvalues

%sort eigenvalues in descending order
[eigval,ind] = sort(eigval,'desc'); 
V = V(:,ind); %reorder eigenvectors as well
mu = mu'; %convert mu to column vector to simplify formulas below

% display top 25 eigencats as images (columns 1-25 of V)
figure(1)
for i=1:25
    subplot(5,5,i)
    imagesc(reshape(V(:,i),dim)); colormap(gray); axis image
    title(sprintf('eigencat %d',i));
end
%% part(a): Synthesize random cats
%  fill in code here
Vhat = V(:,1:50);
r = randn(50,1);
x = Vhat*r + mu;

imagesc(reshape(x,dim)); colormap(gray); axis image;
%% part(b): Compute distances onto "cat space"
%  fill in code here
load test_images.mat

dFromCS = @(y) norm(y-Vhat*Vhat'*y)/norm(y);
dx1 = dFromCS(x1-mu);
dx2 = dFromCS(x2-mu);
dx3 = dFromCS(x3-mu);
disp(dx1);
disp(dx2);
disp(dx3);