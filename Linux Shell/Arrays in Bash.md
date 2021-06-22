# Easy

## Concatenate an array with itself

```bash
arr=($(cat))
carr=(${arr[@]} ${arr[@]} ${arr[@]})
echo ${carr[@]}
```

## Count the number of elements in an Array

```bash
arr=($(cat))
echo ${#arr[@]}
```

## Display an element of an array

```bash
arr=($(cat))
echo ${arr[3]}
```

## Read in an Array

```bash
arr=($(cat))
echo ${arr[@]}
```

## Slice an Array

```bash
arr=($(cat))
echo ${arr[@]} | cut -d ' ' -f 4-8
```

# Medium

## Filter an Array with Patterns

```bash
arr=($(cat))
echo ${arr[@]/*[aA]*/}
```

## Remove the First Capital Letter from Each Element

```bash
arr=($(cat))
echo ${arr[@]/[A-Z]/\.}
```

# Hard

## Lonely Integer - Bash!

```bash
read
echo $((`tr ' ' '^'`))
```