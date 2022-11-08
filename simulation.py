def simulation(t, e):
    c1_h = 10
    c2_h = 15
    c3_h = 13
    days = 300

    optimum_happiness = c2_h*days

    #exlore only
    explore_expected_happiness = 100*c1_h+100*c2_h+100*c3_h
    explore_expected_regret = optimum_happiness-explore_expected_happiness

    #exploit only
    exploit_expected_happiness = c1_h + c2_h + c3_h + 297*c2_h
    exploit_expected_regret = optimum_happiness-exploit_expected_happiness

    #eGreedy
    percent = ((100-e)/100)
    smaller_percent = (1-percent)/3
    print(smaller_percent)
    eGreedy_expected_happiness = percent*days*c2_h + smaller_percent*days*c1_h + smaller_percent*days*c2_h + smaller_percent*days*c3_h
    eGreedy_expected_regret = optimum_happiness-eGreedy_expected_happiness

    #average total happiness and regret
    explore_total = 0
    exploit_total = 0
    eGreedy_total = 0
    for i in range(t):
        explore_total += exploreOnly()
        exploit_total += exploitOnly()
        eGreedy_total += eGreedy(e)

    average_explore = explore_total/t
    average_exploit = exploit_total/t
    average_eGreedy = eGreedy_total/t
    average_regret_explore = optimum_happiness-average_explore
    average_regret_exploit = optimum_happiness-average_exploit
    average_regret_eGreedy = optimum_happiness-average_eGreedy
    
    #prints everything
    print("Explore Only:")
    print('Expected Happiness: ' + explore_expected_happiness)
    print('Expected Regret: ' + explore_expected_regret)
    print('Average happiness for ' + t + ' trials: ' + average_explore)
    print('Average regret for ' + t + ' trials: ' + average_regret_explore)
    print("Explot Only:")
    print('Expected Happiness: ' + exploit_expected_happiness)
    print('Expected Regret: ' + exploit_expected_regret)
    print('Average happiness for ' + t + ' trials: ' + average_exploit)
    print('Average regret for ' + t + ' trials: ' + average_regret_exploit)
    print("eGreedy:")
    print('Expected Happiness: ' + eGreedy_expected_happiness)
    print('Expected Regret: ' + eGreedy_expected_regret)
    print('Average happiness for ' + t + ' trials: ' + average_eGreedy)
    print('Average regret for ' + t + ' trials: ' + average_regret_eGreedy)
