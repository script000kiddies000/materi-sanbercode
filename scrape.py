#!/usr/bin/env python
# coding: utf-8

# In[3]:




import requests

cookies = {
    '_ga': 'GA1.2.1330348029.1633770677',
    '_fbp': 'fb.1.1633770678095.812012426',
    'passster': 'IMDLS',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Alt-Used': 'blog.sanbercode.com',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0',
    'TE': 'Trailers',
}

response = requests.get('https://blog.sanbercode.com/docs/kurikulum-python-data-science-lanjutan/materi-minggu-ke-1/materi_2/', headers=headers, cookies=cookies)



from bs4 import BeautifulSoup as bs

content = bs(response.text,'html.parser')

content_mentah = content.find('div',{'class':'entry-content'})


# In[4]:


import json


# In[10]:


print(content_mentah)


# In[ ]:




