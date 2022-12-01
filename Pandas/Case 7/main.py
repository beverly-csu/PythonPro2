import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('investments_VC.csv')

data = '''0   permalink             39999 non-null  object
 1   name                  39998 non-null  object
 2   homepage_url          37185 non-null  object
 3   category_list         36775 non-null  object
 4    market               36770 non-null  object
 5    funding_total_usd    39999 non-null  object
 6   status                38927 non-null  object
 7   country_code          35815 non-null  object
 8   state_code            24600 non-null  object
 9   region                35815 non-null  object
 10  city                  35124 non-null  object
 11  funding_rounds        39999 non-null  int64
 12  founded_at            31192 non-null  object
 13  founded_month         31148 non-null  object
 14  founded_quarter       31148 non-null  object
 15  founded_year          31148 non-null  float64
 16  first_funding_at      39999 non-null  object
 17  last_funding_at       39999 non-null  object
 18  seed                  39999 non-null  int64
 19  venture               39999 non-null  int64
 20  equity_crowdfunding   39999 non-null  int64
 21  undisclosed           39999 non-null  int64
 22  convertible_note      39999 non-null  int64
 23  debt_financing        39999 non-null  int64
 24  angel                 39999 non-null  int64
 25  grant                 39999 non-null  int64
 26  private_equity        39999 non-null  int64
 27  post_ipo_equity       39999 non-null  int64
 28  post_ipo_debt         39999 non-null  int64
 29  secondary_market      39999 non-null  int64
 30  product_crowdfunding  39999 non-null  int64
 31  round_A               39999 non-null  int64
 32  round_B               39999 non-null  int64
 33  round_C               39999 non-null  int64
 34  round_D               39999 non-null  int64
 35  round_E               39999 non-null  int64
 36  round_F               39999 non-null  int64
 37  round_G               39999 non-null  int64
 38  round_H               39999 non-null  int64'''

#Гипотеза: если в стартап инвестировали больше 1М $ вероятность успешности стартапа выше.
def fix_funding_total_usd(funding_total_usd):
    funding_total_usd = funding_total_usd.replace(',','')
    funding_total_usd = funding_total_usd.replace('-','0')
    return int(funding_total_usd)

df['funding_total_usd'] = df['funding_total_usd'].apply(fix_funding_total_usd)

over_millon = df[df['funding_total_usd'] > 1000000]
success_over_million = over_millon[over_millon['status'] != 'closed']
procent_over_million = len(success_over_million) / len(over_millon) * 100
print(round(procent_over_million, 2))

less_millon = df[df['funding_total_usd'] < 1000000]
success_less_million = less_millon[less_millon['status'] != 'closed']
procent_less_million = len(success_less_million) / len(less_millon) * 100
print(round(procent_less_million, 2))

result = [round(procent_less_million, 2), round(procent_over_million, 2)]
titles = ['< 1М $', '> 1М $']
result_for_legend = [str(result[0]) + '%', str(result[1]) + '%']

plt.pie(result, labels=result_for_legend)
plt.show()