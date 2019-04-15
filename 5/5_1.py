inventory = {
    "零钱":500,
    "小口袋":["小刀","绳子","手套"],
    "大口袋":["帐篷","水杯","睡袋","毛巾"]
}

inventory["零食"]=["苹果","面包","牛奶"]
print(inventory)
inventory["大口袋"].sort()
# inventory["大口袋"].remove("毛巾")

del inventory["大口袋"][3]
inventory["零钱"]=inventory["零钱"]+50
print(inventory)
