%%Shooting Method for Nonlinear BVP ODEs
clear all; close all
global y0 yL L Tair w
y0 = 0; yL = 10; L = 2; Tair = 5; w = 4;
%%
a = 1;
s = F(a);

b = 20;
line_t = F(b);


ydotopt = ((b-a)/(line_t-s))*(y0-s)+a;
%%
%Solve the IVP using ydotopt
ydot = @(t,y) [y(2);-w*(Tair - y(1))];      %Set up the system of ODEs
tspan = [0 L]; ICs = [y0 ydotopt];          %Set the BCs
[t,y] = ode45(ydot, tspan, ICs);            %Solve the IVP
plot(t,y(:,1))
xlabel('x'); ylabel('y');title('Solution of BVP')

%% Residual function. fzero finds root of fn R
function R = F(s)
global y0 yL L Tair w%%
%y0 = 0; yL = 10; L = 2; Tair = 5; w = 4; 
ydot = @(t,y) [y(2);-w*(Tair - y(1))]; %Define the system of ODEs
tspan = [0 L]; ICs = [y0 s];           %Set the BCs
[t,y] = ode45(ydot, tspan, ICs);       %Solve the system
R = y(end,1) - yL;                     %Compute and return the difference between the predicted and actual BC
end