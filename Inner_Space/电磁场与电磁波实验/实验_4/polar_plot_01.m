% 定义角度范围
theta = 0:15:360;

% 定义半径范围
rho = 0:30:360;

% 创建极坐标网格
[Theta, Rho] = meshgrid(theta, rho);

% 绘制极坐标网格图
polarplot(Theta(1,:), Rho(:,1), 'k'); % 绘制径向线
hold on;
polarplot(Theta(1,:), Rho(1,:), 'k'); % 绘制极向线
hold off;

% 设置极坐标轴的属性
ax = gca;
ax.ThetaTick = 0:15:360; % 设置角度刻度
ax.RhoTick = 0:30:360; % 设置半径刻度
ax.ThetaTickLabel = {'0°', '15°', '30°', '45°', '60°', '75°', '90°', ...
                     '105°', '120°', '135°', '150°', '165°', '180°', ...
                     '195°', '210°', '225°', '240°', '255°', '270°', ...
                     '285°', '300°', '315°', '330°', '345°'};
ax.RhoTickLabel = {'0', '30', '60', '90', '120', '150', '180', '210', '240', '270', '300', '330', '360'};

% 设置极坐标轴的标题
title('极坐标网格图');

% 显示网格
grid on;
