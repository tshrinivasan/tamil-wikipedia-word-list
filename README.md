Extract all words from tamil wikipedia dump.

Get the wikipedia dump from the following url
http://dumps.wikimedia.org/tawiki/latest/

tawiki-latest-pages-articles.xml.bz2   

extract it using the following command.

bunzip2  tawiki-latest-pages-articles.xml.tar.bz2




##### To remove all english charecters

```
tr  [:graph:]  ' ' < tawiki-latest-pages-articles.xml > all.tr
```


##### To remove all symbols

```
tr  "\012\015\041\042\043\044\045\046\047\050\051\053\054\055\056\057\060\061\062\06<200c><200b>3\064\065\066\067\070\071\073\074\075\076\077\100\101\102\103\104\105\106\107\110\<200c><200b>111\112\113\114\115\116\117\120\121\122\123\124\125\126\127\130\131\132\133\135\1<200c><200b>40\173\174\175" '\n' < all.tr > all.tr1
```

##### To remove leading spaces and blank lines
```
cat all.tr1 | sed -e 's/^[ \t]*//' | grep -v ^$ > all.trim
```




##### shell script to  seperate the words

```
cat line.sh 
#!/bin/bash 
for WORD in `cat all.trim` 
do 
    echo $WORD 
done 
```


Run the script
```
sh ./line.sh > words
```

##### Get unique tamil words
find_tamil.py script searches for only tamil words and stores the unique tamil words to the file 'only_uniq_tamil_words.txt'

```
python find_tamil.py 
```




##### count the number of words available

```
wc -l only_uniq_tamil_words.txt
1197913 only_uniq_tamil_words.txt
```


Now you can delete all the temporary files all.tr, all.tr1, all.trim, words and tawiki-latest-pages-articles.xml


##### sort the words

If you want to sort the words, run the below command.

```
sort only_uniq_tamil_words.txt > sorted_words.txt
```

This will sort the words and store in the file sorted_words.txt


