# Easy

## A Personalized Echo

```bash
read name
echo "Welcome "$name
```

## Comparing Numbers

```bash
read X
read Y

if [[ $X -gt $Y ]]
then
    echo "X is greater than Y "
elif [[ $Y -gt $X ]]
then
    echo "X is less than Y"
else
    echo "X is equal to Y"
fi
```

## Getting started with conditionals

```bash
read char
echo -e "YES\nNO" | grep -i $char
```

## Let's Echo

```bash
echo "HELLO"
```

## Looping and Skipping

```bash
for num in {1..99..2}
do
    echo $num
done
```

## Looping with Numbers

```bash
for num in {1..50}
do
    echo $num
done
```

## More on Conditionals

```bash
read A
read B
read C

if [ $A -eq $B ] || [ $B -eq $C ] || [ $A -eq $C ]
then
    if [ $A -eq $B ] && [ $B -eq $C ] && [ $A -eq $C ]
    then
        echo "EQUILATERAL"
    else
        echo "ISOSCELES"
    fi
else
    echo "SCALENE"
fi
```

## The World of Numbers

```bash
read X
read Y
echo $(($X + $Y))
echo $(($X - $Y))
echo $(($X * $Y))
echo $(($X / $Y))
```

# Medium

## Arithmetic Operations

```bash
read input
echo $input | bc -l | xargs printf "%.3f"
```

## Compute the Average

```bash
read n
arr=($(cat)) 
arr=${arr[*]}
echo $((${arr// /+}))/$n | bc -l | xargs printf "%.3f"
```

# Hard

## Functions and Fractals - Recursive Trees - Bash!

```bash
declare -A a

f() {
  local d=$1 l=$2 r=$3 c=$4
  [[ $d -eq 0 ]] && return
  for ((i=l; i; i--)); do
    a[$((r-i)).$c]=1
  done
  ((r -= l))
  for ((i=l; i; i--)); do
    a[$((r-i)).$((c-i))]=1
    a[$((r-i)).$((c+i))]=1
  done
  f $((d-1)) $((l/2)) $((r-l)) $((c-l))
  f $((d-1)) $((l/2)) $((r-l)) $((c+l))
}
read n
f $n 16 63 49
for ((i=0; i<63; i++)); do
  for ((j=0; j<100; j++)); do
    if [[ ${a[$i.$j]} ]]; then
      printf 1
    else
      printf _
    fi
  done
  echo
done
```