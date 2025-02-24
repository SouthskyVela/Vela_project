import grey_code_create #导入格雷码转换模块
def create_bin():
    gery_dimensionality=5  
    #格雷码列方向上的维数(位数)
    count=pow(2,gery_dimensionality)
    #生成五位二进制码即为生成前pow(2,5)个十进制数(五位二进制数就这么多)
    gery_matrix=grey_code_create.grey_create(gery_dimensionality)
    #调用格雷码高维数组生成函数
    #global bin_num  
    bin_num=[]
    
    with open("out_put.txt","w") as file: 
        for i in range(count):
            bin_num.append(format(i,'05b')) 
            #'05b'即将目标数格式化为五位二进制数
            print("十进制数:{}-->二进制数:{}-->格雷码:{}".format(i,bin_num[i],gery_matrix[i]))

            line_result="十进制数:{}-->二进制数:{}-->格雷码:{}".format(i,bin_num[i],gery_matrix[i])
            file.write(line_result+"\n")

create_bin()