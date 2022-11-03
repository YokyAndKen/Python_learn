print("1 * 1的结果是: %d" % (1 * 1))
print(f"1 * 1的结果是：{1 * 1}")
print("字符串在python中的类型是：%s" % type('字符串'))


# 字符串格式化练习
name = "transwarp"
stock_price = 80.22
stock_code = 600100
stock_price_daily_growth_factor = 1.2
growth_days = 10

print(f"公司： {name}, 股票代码：{stock_code}, 当前股价：{stock_price}"
      f"每日增长系数：{stock_price_daily_growth_factor}, 经过{growth_days}天的增长后，股价达到了：{stock_price * (stock_price_daily_growth_factor ** growth_days)}")

print("公司：%s, 股票代码：%s，当前股价：%s，每日增长系数：%s，经过%s天的增长后，股价达到了%.2f" % (name, stock_code, stock_price, stock_price_daily_growth_factor, growth_days, stock_price * (stock_price_daily_growth_factor ** growth_days)))