def calculate_success_probability(deal_success, current_profit):
    success_count = sum([1 for x in deal_success if x > 0]) 
    total_count = len(deal_success) 
    success_probability = success_count / total_count 

    net_profit = sum(deal_success) + current_profit 
    initial_capital = 1000 
    roi = (net_profit / initial_capital) * 100 

    print("Вероятность успеха сделки:", success_probability)
    print("Чистый доход (убыток) инвестора:", net_profit)
    print("ROI:", "{:.2f}%".format(roi))

