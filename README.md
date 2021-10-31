Array formatting library

`arrays.to_str(array, spacing=0)` returns array as a string. Spacing is set to 0 by default but can be changed

`arrays.to_str2D(array, spacing)` returns 2D array as a string. Spacing is set to 1 by default but can be changed

`arrays.add_char(array, char, count, interval, rng)`:
- `array`: array you want to add a character in
- `char`: character you want to add 
- `count`: number of times you want to add character at each interval. Default is 1
- `interval`: interval at which you want to add characters. Default is 1
- `rng`: range in which you want to add characters. Default is `[0, len(array)]`

`arrays.add_char_in_2D(array, char, count, interval, in_rng, out_rng)`:
- `array`: 2D array that contains arrays you want to add character to
- `char`: charater you want to add
- `count`: number of characters you want to add at each interval. Default is 1
- `interval [out_interval, inner_interval]`: 
    - Default is `[1, 1]`
    - `out_interval` is the interval in the 2D array at which you pick 1D arrays to add characters to
    - `in_interval` is the interval at which you want to add characters in the 1D arrays
- `in_rng [start index, end index]`: is the range in the arrays inside the 2D array in which you want to add characters
    - Default value is `[0, len(array)]`
    - You can do `[2]` which takes 2 as starting index and end index is the default `len(array)`
- `out_rng [start index, end index]`: is the range in the outer 2D array in which you want to choose arrays to add character to
    - Default value is `[0, len(2D_array)`
    - You can do `[2]` which takes 2 as starting index and end index is the default `len(array)`