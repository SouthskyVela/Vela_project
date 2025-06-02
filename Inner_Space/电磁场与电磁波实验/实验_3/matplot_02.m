clear; clc; close all;

% 设定参数
c = 3e8; % 光速 (m/s)
f = 1e9; % 频率 (Hz)
omega = 2 * pi * f; % 角频率 (rad/s)
lambda = c / f; % 波长 (m)
k1 = omega / c; % 波数 (rad/m)

% 介质参数
mu1 = 1.26e-6; % 介质1的磁导率
epsilon1 = 8.84e-12; % 介质1的介电常数
sigma1 = 3.77e+2; % 介质1的电导率

mu2 = 1.89e-6; % 介质2的磁导率
epsilon2 = 1.77e-11; % 介质2的介电常数
sigma2 = 3.26e+2; % 介质2的电导率

% 计算折射率
n1 = sqrt(mu1 * epsilon1);
n2 = sqrt(mu2 * epsilon2);

% 计算反射系数和透射系数
R = (n1 - n2)^2 / (n1 + n2)^2;
T = 1 - R;

% 入射波参数
E0 = 1; % 入射波电场幅度 (V/m)
z_interface = 0; % 界面位置 (m)

% 计算反射波和透射波参数
E0_reflected = -E0 * sqrt(R); % 反射波幅度
E0_transmitted = E0 * sqrt(T); % 透射波幅度

% 空间网格
z = linspace(-0.3, 0.3, 1000); % z轴坐标 (-0.3到0.3)
t = 0; % 时间 (s)

% 计算电场分布
E_incident = E0 * exp(-1i * k1 * z) * exp(1i * omega * t); % 入射波
E_reflected = E0_reflected * exp(1i * k1 * z) * exp(1i * omega * t); % 反射波
E_transmitted = E0_transmitted * exp(-1i * k1 * z) * exp(1i * omega * t); % 透射波

% 总电场分布
E_total = E_incident + E_reflected;
E_total(z > 0) = E_transmitted(z > 0); % 在 z > 0 时，总电场等于透射波

% 提取实部用于绘图
E_incident_real = real(E_incident);
E_reflected_real = real(E_reflected);
E_transmitted_real = real(E_transmitted);
E_total_real = real(E_total);

% 绘制电场分布
figure;
subplot(4,1,1);
plot(z, E_incident_real, 'b');
title('入射波电场分布');
xlabel('z (m)');
ylabel('E (V/m)');
grid on;

subplot(4,1,2);
plot(z, E_reflected_real, 'r');
title('反射波电场分布');
xlabel('z (m)');
ylabel('E (V/m)');
grid on;

subplot(4,1,3);
plot(z, E_transmitted_real, 'k');
title('透射波电场分布');
xlabel('z (m)');
ylabel('E (V/m)');
grid on;

subplot(4,1,4);
plot(z, E_total_real, 'g');
title('总电场分布');
xlabel('z (m)');
ylabel('E (V/m)');
grid on;

% 标记界面位置
line([z_interface, z_interface], ylim, 'Color', 'k', 'LineStyle', '--');
legend('界面位置 z=0');

% 动画显示
for t = 0:0.1e-9:200e-9
    E_incident = E0 * exp(-1i * k1 * z) * exp(1i * omega * t);
    E_reflected = E0_reflected * exp(1i * k1 * z) * exp(1i * omega * t);
    E_transmitted = E0_transmitted * exp(-1i * k1 * z) * exp(1i * omega * t);
    
    % 总电场分布
    E_total = E_incident + E_reflected;
    E_total(z > 0) = E_transmitted(z > 0); % 在 z > 0 时，总电场等于透射波
    

    E_incident_real = real(E_incident);
    E_reflected_real = real(E_reflected);
    E_transmitted_real = real(E_transmitted);
    E_total_real = real(E_total);
    
    % 限制在 z <= 0 的部分
    E_incident_real(z > 0) = 0;
    E_reflected_real(z > 0) = 0;
    E_transmitted_real(z<0) =0;
    
    subplot(4,1,1);
    plot(z, E_incident_real, 'b');
    title('入射波电场分布');
    xlabel('z (m)');
    ylabel('E (V/m)');
    grid on;
    ylim([-1.5 1.5]);
    
    subplot(4,1,2);
    plot(z, E_reflected_real, 'r');
    title('反射波电场分布');
    xlabel('z (m)');
    ylabel('E (V/m)');
    grid on;
    ylim([-1.5 1.5]);
    
    subplot(4,1,3);
    plot(z, E_transmitted_real, 'k');
    title('透射波电场分布');
    xlabel('z (m)');
    ylabel('E (V/m)');
    grid on;
    ylim([-1.5 1.5]);
    
    subplot(4,1,4);
    plot(z, E_total_real, 'm');
    title('总电场分布');
    xlabel('z (m)');
    ylabel('E (V/m)');
    grid on;
    ylim([-2.5 2.5]);
    
    line([z_interface, z_interface], ylim, 'Color', 'k', 'LineStyle', '--');
    legend('界面位置 z=0');
    
    drawnow;
    pause(0.01);
end
