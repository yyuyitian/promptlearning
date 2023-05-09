from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    loan_amount = float(request.json['loan_amount'])
    annual_rate = float(request.json['annual_rate'])
    expire_date = request.json['expire_date']
    today_string = request.json['today_string']
    payment_day = int(request.json['payment_day'])
    
    print("loan_amount =", loan_amount)
    print("annual_rate =", annual_rate)
    print("expire_date =", expire_date)
    print("today_string =", today_string)
    print("payment_day =", payment_day)
    # 计算月利率
    monthly_rate = annual_rate / 12

    # 计算还款期限（总月数）和第一个还款日
    from datetime import datetime, timedelta
    from dateutil.relativedelta import relativedelta
    expire_date_obj = datetime.strptime(expire_date, '%Y-%m-%d')
    today_obj = datetime.strptime(today_string, '%Y-%m-%d')
    this_month = datetime(today_obj.year, today_obj.month, payment_day)
    first_payment_date = this_month if today_obj.day <= payment_day else this_month + timedelta(days=1)
    total_months = (expire_date_obj.year - first_payment_date.year) * 12 + (expire_date_obj.month - first_payment_date.month) + 1

    # 计算每个月应还的本金和利息
    repayment = []
    for month in range(1, total_months + 1):
        # 第n个月的还款日
        this_month = first_payment_date + relativedelta(months=month - 1)
        if this_month > expire_date_obj:
            this_month = expire_date_obj

        # 第 n 个月偿还的贷款利息
        month_loan_interest = loan_amount * monthly_rate

        # 第 n 个月偿还的贷款本金
        month_loan_principal = loan_amount / (total_months - month + 1)

        # 第 n 个月偿还总贷款金额
        month_repayment = month_loan_principal + month_loan_interest

        # 将结果加入列表
        repayment.append([month_loan_principal,
                        month_loan_interest, month_repayment, this_month])

        # 更新贷款余额
        loan_amount -= month_loan_principal
# 输出每个月需要还款的金额、本金和利息到文件
    import datetime

    total_loan_principal = 0
    total_loan_interest = 0
    total_loan = 0
    with open("repayment_plan.txt", "w", encoding="utf-8") as f:
        f.write("按月还款计划如下：\n")
        f.write("日期\t\t还款金额\t还款本金\t还款利息\n")
        for r in repayment:
            date_str = r[3].strftime("%Y-%m-%d")
            total_loan += r[2]
            total_loan_principal += r[0]
            total_loan_interest += r[1]
            f.write("{}\t{:.2f} 元\t{:.2f} 元\t{:.2f} 元\n".format(date_str, r[2], r[0], r[1]))
        f.write("总还款金额{:.2f} 元\t 总还款本金{:.2f} 元\t 总还款利息{:.2f} 元".format(total_loan, total_loan_principal, total_loan_interest))
    # 输出本月需要还款的金额、本金和利息
    this_month_repayment = [r for r in repayment if r[3].month == first_payment_date.month][0]
    print("本月需要还款的金额为：{:.2f} 元，其中本金为 {:.2f} 元，利息为 {:.2f} 元。".format(this_month_repayment[2], this_month_repayment[0], this_month_repayment[1]))

    print("begin return")

    return jsonify(repayment)


if __name__ == '__main__':
    app.run()
