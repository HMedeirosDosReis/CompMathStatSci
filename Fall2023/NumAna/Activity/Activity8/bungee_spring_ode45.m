%% RK45 ODE solver
clear all; close all;
global s r b 
tspan = [0 20];
%parameters
s = 10;r=28;b=8/3;
x_init = 5.00001;%-sqrt(b*(r-1));
y_init = 5.00001;%x_init;
z_init = 5.00001;%r-1;
vars = [x_init,y_init,z_init];
%% RK
options = odeset('RelTol',1e-8,'AbsTol',1e-8);
[t,Y] = ode45(@(t,y) lorenz(t,y),tspan,vars,options);
figure
plot(t,Y(:,1))
xlabel('t'); ylabel('x');
figure
plot(t,Y(:,2))
xlabel('t'); ylabel('y');
figure
plot(t,Y(:,3))
xlabel('t'); ylabel('z');
%% Graph
figure
plot3(Y(:,1),Y(:,2),Y(:,3))
%%
function ddt = lorenz(t,Y)
global s r b
    x = Y(1);
    y = Y(2);
    z = Y(3);
    dxdt = -s*x+s*y;
    dydt = -x*z+r*x-y;
    dzdy = x*y-b*z;
    ddt = [dxdt,;dydt;dzdy];
end