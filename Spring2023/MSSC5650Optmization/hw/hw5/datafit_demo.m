%% generate noisy samples from from 4th degree polynomial
rng(1); %fix random seed

m = 3; %number of data-points
f = @(x) 1 -2*x + x.^2 - 3*x.^3 + x.^4;
x = 2.5*(2*rand(m,1)-1); %sample from interval [-2.5,2.5]
y = f(x) + 2*randn(m,1); %noisy samples

figure(1);
scatter(x,y,50,'DisplayName','original data');
legend;
set(gca,'fontsize',18);
axis([-3 3 -20 100]);
%% solve for coefficients c using "backslash"
d = 5;
X = vandermonde(x,d);
c = X\y;
c1 = leastNormSolution(X,y);
c2 = lsqminnorm(X,y);
% plot result on top of scattered data
xp = linspace(-3,3,100);
Xp = vandermonde(xp,d);
poly = Xp*c;
poly1 = Xp*c1;
poly2 = Xp*c2;

figure(1);
hold all;
plot(xp,poly, xp,poly1,xp,poly2,'DisplayName',sprintf('d=%d',d),'linewidth',1.5);
hold off;
legend;
set(gca,'fontsize',18);
axis([-3 3 -20 100]);

%% helper functions
function x0 = leastNormSolution(A, b)
    % Compute the reduced QR factorization of A'
    [Q, R] = qr(A',0);
    %Q = Q(:, 1:size(A, 1));
    %R = R(1:size(A, 1), :);
    
    % Compute the least-norm solution using the QR factors
    x0 = Q * (R'\b);
end

%create Vandermonde matrix X from data-points x_i
function X = vandermonde(x,d)
    %x = m x 1 vector of inputs x_i
    %d = polynomial degree
    X = [];
    for k=0:d
        X(:,end+1) = x.^k;
    end
end