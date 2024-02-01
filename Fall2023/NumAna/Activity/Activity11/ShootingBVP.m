%%Shooting Method for Nonlinear BVP ODEs
clear all; close all
global y0 yL L Tair w
y0 = 0; yL = 10; L = 2; Tair = 5; w = 4;

%Before running, determine values of ydot that yield 
%one + and one - residual (R= pred y(L) - y(L)). These values are the
%endpoints of the search interval. 
%fzero will determine the root on that search interval
% u'_opt
ydotopt = fzero(@F, [10 15]) ;                %Value of y' that will hit the BC

%Solve the IVP using ydotopt
% u'
ydot = @(t,y) [y(2);-w*(Tair - y(1))];      %Set up the system of ODEs
tspan = [0 L]; ICs = [y0 ydotopt];          %Set the BCs
[t,y] = ode45(ydot, tspan, ICs);            %Solve the IVP
plot(t,y(:,1))
xlabel('x'); ylabel('y');title('Solution of BVP')
%%
F(15)
%%
%% Residual function. fzero finds root of fn R
function R = F(s)
global y0 yL L Tair w%%
%y0 = 0; yL = 10; L = 2; Tair = 5; w = 4; 
% THIS GIVES RESIDUAL WITH DIFFERENT S VALUES 
ydot = @(t,y) [y(2);-w*(Tair - y(1))]; %Define the system of ODEs
tspan = [0 L]; ICs = [y0 s];           %Set the BCs
[t,y] = ode45(ydot, tspan, ICs);       %Solve the system
R = y(end,1) - yL;                     %Compute and return the difference between the predicted and actual BC
end