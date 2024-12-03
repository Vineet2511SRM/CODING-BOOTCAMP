''' Mahesh is a farmer and owns 80 acres of land. His land is equally divided into 5 segments. 
He grows tomatoes in the 1st segment, potatoes in the 2nd segment, cabbage in the 3rd segment, 
sunflower in the 4th segment and sugarcane in the 5th segment. He is converting his land from 
chemical-driven farming to chemical-free farming. Mahesh starts with the conversion of vegetables 
into chemical-free produce. He spends the first 6 months doing the same. He then converts the 
sunflower land bank into chemical-free farming. This takes him another 4 months. Finally, he 
converts sugarcane into chemical-free farming over the next 4 months. He gets a yield of the 
following for tomatoes. 30% of his tomato land gives him 10 tonne yield per acre. The remaining 
70% of his tomato land gives him 12 tonnes yield per acre. The selling price of tomato is Rs. 7 
per Kg. The yield of potatoes is 10 tonnes per acre. He sells each kg at Rs. 20. The yield of 
cabbage is 14 tonnes per acre. He sells each kg at Rs. 24. The yield of sunflowers is 0.7 tonnes
 per acre. He sells each kg at Rs. 200. The yield of sugarcane is 45 tonnes per acre. He sells 
each tonne at Rs. 4,000. All the crops are sowed at the same time. Mahesh gets the above yield 
at the above-mentioned rate in one crop cycle across his entire land of 80 acres. What is 
a. The overall sales achieved by Mahesh from the 80 acres of land. 
b. Sales realisation from chemical-free farming at the end of 11 months '''

tomato_yield=((30/100)*16*10) + ((70/100)*16*12)
tomato_price=(7*1000)*tomato_yield

potato_yield=10*16
potato_price=(20*1000)*potato_yield

cabbage_yield=14*16
cabbage_price=(24*1000)*cabbage_yield

sunflower_yield=(0.7)*16
sunflower_price=(200*1000)*sunflower_yield

sugarcane_yield=45*16
sugarcane_price=4000*sugarcane_yield

print("Total sales of tomato:",tomato_price)
print("Total sales of potato:",potato_price)
print("Total sales of cabbage:",cabbage_price)
print("Total sales of sunflower:",sunflower_price)
print("Total sales of sugarcane:",sugarcane_price)

print("Total sales:",tomato_price+potato_price+cabbage_price+sunflower_price+sugarcane_price)