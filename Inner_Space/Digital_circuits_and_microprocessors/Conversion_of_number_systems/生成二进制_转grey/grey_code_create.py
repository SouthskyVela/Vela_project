def grey_create(n):
    gery_code=["0","1"]
    for i in range(2,n+1):
        # for code in gery_code:
        #     gery_plus0=["0"+code]
        # for code in reversed(gery_code):
        #     gery_plus1=["1"+code]
        gery_plus0=["0"+ code for code in gery_code]
        gery_plus1=["1"+ code for code in reversed(gery_code)]
        gery_code=gery_plus0+gery_plus1
        #print(gery_code)
    return gery_code
# gery_test=grey_create(5)
# #print(gery_test[0])
# for line_gery in gery_test:
#      print(line_gery)