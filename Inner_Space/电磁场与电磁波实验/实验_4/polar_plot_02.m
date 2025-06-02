% 创建一个新的图形窗口
figure;
ax = polaraxes('PolarAxes', gcf); % 创建极坐标轴
polarplot(ax, [], []); % 初始化极坐标图

% 设置角度范围（0° 到 360°）
theta = linspace(0, 2*pi, 361); % 0° 到 360°，步长 1°

% 设置径向网格线（半径刻度）
rlim([0, 1]); % 设置半径范围（可根据数据调整）
rticks([0, 0.25, 0.5, 0.75, 1]); % 设置径向刻度

% 设置角度网格线（0° 到 360°，每 30° 一条）
thetaticks(0:30:360); % 设置角度刻度
thetagrid('On'); % 显示角度网格线

% 数据（示例：上半平面 0° 到 180°）
angles_deg = [0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180]; % 角度（°）
power_readings = [-31.9, -32.6, -32.4, -32.9, -33.3, -34.2, -35.3, -36.1, -35.4, -34.5, -33.8, -33.3, -33.9]; % 功率读数（dBm）

% 转换为弧度
angles_rad = deg2rad(angles_deg);

% 绘制上半平面数据
polarplot(ax, angles_rad, power_readings, 'LineWidth', 2, 'Color', 'blue');

% 对称映射到下半平面（180° 到 360°）
angles_rad_lower = deg2rad(360 - angles_deg(2:end-1)); % 排除 0° 和 180° 避免重复
power_readings_lower = power_readings(2:end-1); % 对称映射功率读数
polarplot(ax, angles_rad_lower, power_readings_lower, 'LineWidth', 2, 'Color', 'blue');

% 设置标题和标签
title('极坐标网格图（0° 到 360°）');
rlabel('功率（dBm）');
thetaticklabel('0°', '30°', '60°', '90°', '120°', '150°', '180°', '210°', '240°', '270°', '300°', '330°', '360°');

% 显示网格
grid on;
axis equal;
