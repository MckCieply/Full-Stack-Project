/* 
Gotta create custom colors for car prices and mileage where:
Prices: <30k - dark green, 30-40k - light green, 40-50k - yellow, >50k red
Mileage <100k - dark green, 100-150k - light green, 150-200k yellow, >200k red
*/

var price = document.getElementsByClassName('price');
var mileage = document.getElementsByClassName('mileage');
for(var i = 0; i<price.length;i++){
    if (price[i].textContent < 30000){
        price[i].style.color = "#17bc17";
    }
    else if(price[i].textContent >= 30000 && price[i].textContent < 40000){
        price[i].style.color = "yellow";
    }
    else if(price[i].textContent >= 40000 && price[i].textContent < 50000){
        price[i].style.color = "orange";
    }
    else{
        price[i].style.color = '#fb4747'; 
    }
}

for(var i = 0; i<mileage.length;i++){
    if (mileage[i].textContent < 100000){
        mileage[i].style.color = "#17bc17";
    }
    else if(mileage[i].textContent >= 100000 && mileage[i].textContent < 150000){
        mileage[i].style.color = "yellow";
    }
    else if(mileage[i].textContent >= 150000 && mileage[i].textContent < 200000){
        mileage[i].style.color = "orange";
    }
    else{
        mileage[i].style.color = '#fb4747'; 
    }
}
