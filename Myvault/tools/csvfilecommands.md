to veiw first line of file (header) and sed is used to replace , with \n so that each header is in diffent line while showing it does not affect file
head -n 1 UNBXD_en_US.csv | sed 's/,/\n/g'

to see first entry of csv file
tail -n +2 UNBXD_en_US.csv | head -n 1 | sed 's/;/\n/g'



tail and head 
### Using `tail` and `head`:

1. **Extract Lines Starting from the Second Line:** Use `tail` to skip the first line and then `head` to get only the second line.
    
    
    
    `tail -n +2 yourfile.txt | head -n 1`
    
    **Explanation:**
    
    - **`tail -n +2 yourfile.txt`**: This command outputs the file starting from the second line. `-n +2` means to start outputting from line 2 to the end.
    - **`head -n 1`**: This command then takes the first line from the output of `tail`, which effectively gives you the second line of the original file.

### Example:

Assume `yourfile.txt` contains:




`Header 
Second Line 
Third Line 
Fourth Line`


command
```
tail -n +2 yourfile.txt | head -n 1

```


Will output:
`Second Line`

### Summary:

- **`tail -n +2`** skips the first line of the file.
- **`head -n 1`** extracts the first line from the result of `tail`, which is the second line of the original file.

Let me know if you need more help with this or other commands!


