from django.db import models

class Vmms(models.Model):
    # 车型
    carModel = models.CharField('车型',max_length=255)
    # VIN码
    VIN = models.CharField("VIN码",max_length=17)
    #里程
    mileage = models.IntegerField("里程")
    #接样人
    recipient = models.CharField("接样人",max_length=5)
    # 接车时间
    sampleDate = models.DateTimeField("接车时间")
    # 还车时间
    returnDate = models.DateTimeField("还车时间")
    # 试验项目
    testProjects = (
        (0, "请选择试验类型"),
        (1,"排放油耗试验"),
        (2, "温度场试验"),
        (3, "冷却试验"),
        (4, "空调试验"),
    )
    testProject = models.IntegerField("试验类型",choices=testProjects,default=0)
    # 试验状态
    testState = models.IntegerField("试验状态")
    # 运输
    transports = (
        (0,"不可拖运"),
        (1, "可拖回")
    )
    transport = models.IntegerField("运输",choices=transports,default=0)
    #停放地
    parks = (
        (0, "试验室"),
        (1, "停车场"),
    )
    park = models.IntegerField("停放地",choices=parks,default=0)

    # 备注
    remarks = models.TextField("备注")




