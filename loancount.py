# 输入信息
remaining_loan_principal = 982680.12  # 贷款金额
annual_rate = 0.039  # 年利率
expire_date = "2047-12-02"  # 到期日期
today_string = "2023-05-07"  # 当前日期

# 计算月利率
monthly_rate = annual_rate / 12

# 计算还款期限（总月数）
from datetime import datetime
expire_date_obj = datetime.strptime(expire_date, '%Y-%m-%d')
today_obj = datetime.strptime(today_string, '%Y-%m-%d')
total_months = (expire_date_obj.year - today_obj.year) * 12 + (expire_date_obj.month - today_obj.month)

# 计算每个月应还的本金和利息
repayment = []
for month in range(1, total_months + 1):
    # 该月应还贷款本金
    month_loan_principal = remaining_loan_principal / total_months

    # 该月应还贷款利息
    month_loan_interest = remaining_loan_principal * monthly_rate * (1 - (month - 1) / total_months)

    # 该月应还总贷款金额
    month_repayment = month_loan_principal + month_loan_interest

    # 剩余贷款本金
    remaining_loan_principal -= month_repayment

    # 将结果加入列表
    repayment.append([month_loan_principal, month_loan_interest, month_repayment])
import datetime
with open("repayment_plan.txt", "w", encoding="utf-8") as f:
    f.write("按月还款计划如下：\n")
    f.write("日期\t\t还款金额\t还款本金\t还款利息\n")
    for i, r in enumerate(repayment):
        month = today_obj.month + i
        year = today_obj.year + (month - 1) // 12
        month = (month - 1) % 12 + 1
        date = datetime.date(year, month, 1) + datetime.timedelta(days=-1)
        date_str = date.strftime("%Y-%m-%d")
        f.write("{}\t{:.2f} 元\t{:.2f} 元\t{:.2f} 元\n".format(date_str, r[2], r[0], r[1]))
