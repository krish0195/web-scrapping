#!/usr/bin/env python
# coding: utf-8

# In[7]:


get_ipython().system('pip install autoscraper')


# In[87]:


from autoscraper import AutoScraper


# In[88]:



amazon_url="https://www.amazon.in/s?k=iphones"

wanted_list=["₹53,999","Apple iPhone 12 (64GB) - Purple"]


# In[89]:


scraper=AutoScraper()
result=scraper.build(amazon_url,wanted_list)
print(result)


# In[90]:



scraper.get_result_similar(amazon_url,grouped=True)


# In[93]:


scraper.set_rule_aliases({'rule_f1yo':'Title','rule_tf68':'Price'})
scraper.keep_rules(['rule_f1yo','rule_tf68'])
scraper.save('amazon-search')


# In[95]:



results=scraper.get_result_similar('https://www.amazon.in/s?k=mi+phones&crid=3TQWER5OOXTEO',group_by_alias=True)


# In[96]:



results['Price']


# In[98]:


results['Title']


# In[ ]:





# In[ ]:





# In[ ]:




