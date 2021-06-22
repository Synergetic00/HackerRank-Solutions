# Easy

## Cut #1

```bash
while read line
do echo $line | cut -c 3
done
```

## Cut #2

```bash
while read line
do echo $line | cut -c 2,7
done
```

## Cut #3

```bash
while read line
do echo $line | cut -c 2-7
done
```

## Cut #4

```bash
while read line
do echo $line | cut -c -4
done
```

## Cut #5

```bash
while read line
do echo "$line" | cut -f -3
done
```

## Cut #6

```bash
while read line
do echo $line | cut -c 13-
done
```

## Cut #7

```bash
while read line
do echo $line | cut -d ' ' -f 4
done
```

## Cut #8

```bash
while read line
do echo $line | cut -d ' ' -f -3
done
```

## Cut #9

```bash
while read line
do echo "$line" | cut -f 2-
done
```

## Head of a Text File #1

```bash
head -n 20
```

## Head of a Text File #2

```bash
head -c 20
```

## Middle of a Text File

```bash
head -n 22 | tail -n +12
```

## Tail of a Text File #1

```bash
tail -n 20
```

## Tail of a Text File #2

```bash
tail -c 20
```

## Tr' Command #1

```bash
while read line
do echo $line | tr '()' '[]'
done
echo $line | tr '()' '[]'
```

## Tr' Command #2

```bash
while read line
do echo $line | tr -d a-z
done
```

## Tr' Command #3

```bash
while read line
do echo $line | tr '\t' ' '
done
```

## Sort Command #1

```bash
sort
```

## Sort Command #2

```bash
sort -r
```

## Sort Command #3

```bash
sort -n
```

## Sort Command #4

```bash
sort -n -r
```

## Sort Command #5

```bash
sort -t $'\t' -k 2 -r -n
```

## Sort' command #6

```bash
sort -t $'\t' -k 2 -n
```

## Sort' command #7

```bash
sort -t $'|' -k 2 -r -n
```

## Uniq' Command #1

```bash
uniq
```

## Uniq' Command #2

```bash
uniq -c | cut -c 7-
```

## Uniq' command #3

```bash
uniq -i -c | cut -c 7-
```

## Uniq' command #4

```bash
uniq -u
```

# Medium

## Paste - 1

```bash
paste -s -d ';'
```

## Paste - 2

```bash
paste -d ';' - - -
```

## Paste - 3

```bash
paste -s -d '\t'
```

## Paste - 4

```bash
paste -d '\t' - - -
```