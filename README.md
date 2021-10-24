Array formatting library

`arrays.to_str(array, spacing=0)` returns 2D array as a string. Spacing is set to 0 by default but can be changed

`arrays.to_str3D(array, spacing)` returns 3D array as a string. Spacing is set to 1 by default but can be changed

`arrays.add_char(array, char, count, interval, rng)`:
- `array`: array you want to add a character in
- `char`: character you want to add 
- `count`: number of times you want to add character at each interval
- `interval`: interval at which you want to add characters
- `rng`: range in which you want to add characters 

`arrays.add_char_in_3D(array, char, count, interval, rng)`:
- `array`: 3D array that contains arrays you want to add character to
- `char`: charater you want to add
- `count`: number of characters you want to add at each interval
- `inteval [out_interval, inner_interval]`:
    - `out_interval` is the interval in the 3D array at which you pick 2D arrays to add characters to
    - `in_interval` is the interval at which you want to add characters in the 2D arrays
- `rng [out_rng, in_rng]`:
    - `out_rng List(int, int)`: is the range of 2D arrays in the 3D array that you want to add characters to 
    - `in_rng List(int, int)`: is the range inside each 2D array which you want to add character to.