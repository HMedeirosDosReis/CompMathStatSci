%% RK45 ODE solver
clear all; close all;
global a_damp a_spring a_drag g L mass
tspan = [0 100];
%parameters
a_damp = 8; a_spring=40; a_drag = 0.25; g = 9.81; L = 30;
mass = 34.0194;init_height = 62;
xinit =0; yinit = 0;
ICs = [xinit yinit]; 
%% RK
[t,y] = ode45(@(t,y) bungee(t,y),tspan,ICs);

%% Graph
plot(t,-y(:,1)+init_height)
hold on
%%
function dydt = bungee(t,y)
global a_damp a_spring a_drag g L mass
q = y(2);
if y(1) > L      %Cord exerts force
    F_cord = a_spring*(y(1) - L) + a_damp*y(2);
else
    F_cord = 0;
end
    
TotalForce = g - sign(y(2))*a_drag*y(2)^2/mass - F_cord/mass;
r = TotalForce;
dydt = [q;r];
end