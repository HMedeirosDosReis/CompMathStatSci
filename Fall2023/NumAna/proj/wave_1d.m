clear all; close all;
%vidObj = VideoWriter("wave_1d_absorb.avi");
%open(vidObj)
%% Space
Lx = 10;
dx = 0.1;
nx = Lx/dx;
x = (0:Lx/dx-1)*dx;

%% Time 
T = 30;

%% Grid

u = zeros(nx,1);
u_prev = u;
u_next = u;

CFL = 1;
c=1;
dt = CFL*dx;
%% Initial condition
%u(30:32) = [0.1 0.2 0.1];
%u_next = u;
t = 0;
figure('units','pixels','position',[0 0 1440 1080])

while t<T
   % Reflect 
   u([1 end]) = 0;

   % Absorb
   %u_next(1) = u(2)+(CFL-1)/(CFL+1)*(u_next(2)-u(1));
   %u_next(end) = u(end-1)+(CFL-1)/(CFL+1)*(u_next(end-1)-u(end));

   % Solve 
   t = t+dt;
   u_prev = u;
   u = u_next;

   % f
   u(end/2) = dt^2*10*sin(20*pi*t/T);

   % interior 
   for i = 2:nx-1
       u_next(i) = 2*u(i)-u_prev(i)+CFL^2*(u(i+1)-2*u(i)+u(i-1));
   end
   clf;
   plot(x,u)
   title(sprintf("t=%.2f",t))
   axis([0 Lx -0.5 0.5])
   shg;
%    currFrame = getframe;
%    writeVideo(vidObj, currFrame);
%  if (t - 0.5*T<0.1&& t>15)
%  pause(30)
%  end
end


%close(vidObj)

