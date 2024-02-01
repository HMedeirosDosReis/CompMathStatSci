clear all; close all;

% vidObj = VideoWriter("wave_3d_reflect_not_middle.avi");
% open(vidObj)

%% Space
Lx = 10;
Ly = 10;
Lz = 10;
dx = 0.1;
dy = 0.1;
dz = 0.1;
nx = Lx/dx;
ny = Ly/dy;
nz = Lz/dz;
x = (0:Lx/dx-1)*dx;
y = (0:Ly/dy-1)*dy;
z = (0:Lz/dz-1)*dz;

%% Time 
T = 10;

%% Grid
u = zeros(nx, ny, nz);
u_prev = u;
u_next = u;

CFL = 0.5;
c = 1;
dt = CFL * dx;
%% Initial condition
t = 0;
figure('units','pixels','position',[0 0 1440 1080])

while t<T
    % Reflect
%     u(:, [1 end], :) = 0;
%     u([1 end], :, :) = 0;
%     u(:, :, [1 end]) = 0;
%     
%     u_next(:, [1 end], :) = 0;
%     u_next([1 end], :, :) = 0;
%     u_next(:, :, [1 end]) = 0;

   % Absorb
    u_next(1, :, :) = u(2, :, :) + (CFL-1)/(CFL+1)*(u_next(2, :, :) - u(1, :, :));
    u_next(end, :, :) = u(end-1, :, :) + (CFL-1)/(CFL+1)*(u_next(end-1, :, :) - u(end, :, :));
    u_next(:, 1, :) = u(:, 2, :) + (CFL-1)/(CFL+1)*(u_next(:, 2, :) - u(:, 1, :));
    u_next(:, end, :) = u(:, end-1, :) + (CFL-1)/(CFL+1)*(u_next(:, end-1, :) - u(:, end, :));
    u_next(:, :, 1) = u(:, :, 2) + (CFL-1)/(CFL+1)*(u_next(:, :, 2) - u(:, :, 1));
    u_next(:, :, end) = u(:, :, end-1) + (CFL-1)/(CFL+1)*(u_next(:, :, end-1) - u(:, :, end));

   % Solve 
   t = t + dt;
   u_prev = u;
   u = u_next;

   % f
   u(end/4, end/4, end/4) = dt^2 * 100 * sin(20 * pi * t / 20);

   % Interior 
   for i = 2:nx-1 
       for j = 2:ny-1
           for k = 2:nz-1
               u_next(i, j, k) = 2*u(i, j, k) - u_prev(i, j, k) + ...
                   CFL^2 * (u(i+1, j, k) + u(i, j+1, k) + u(i, j, k+1) - 6*u(i, j, k) + ...
                   u(i-1, j, k) + u(i, j-1, k) + u(i, j, k-1));
           end
       end
   end

   clf;
   % Visualize the isosurface plot
   isosurface(x, y, z, u, 0);
   colorbar; caxis([-0.02 0.02]);
   title(sprintf("t=%.2f", t));
   axis([0 Lx 0 Ly 0 Lz]);
   grid on;
   view(3);

%    currFrame = getframe;
%    writeVideo(vidObj, currFrame);
end

% close(vidObj);
