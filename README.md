Array formatting library

`arrays.to_str(array, spacing=0)` returns 2D array as a string. Spacing is set to 0 by default but can be changed

`arrays.to_str3D(array, spacing)` returns 3D array as a string. Spacing is set to 1 by default but can be changed

`arrays.add_char(array, char, count, interval, rng)`:
- `array`: array you want to add a character in
- `char`: character you want to add 
- `count`: number of times you want to add character at each interval
- `interval`: interval at which you want to add characters
- `rng`: range in which you want to add characters 