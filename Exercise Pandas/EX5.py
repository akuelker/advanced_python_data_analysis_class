
# coding: utf-8

# In[2]:

import numpy as np
import pandas as pd


# In[4]:

lemon = pd.read_csv('LemonadeStandWeekend.csv', index_col = ['Day', 'Time'])
lemon


# In[8]:

LemonadeDrop = lemon.dropna()
LemonadeDrop


# In[15]:

np.max(LemonadeDrop)
np.min(LemonadeDrop)
np.sum(LemonadeDrop)
np.mean(LemonadeDrop)


# In[16]:

LemonadeCleaned = lemon.fillna(0)
LemonadeCleaned


# In[17]:

np.max(LemonadeCleaned)
np.min(LemonadeCleaned)
np.sum(LemonadeCleaned)
np.mean(LemonadeCleaned)


# In[19]:

np.max(lemon('Donations))


# In[43]:

import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('LemonadeStandWeekend.csv')
data.columns = ('Day', 'Time', 'Kid', 'Sales', 'Donations', 'Lemonade By Cup', 'Cookies')
data=data.fillna({'Sales':0, 'Donations':0})
fig, ax=plt.subplots()
groups = data.groupby(['Kid']).plot(x ='Day', y='Sales', ax=ax,legend=True, label='Kid')
#data.plot(kind='line',x='Day', y='Time', color='purple', title = 'Lemonade Sold')
plt.show()


# In[64]:

data = pd.read_csv('LemonadeStandWeekend.csv')
data.columns = ('Day', 'Time', 'Kid', 'Sales', 'Donations', 'Lemonade By Cup', 'Cookies')
#fig, ax=plt.subplots()
figure_1 = plt.plot(x['Day'], data['Sales'])
#figure_1 = plt.plot(x ='Day', y='Sales',legend=True, label = 'Kid')
#figure_2 = plt.plot(data['Donations'], data['Time'])

plt.legend(loc='upper right')
plt.xlabel('data')
plt.ylabel('time')

plt.show()


# In[65]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn

get_ipython().magic('matplotlib inline')


# In[66]:

data = pd.read_csv('LemonadeStandWeekend.csv')
rep_plot = data.groupby('Kid').sum().plot(kind='bar')
rep_plot.set_xlabel('Kid')
rep_plot.set_ylabel('Sales')


# In[78]:

data['Total Units'] = data['Lemonade By Cup']+ data['Cookies']
data.groupby('Kid').sum().sort_values('Total Units', ascending=False).plot(kind='bar')


# In[72]:

data_day = data[['Day', 'Total Units']]
data_day.groupby('Day').sum().plot(kind='bar')


# In[83]:

group = data.groupby(['Day', 'Kid']).sum()
total_sales = group['Sales'].groupby(level=0, group_keys=False)

gtp = total_sales.nlargest(5)
ax = gtp.plot(kind='bar')

count = gtp.groupby('Day').count()
cs = np.cumsum(count)
for i in range(len(count)):
    title = count.index.values[i]
    ax.axvline(cs[i]-0.5, lw=0.8, color='k')
    ax.text(cs[i]-(count[i]+1)/2., 1.02, title, ha='center',
           transform=ax.get_xaxis_transform())
ax.set_xticklabels([l.get_text().split(', ')[1][:-1] for l in ax.get_xticklabels()])


# In[ ]:



