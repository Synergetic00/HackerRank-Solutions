# Easy

## Blocks

```ruby

```

## Closures

```ruby

```

## Currying

```ruby

```

## Lambdas

```ruby

```

## Partial Applications

```ruby

```

## Procs

```ruby

```

## Ruby - Methods - Introduction

```ruby

```

## Ruby - Methods - Variable Arguments

```ruby
def full_name(first, *rest)
    rest.reduce(first) { |x,y| x + " " + y }
end
```

# Medium

## Lazy Evaluation

```ruby
require 'prime'

n = gets.to_i
p Prime.each.lazy.select{|x| x == x.to_s.reverse.to_i}.first(n)
```

## Ruby - Methods - Arguments

```ruby

```

## Ruby - Methods - Keyword Arguments

```ruby

```