# Easy

## Grep' - A

```bash
grep -i -w -E 'the|that|then|those'
```

## Grep' - B

```bash
grep '\([0-9]\) *\1'
```

## Sed' command #3

```bash
sed 's/thy/{&}/ig'
```

# Medium

## Awk' - 1

```bash
awk '$4=="" {print "Not all scores are available for " $1}'
```

## Awk' - 2

```bash
awk '{print $1, ":", ($2 < 50 || $3 < 50 || $4 < 50) ? "Fail" : "Pass"}'
```

## Awk' - 3

```bash
awk '{total = ($2 + $3 + $4)/3; grade = (total >= 80) ? "A" : (total >= 60) ? "B" : (total >= 50) ? "C" : "FAIL"; print $0, ":", grade }'
```

## Awk' - 4

```bash
awk 'ORS = NR % 2 ? ";" : "\n"'
```

## Grep' #1

```bash
grep -w the
```

## Grep' #2

```bash
grep -i -w the
```

## Grep' #3

```bash
grep -v -i -w that
```

## Sed' command #1

```bash
sed 's/\bthe\b/this/'
```

## Sed' command #2

```bash
sed 's/\bthy\b/your/ig'
```

# Hard

## Sed' command #4

```bash
sed 's/[0-9]\+ /**** /g'
```

## Sed' command #5

```bash
sed -r 's/(.+ )(.+ )(.+ )(....)/\4 \3\2\1/'
```