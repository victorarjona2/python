# -*- coding: utf-8 -*-
"""
@author: Victor Arjona
DESCRIPTION:
    THIS SCRIPT IS TO FULFILL THE PREREQUISITES FOR THE ID ANALYTICS INTERVIEW.
    WE'LL BE INGESTING A CSV FILE THAT CAME FROM AN EXCEL FILE.
    THERE ARE 9 COLUMNS IN TOTAL. THE ORIGINAL HEADINGS WILL BE CHANGED BY THE
    OPTIONS ON THE RIGHT FOR EASIER ACCESS.
    Application ID      -   id
    Application Date    -   date
    Channel             -   chnl
    Ammount Requested   -   amt_req
    Risk Class          -   risk
    Decision            -   dec
    Decision Code       -   dec_code
    Outcome             -   out
    Revenue/ (Loss)     -   rev_loss
                                TABLE OF CONTENTS
    1. General information
        1.1 What columns do we have and what do they represent?
        1.2 What are the contents of each of these columns?
        1.3 What’s the frequency of applications throughout the month in total?
        1.4 What time span are we in here?
        1.5 What are some stats on the amounts requested?
        1.6 What’s the count for online/store channels? Percentage?
        1.7 How much revenue did we get?
        1.8 how much loss did we get?
        1.9 What are the counts for each decision code? Percentage?
        1.10 What are the counts for each decision? Percentage?
    2. Specific questions provided by email
        Definitions:
                bad rate :  the rate of accounts that we had a loss from the
                            accounts that were approved.
                approval :  the rate of accounts approved for a loan.
                rate
        2.1 What is the bad rate, approval rate, and average loan amount by
            channel?
        2.2 What is the bad rate, approval rate, and average loan amount by
            risk?
        2.3 What do you think the different risk (N, J, B) likely represent?
    3. Further analysis
        3.1
        3.2
        3.3
"""

# IMPORTS
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# READ CSV FILE WITH PANDAS. HEADERS WILL BE AUTOMATICALLY CONSIDERED.
file_path = r"C:\Users\vargo\codebase\python\data\fake-data.csv"
data = pd.read_csv(file_path)

# CLEAN DATA: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#       1) RENAME HEADERS. ----------------------------------------------------
nu_hdrs_lst = ['id', 'date', 'chnl',
               'amt_req', 'risk', 'dec',
               'dec_code', 'out', 'rev_loss']
curr_hdrs = data.columns
nu_hdrs_dict = {}

for idx, hdr in enumerate(curr_hdrs):
    nu_hdrs_dict[hdr] = nu_hdrs_lst[idx]

data.rename(columns=nu_hdrs_dict, inplace=True)     
# -----------------------------------------------------------------------------
#       2) TURN 'Application Date', NOW 'date', INTO A TIMESTAMP. -------------
data.loc[:, 'date'] = pd.to_datetime(data.date)
# -----------------------------------------------------------------------------
#       3) TURN 'Amount Requested', NOW 'amt_req', INTO A FLOAT. --------------
data.loc[:, 'amt_req'] = [float(amt.strip(' $')) for amt in data.amt_req]
# -----------------------------------------------------------------------------
#       4) TURN 'Decision', NOW 'dec', INTO 'True'/'False', WHERE 'True' IS ---
#           FOR 'Approve' AND 'False' FOR THE 'Decline'
# data.loc[:, 'dec'] = [dec == 'Approve' for dec in data.dec]
# -----------------------------------------------------------------------------
#       5) TURN THE VALUES IN THE 'Outcome' COLUMN, NOW 'out', TO 'good', -----
#           'bad', AND 'N/A'.
strt_out = list(set(data.out))
end_out = [np.nan, 'good', 'bad']
out_map = {}

for idx, out in enumerate(strt_out):
    out_map[out] = end_out[idx]

data.loc[:, 'out'] = [out_map[out] for out in data.out]
# -----------------------------------------------------------------------------
#       6) TURN 'rev_loss' TO A FLOAT. IF IT HAS A PARENTHESES THEN IT IS -----
#           NEGATIVE!


def Rev_Loss(rl):
    if rl == '-   ':
        return 0
    if '(' in rl:
        return (-1)*float(rl[1:-1])
    return float(rl)


data.loc[:, 'rev_loss'] = [Rev_Loss(rl.split(' $')[1]) for rl in data.rev_loss]
# -----------------------------------------------------------------------------

# CLEAN DATA: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# CONTENT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   1 GENERAL INFORMATION +++++++++++++++++++++++++++++++++++++++++++++++++++++
#       1.1 WHAT COLUMNS DO WE HAVE AND WHAT DO THEY REPRESENT?
#       1.2 WHAT ARE THE CONTENTS OF EACH OF THESE COLUMNS?
print("1.1 and 1.2", "\n")
print(data.dtypes, "\n")

#       1.3 WHAT'S THE FREQUENCY OF APPLICATIONS IN THE MONTH? ----------------
t = np.linspace(1, 30, 30)

all_h = {}
five_h = {}
three_h = {}
two_h = {}

for tt in t:
    all_h[tt] = 0
    five_h[tt] = 0
    three_h[tt] = 0
    two_h[tt] = 0

f_hold = data.loc[data.amt_req == 500, "date"]

for ff in f_hold:
    if ff.day in five_h:
        five_h[ff.day] += 1
        all_h[ff.day] += 1

th_hold = data.loc[data.amt_req == 300, "date"]

for th in th_hold:
    if th.day in three_h:
        three_h[th.day] += 1
        all_h[th.day] += 1

tw_hold = data.loc[data.amt_req == 200, "date"]

for tw in tw_hold:
    if tw.day in two_h:
        two_h[tw.day] += 1
        all_h[tw.day] += 1

lbl = ["Total", "Five hundred", "Three hundred", "Two hundred"]

fig = plt.figure()
plt.plot(all_h.keys(), all_h.values())
plt.plot(five_h.keys(), five_h.values())
plt.plot(three_h.keys(), three_h.values())
plt.plot(two_h.keys(), two_h.values())
plt.grid()
plt.legend(lbl)
plt.title("Frequency of applications in the month")
plt.xlabel("Day of the month (December)")
plt.ylabel("Frequency")
#fig.savefig('Frequency of Applications.png')

#       1.4 WHAT TIME SPAN ARE WE IN HERE!? -----------------------------------
max_date = max(data.date)
min_date = min(data.date)
gi_1_1 = max_date - min_date
gi_1_1_ans = "The starting date is {} {} of {}, {}. "
gi_1_1_ans = gi_1_1_ans.format(min_date.day_name(),
                               min_date.day,
                               min_date.month_name(),
                               min_date.year)
gi_1_1_ans += "The last date is {} {} of {}, {}. "
gi_1_1_ans = gi_1_1_ans.format(max_date.day_name(),
                               max_date.day,
                               max_date.month_name(),
                               max_date.year)
gi_1_1_ans = gi_1_1_ans + "Total span of time: {}".format(gi_1_1)
print(gi_1_1_ans, '\n')

# -----------------------------------------------------------------------------
#       1.5 WHAT'RE SOME STATS ON THE AMOUNTS REQUESTED? ----------------------
amt_ord_dict = dict(data.amt_req.value_counts())
amt_ord_vals = list(amt_ord_dict.values())
for key, val in amt_ord_dict.items():
    amt_ord_dict[str(key)] = amt_ord_dict.pop(key)

amt_ord_keys = list(amt_ord_dict.keys())

aiybq2_ans = "There were three amounts requested: ${}, ${}, and ${}. \n"
aiybq2_ans = aiybq2_ans.format(amt_ord_keys[0], amt_ord_keys[1],
                               amt_ord_keys[2])

la_somme = sum(amt_ord_vals)

for key, val in amt_ord_dict.items():
    aiybq2_ans += "{} had %{} of the requests made this month.\n"
    aiybq2_ans = aiybq2_ans.format(key, round(100*val/la_somme, 2))

print(aiybq2_ans)

lbl = ['%' + str(round(100*val/la_somme, 2)) for val in amt_ord_dict.values()]

fig = plt.figure()
big_p = []
for idx, key in enumerate(amt_ord_keys):
    big_p.append(plt.bar(key, amt_ord_vals[idx]))

plt.grid()
plt.legend(tuple(big_p), tuple(lbl))
plt.title('Frequency per Amount')
plt.xlabel('Amount requested')
plt.ylabel('Frequency')
plt.show()
#fig.savefig('Frequency per Amount.png')
print()
# -----------------------------------------------------------------------------
#       1.6 WHAT'S THE COUNT FOR ONLINE/STORE CHANNELS? PERCENTAGE? -----------
onl_str_dict = dict(data.chnl.value_counts())
onl_str_vals = list(onl_str_dict.values())
onl_str_keys = list(onl_str_dict.keys())

aiybq3_ans = "There were 2 channels: {}, and {}. \n"
aiybq3_ans = aiybq3_ans.format(onl_str_keys[0], onl_str_keys[1])

la_somme = sum(onl_str_vals)

for key, val in onl_str_dict.items():
    aiybq3_ans += "{} had %{} of the requests made this month.\n"
    aiybq3_ans = aiybq3_ans.format(key, round(100*val/la_somme, 2))

print(aiybq3_ans)

lbl = [key for key, val in onl_str_dict.items()]

fig = plt.figure()
big_p = []
for idx, key in enumerate(onl_str_keys):
    big_p.append(plt.bar(key, onl_str_vals[idx]))

plt.grid()
plt.legend(tuple(big_p), tuple(lbl))
plt.title('Frequency per Channel')
plt.xlabel('Channel')
plt.ylabel('Frequency')
plt.show()
#fig.savefig('Frequency per Channel.png')
print()
# -----------------------------------------------------------------------------
#       1.7 HOW MUCH REVENUE DID WE GET? --------------------------------------
tot_rev = round(sum([s for s in data.rev_loss if s >= 0]), 2)
aiybq4_ans = "There was a total of ${} in revenue.".format(tot_rev)
print(aiybq4_ans, '\n')
# -----------------------------------------------------------------------------
#       1.8 HOW MUCH LOSS DID WE GET? -----------------------------------------
tot_loss = round(-1*sum([s for s in data.rev_loss if s <= 0]), 2)
aiybq5_ans = "There was a total of ${} in loss.".format(tot_loss)
print(aiybq5_ans, '\n')
# -----------------------------------------------------------------------------
#       1.9 WHAT'RE THE COUNTS FOR EACH DECISION CODE? PERCENTAGE? -----------
dec_code_dict = dict(data.dec_code.value_counts())
dec_code_vals = list(dec_code_dict.values())
dec_code_keys = list(dec_code_dict.keys())

aiybq6_ans = "There were 3 decision codes: {}, {}, and {}. \n"
aiybq6_ans = aiybq6_ans.format(dec_code_keys[0], dec_code_keys[1],
                               dec_code_keys[2])

la_somme = sum(dec_code_vals)

for key, val in dec_code_dict.items():
    aiybq6_ans += "{} had %{} of the requests made this month.\n"
    aiybq6_ans = aiybq6_ans.format(key, round(100*val/la_somme, 2))

print(aiybq6_ans)

lbl = [key for key, val in dec_code_dict.items()]

fig = plt.figure()
big_p = []
for idx, key in enumerate(dec_code_keys):
    big_p.append(plt.bar(key, dec_code_vals[idx]))

plt.grid()
plt.legend(tuple(big_p), tuple(lbl))
plt.title('Frequency per Decision Code')
plt.xlabel('Decision Code')
plt.ylabel('Frequency')
plt.show()
#fig.savefig('Frequency per Decision Code.png')
print()
# -----------------------------------------------------------------------------
#       1.10 WHAT'RE THE COUNTS FOR EACH DECISION? PERCENTAGE? -------------
dec_dict = dict(data.dec.value_counts())
dec_vals = list(dec_dict.values())
dec_keys = list(dec_dict.keys())

aiybq7_ans = "There were 2 different decisions: {}, and {}. \n"
aiybq7_ans = aiybq7_ans.format(dec_keys[0], dec_keys[1])

la_somme = sum(dec_code_vals)

for key, val in dec_dict.items():
    aiybq7_ans += "{} had %{} of the requests made this month.\n"
    aiybq7_ans = aiybq7_ans.format(key, round(100*val/la_somme, 2))

print(aiybq7_ans)

lbl = [key for key, val in dec_dict.items()]

fig = plt.figure()
big_p = []
for idx, key in enumerate(dec_keys):
    big_p.append(plt.bar(key, dec_vals[idx]))

plt.grid()
plt.legend(tuple(big_p), tuple(lbl))
plt.title('Frequency per Decision')
plt.xlabel('Decision')
plt.ylabel('Frequency')
plt.show()
#fig.savefig('Frequency per Decision.png')
print()
#   1 GENERAL INFORMATION +++++++++++++++++++++++++++++++++++++++++++++++++++++

#   2 SPECIFIC QUESTIONS PROVIDED BY EMAIL ++++++++++++++++++++++++++++++++++++
#       2.1 WHAT IS THE BAD RATE, APPROVAL RATE, AND AVERAGE LOAN AMOUNT BY ---
#           CHANNEL?
#
#           DEFINITIONS:
#               bad rate :  the rate of accounts that we had a loss from the
#                           accounts that were approved.
#               approval :  the rate of accounts approved for a loan.
#                   rate

# ONLINE AND STORE POPULATION DATAFRAME.
onl_pop = data.loc[data.chnl == "Online", :]
str_pop = data.loc[data.chnl == "Store", :]

len_onl_pop = len(onl_pop)
len_str_pop = len(str_pop)

ans2_1_onl = "The total amount of online applications is {}. That's {}% total."
print(ans2_1_onl.format(len_onl_pop,
                        100*round(1.0*onl_str_dict["Online"]/len(data), 2)
                        ), "\n")

ans2_1_str = "The total amount of store applications is {}. That's {}% total."
print(ans2_1_str.format(len_str_pop,
                        100*round(1.0*onl_str_dict["Store"]/len(data), 2)
                        ), "\n")


ans2_1_bad_onl = "The percentage of online bad rates is {}% of all "
ans2_1_bad_onl += "applications but {}% of all online applications."




#apprvd_onl_lst = data.loc[(data.dec == "Approve") & (data.chnl == "Online"),
#                          "rev_loss"]
#apprvd_str_lst = data.loc[(data.dec == "Approve") & (data.chnl == "Store"),
#                          "rev_loss"]
#neg_cnt_onl = 0
#neg_cnt_str = 0
#
#len_apprvd_onl = len(apprvd_onl_lst)
#len_apprvd_str = len(apprvd_str_lst)
#
#for el in apprvd_onl_lst:
#    if el < 0:
#        neg_cnt_onl += 1
#
#for el in apprvd_str_lst:
#    if el < 0:
#        neg_cnt_str += 1
#
#ans2_1 = "The total amount of approved {} applications was {}. "
#ans2_1 += "There were a total of {} bad approved online applications. "
#ans2_1 += "For the entire month's approved applications, {}% were online. "
#ans2_1 += "{}% of the online approved applications were bad."
#
#ans2_1 = ans2_1.format("online", len_apprvd_onl, neg_cnt_onl, 
#                       )
# ans2_1
#
# apprvd_cnt_december = len(data.loc[data.dec == "Approve"])
# ans = "There were a total of {} approved loans for the month of December. "
# ans += "Out of those, there were {} that were considered bad. "
# ans += "Therefore, the rate of bad loans was {}."s
# ans = ans.format(apprvd_cnt_december, neg_cnt_onl, neg_cnt_onl/apprvd_chnl_len)
# print(ans, "\n")

# -----------------------------------------------------------------------------
#       2.2 BY RISK LEVEL? ----------------------------------------------------

# -----------------------------------------------------------------------------
#       2.3 WHAT DO YOU THINK THE DIFFERENT RISK (N, J, B) LIKELY REPRESENT? --
ans3_1 = "According to the decline/approve rates for each risk code, "
ans3_1 += "I'd say that J represents a low risk, N medium, and B high."
print(ans3_1, '\n')
# -----------------------------------------------------------------------------
#   2 SPECIFIC QUESTIONS PROVIDED BY EMAIL ++++++++++++++++++++++++++++++++++++

#   3 FURTHER ANALYSIS ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#       3.1
#       3.1

#       3.2
#       3.2

#       3.3
#       3.3
#   3 FURTHER ANALYSIS ++++++++++++++++++++++++++++++++++++++++++++++++++++++++