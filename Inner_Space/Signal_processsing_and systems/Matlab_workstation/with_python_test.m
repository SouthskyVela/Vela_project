py.importlib.import_module('numpy')
py.importlib.import_module('my_functions')
%py.importlib.reload(obj);
py.my_functions.hello_world()
%[result_array, mean_value]=py.my_functions.generate_random_array(10)
% 设置路径
%addpath('F:\Host_notes\Signal processing and systems\Python_processing\matlab_workstation\my_functions.py'); % 替换为你的Python函数文件
% py.importlib.import_module('my_functions');
% 
% 调用Python函数
% size = 10; % 随机数组大小
% [result_array, mean_value] = py.my_functions.generate_random_array(size);
% 
% 显示结果
% disp(['随机数组: ', num2str(result_array)]);
% disp(['均值: ', num2str(mean_value)]);
