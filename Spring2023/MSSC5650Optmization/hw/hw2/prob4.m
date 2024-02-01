%% 
rng(1); %fix random seed -- must include this!
x = randn(5,1);
A = randn(5,5);
%% a
disp(x(2));
% output: 1.1812
%% b
disp(A(1,4));
% output: -0.2752
%% c
disp(A(:,1:2));
% output:
%   -0.5727   -0.8519
%   -0.5587    0.8003
%    0.1784   -1.5094
%   -0.1969    0.8759
%    0.5864   -0.2428
%% d
disp(norm(x-A*x));
% output: 3.9050
%% e 
[V,D] = eig(A);
disp(max(diag(D)));
% output: 3.8004
% the actual maximum eigenvalue is -3.8004, but we are using the absolute
% value