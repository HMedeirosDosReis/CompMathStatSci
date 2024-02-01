%% RK for bungee jumper rope
clear all;
close all;
%%
m = 158.757;
c_drag = 0.25;
g = 9.81;

f = @(t,v) g-(c_drag./m).*v.^2;

tspan = [0 60]; %time interval
v0 = 0; % Initial velocity

%%RK
[t,v] = ode45(f,tspan,v0);

%%
plot(t,v)
xlabel('t')
ylabel('v')


%%
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
q = y(2);
if y(1) < L;
    Fcordm = 0;
else 
    Fcordm = k/m*sign(v)*(y-L)-gamma/m*v;%...
end
r = 1;%...-....-Fcordm 
dydt = [q;r];
end
