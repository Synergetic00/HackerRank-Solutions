# Easy

## Matching Same Text Again & Again

`^([a-z]\w\s\W\d\D[A-Z][A-Za-z][AEIOUaeiou]\S)\1$`

## Backreferences To Failed Groups

`^\d\d(-?)\d\d\1\d\d\1\d\d$`

## Branch Reset Groups

`^\d\d(?|(-)|(:)|(\.)|(---))\d\d\1\d\d\1\d\d$`

## Forward References

`^(\2tic|(tac))+$`