% This program plots the phase portrait for a system of differential equations.
% Current use is for the Predator Model
clear all
close all

%%Input
a = 2; b=1; m = 0.5; n = 1;             %parameters

f = @(x,y) (a- b*y)*x;                 %Input RHS of DE
g = @(x,y) (-m + n*x)*y;                %Input RHS of DE

Tfinal = 40;                            %Time interval for solution
xinit = 1;                              %Initial value for x
yinit = 1;                              %Initial value for y
dt = 0.0001;                              %Deltat for solution

%% Solve using Euler's method
x(1) = xinit;                           %Initialize the x and y soln vector
y(1) = yinit;
Nfinal = round(Tfinal/dt);              %Calculate number of points for soln

for k= 1:Nfinal
    x(k+1) = x(k) + f(x(k),y(k))*dt;    %Euler formula for x and y
    y(k+1) = y(k) + g(x(k),y(k))*dt;
end

%% Output results
figure(1)                               %Plot the phase portrait
plot(x(1),y(1),'*k')                    %Plot the initial point
hold on
plot(x,y)                               %Plot the solns
xlabel('x'); ylabel('y')
title('Predator-Prey Phase Portrait')
plot(m/n,a/b,'+b')                      %Plot the equilibrium point

figure(2)                               %Plot solns as a fn of t
t = 0:dt:Tfinal;                        %Create a time vector
plot(t,x)
hold on
plot(t,y)
xlabel('Time t'), ylabel('Population Size')
legend('x = prey','y = predator')
title('Predator-Prey Solutions')



