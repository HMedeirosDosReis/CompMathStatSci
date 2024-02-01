%% RK45 ODE solver
clear all; close all;
global a b m n 
tspan = [0 10];
a = 1; b=1; m = 2; n = 1;             %parameters
xinit = 0.5; yinit = 0.5;
ICs = [xinit yinit]; 
%% RK
[t,y] = ode45(@(t,y) predprey(t,y),tspan,ICs);

%% Graph
plot(y(:,1),y(:,2))
hold on
plot(y(1,1),y(1,2),'+')
xlabel('prey'); ylabel('predator');
plot(m/n,a/b,'*')
%%
function dydt = predprey(t,y)
global a b m n
q = a*y(1) - b*y(1)*y(2);
r = -m*y(2) + n*y(1)*y(2);
dydt = [q;r];
end
