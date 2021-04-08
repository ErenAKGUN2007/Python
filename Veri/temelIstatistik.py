#%%
import pandas as pd
sozluk={"isim":["Eren","Reyyan","Mert","Atakan","Serkan"],
        "yas": [13    ,13      ,12    ,15      ,39      ],
        "boy": [1.56  ,1.58    ,1.65  ,1.76    ,1.74    ],
        "kilo":[50    ,45      ,53    ,60      ,78      ]
        }
veri=pd.DataFrame(sozluk)
veri
#%%
veri.head(3)
#%%
veri.tail(2)
#%%
veri.columns
#%%
veri.info
#%%
veri=pd.read_csv("kalp_rahatsizligi.csv")
veri.head
#%%
print(veri.columns)
#%%
veri.info
#%%
veri.describe
#%%
veri["serum_kolestrol"]
#%%
veri[veri.yas>50]
veri[veri["yas"]>50]
#%%
veri[(veri.yas>50)&(veri.cinsiyet=="kadin")]
#%%
veri[veri.hareketsiz_kan_basinci>120]
#%%
ort=veri["serum_kolestrol"].mean()
std=veri["serum_kolestrol"].std()
print("serum k ort:",ort)
print("serum k std:",std)
#%%
kadinveri=veri[(veri.cinsiyet=="kadin")&(veri.yas>50)]
kadinveri["serum_kolestrol"].mean()