clear all;
close all;
%%
f = @(t,y) -21*y+exp(-t);

tspan = [0 2]; %time interval
v0 = 0; % Initial velocity

%%RK
[t,v] = ode23s(f,tspan,v0);

%%
xexact = 1/20*exp(-t)-1/20*exp(-21*t);
hold on 
plot(t,xexact)
plot(t,v)
xlabel('t')
ylabel('v')