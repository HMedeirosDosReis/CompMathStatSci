%note: the file mystery_function.p needs to be in the 
%current folder for this script to work.
[f,grad] = mystery_function; %load mystery function and gradient
x = zeros(500,1); %fixed initialization

% define algorithm parameters here
s = 4;
alpha = 0.25;
beta = 0.552;
cost = f(x); %initialize cost array


for k=1:30
    g = grad(x);
    d = - g;
    t=1/4;
    x = x+t*d;
    cost = [cost,f(x)];
end
for k=31:1000
    g = grad(x);
    %your algorithm goes here
    if norm (g) < 1e-16
        break ;
    end
    d = - g; % steepest descent
    t = s;
    while (f(x) - f(x+t*d) < -alpha*t*g'*g)
        t = beta*t;
    end
    x = x+t*d;
    
    cost = [cost,f(x)];
end
fprintf('f(x) = %8.6f\n',f(x));
fprintf('number of gradient calls = %d\n',grad('count'));

figure(1); %plot the cost 
semilogy(cost,'linewidth',2);
title('cost vs. iteration');
set(gca,'fontsize',14);