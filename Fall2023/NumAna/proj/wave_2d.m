clear all; close all;

%vidObj = VideoWriter("wave_2d_absorb_not_middle.avi");
%open(vidObj)
%% Space
Lx = 10;
Ly = 10;
dx = 0.1;
dy = 0.1;
nx = Lx/dx;
ny = Ly/dy;
x = (0:Lx/dx-1)*dx;
y = (0:Ly/dy-1)*dy;
%% Time 
T = 20;

%% Grid

u = zeros(nx,ny);
u_prev = u;
u_next = u;

CFL = 0.5;
c=1;
dt = CFL*dx;
%% Initial condition
%u(30:32) = [0.1 0.2 0.1];
%u_next = u;
t = 0;
figure('units','pixels','position',[0 0 1440 1080])
while t<T
   % Reflect 
   %u(:,[1 end]) = 0;
   %u([1 end], :) = 0;
   % Absorb
   u_next(1,:) = u(2,:)+(CFL-1)/(CFL+1)*(u_next(2,:)-u(1,:));
   u_next(end, :) = u(end-1,:)+(CFL-1)/(CFL+1)*(u_next(end-1,:)-u(end,:));
   u_next(:,1) = u(:,2)+(CFL-1)/(CFL+1)*(u_next(:,2)-u(:,1));
   u_next(:,end) = u(:,end-1)+(CFL-1)/(CFL+1)*(u_next(:,end-1)-u(:,end));

   % Solve 
   t = t+dt;
   u_prev = u;
   u = u_next;

   % f
   u(end/2, end/2) = dt^2*100*sin(20*pi*t/20);

   % interior 
   for i = 2:nx-1 
       for j=2:ny-1
       u_next(i,j) = 2*u(i,j)-u_prev(i,j)...
           +CFL^2*(u(i+1,j)+u(i,j+1)-4*u(i,j)...
           +u(i-1,j)+u(i,j-1));
       end
   end
   clf;
%    subplot(2,1,1);
%    imagesc(x,y,u); colorbar; caxis([-0.02 0.02])
%    title(sprintf("t=%.2f",t))
%    subplot(2,1,2);
   
   mesh(x,y,u'); colorbar; caxis([-0.02 0.02])
   title(sprintf("t=%.2f",t))
   axis([0 Lx 0 Ly -0.5 0.5])
   shg;

   %currFrame = getframe;
   %writeVideo(vidObj, currFrame);
%    if (t - 0.5*T<0.1&& t>15)
%  pause(30)
%  end
end

%close(vidObj)



