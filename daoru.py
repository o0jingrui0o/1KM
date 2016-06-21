import numpy as np
import pandas
import random
import matplotlib.pyplot as plt

Site_info=pandas.read_csv("e://1KM//1.csv")
Site_info.index=Site_info['Site_id']
# print(Site_info)

Spot_info=pandas.read_csv("e://1KM//2.csv")
Spot_info.index=Spot_info['Spot_id']
# print(Spot_info)

Shop_info=pandas.read_csv("e://1KM//3.csv")
Shop_info.index=Shop_info['Shop_id']
# print(Shop_info)

Order_site=pandas.read_csv("e://1KM//4.csv")
# print(Order_site)

Order_shop=pandas.read_csv("e://1KM//5.csv")
# print(Order_shop)


fig_1,ax=plt.subplots()
for id_unique in Order_site['Site_id'].unique():
    r=random.uniform(0,1)
    g=random.uniform(0,1)
    b=random.uniform(0,1)
    for index in Order_site.index:
        if Order_site.get_value(index,'Site_id')==id_unique:
            index_spot=Order_site.get_value(index,'Spot_id')
            ax = plt.plot(Spot_info.get_value(index_spot,'Lng'), Spot_info.get_value(index_spot,'Lat'), '.', color=(r,g,b))
ax=plt.plot(Shop_info['Lng'],Shop_info['Lat'],'*',color='black')
# ax=plt.plot(Site_info['Lng'],Site_info['Lat'],'o',color='b')

for id_unique in Order_shop['Shop_id'].unique():
    r=random.uniform(0,1)
    g=random.uniform(0,1)
    b=random.uniform(0,1)
    for index in Order_shop.index:
        if Order_shop.get_value(index,'Shop_id')==id_unique:
            index_spot=Order_shop.get_value(index,'Spot_id')
            ax = plt.plot([Spot_info.get_value(index_spot,'Lng'),Shop_info.get_value(id_unique,'Lng')], [Spot_info.get_value(index_spot,'Lat'),Shop_info.get_value(id_unique,'Lat')], color=(r,g,b))

plt.show(ax)