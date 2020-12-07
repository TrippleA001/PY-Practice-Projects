reservoir_volume = 4.445e8
rainfall = 5e6
runoff = rainfall*0.1
rainfall = rainfall - runoff
reservoir_volume += rainfall
stormwater = reservoir_volume*0.05
reservoir_volume += stormwater
evaporation = reservoir_volume*0.05
reservoir_volume -= evaporation
piped_water = 2.5e5
reservoir_volume -= piped_water
print(reservoir_volume)