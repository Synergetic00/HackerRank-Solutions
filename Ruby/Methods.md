# Easy

## Blocks

```ruby
def factorial
    yield
end

n = gets.to_i
factorial do
    puts (1..n).reduce(1) {|s, i| s * i}
end
```

## Closures

```ruby
def block_message_printer
    message = "Welcome to Block Message Printer"
    if block_given?
        yield # Called
    end
  puts "But in this function/method message is :: #{message}"
end

message = gets
block_message_printer { puts "This message remembers message :: #{message}" }

# Proc

def proc_message_printer(my_proc)
    message = "Welcome to Proc Message Printer"
    my_proc.call() # Called
    puts "But in this function/method message is :: #{message}"
end


my_proc = proc { puts "This message remembers message :: #{message}" }
proc_message_printer(my_proc)

# Lambda

def lambda_message_printer(my_lambda)
    message = "Welcome to Lambda Message Printer"
    my_lambda.call # Called
    puts "But in this function/method message is :: #{message}"
end

my_lambda = -> { puts "This message remembers message :: #{message}" }
lambda_message_printer(my_lambda)
```

## Currying

```ruby
power_function = -> (x, z) {
    (x) ** z
}

base = gets.to_i
raise_to_power = power_function.curry.(base)

power = gets.to_i
puts raise_to_power.(power)
```

## Lambdas

```ruby
square      = ->(x) {x * x}

plus_one    = ->(x) {x + 1}

into_2      = ->(x) {x * 2}

adder       = ->(x, y) {x + y}

values_only = ->(h) {h.values}


input_number_1 = gets.to_i
input_number_2 = gets.to_i
input_hash = eval(gets)

a = square.(input_number_1); b = plus_one.(input_number_2);c = into_2.(input_number_1);
d = adder.(input_number_1, input_number_2);e = values_only.(input_hash)

p a; p b; p c; p d; p e
```

## Partial Applications

```ruby
combination = ->(n) do
    ->(r) do
        fact(n) / (fact(r) * fact(n-r))
    end
end

def fact(v)
    return (1..v).reduce(1) {|v, i| v * i}
end

n = gets.to_i
r = gets.to_i
nCr = combination.(n)
puts nCr.(r)
```

## Procs

```ruby
def square_of_sum (my_array, proc_square, proc_sum)
    sum = proc_sum.call(my_array)
    proc_square.call(sum)
end

proc_square_number = proc {|x| x * x}
proc_sum_array     = proc {|a| a.sum}
my_array = gets.split().map(&:to_i)

puts square_of_sum(my_array, proc_square_number, proc_sum_array)
```

## Ruby - Methods - Introduction

```ruby
def prime?(arg)
    Prime.prime?(arg)
end
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
def take(arr, num)
    arr.delete_if {|x| arr.index(x) < num}
end
```

## Ruby - Methods - Keyword Arguments

```ruby
def convert_temp(temp, input_scale:, output_scale:)
    input = input_scale[0]
    output = output_scale[0]

    val = temp.to_f
    res = 0

    # to celcius
    case input
        when "k"
            res = val - 273.15
        when "f"
            res = (val - 32) * (5/9.0);
    end

    #from celcius
    case output
        when "k"
            res = res + 273.15
        when "f"
            res = (res / (9/5.0)) + 32;
    end

    return res
end
```