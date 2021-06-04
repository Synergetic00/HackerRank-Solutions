# Easy

## Ruby Array - Initialization

```ruby
array = []
array_1 = [nil]
array_2 = [10, 10]
```

```ruby
array = Array.new
array_1 = Array.new(1)
array_2 = Array.new(2, 10)
```

## Ruby Array - Index, Part 1


```ruby
def element_at(arr, index)
    return arr[index]
end
```

```ruby
def element_at(arr, index)
    return arr.at(index)
end

def inclusive_range(arr, start_pos, end_pos)
    return arr[start_pos..end_pos]
end

def non_inclusive_range(arr, start_pos, end_pos)
    return arr[start_pos...end_pos]
end

def start_and_length(arr, start_pos, length)
    return arr[start_pos,length]
end
```

## Ruby Array - Index, Part 2

```ruby
def neg_pos(arr, index)
    return arr[-index]
end

def first_element(arr)
    return arr.first
end

def last_element(arr)
    return arr.last
end

def first_n(arr, n)
    return arr.take(n)
end

def drop_n(arr, n)
    return arr.drop(n)
end
```

## Ruby Array - Addition

```ruby
def end_arr_add(arr, element)
    return arr.push(element)
end

def begin_arr_add(arr, element)
    return arr.unshift(element)
end

def index_arr_add(arr, index, element)
    return arr.insert(index, element)
end

def index_arr_multiple_add(arr, index)
    return arr.insert(index, nil, nil)
end
```

## Ruby Array - Deletion

```ruby
def end_arr_delete(arr)
    return arr.pop
end

def start_arr_delete(arr)
    return arr.shift

end

def delete_at_arr(arr, index)
    arr.delete_at(index)
end

def delete_all(arr, val)
    arr.delete(val)
end
```

## Ruby Array - Selection

```ruby
# select and return all odd numbers
def select_arr(arr)
    return arr.select {|x| x % 2 == 1}
end

# reject all elements which are divisible by 3
def reject_arr(arr)
    return arr.reject {|x| x % 3 == 0}
end

# delete all negative elements
def delete_arr(arr)
    return arr.delete_if {|x| x < 0}
end

# keep all non negative elements
def keep_arr(arr)
    return arr.keep_if {|x| x >= 0}
end
```

## Ruby Hash - Initialization

```ruby
empty_hash = Hash.new
default_hash = Hash.new(1)
hackerrank = {"simmy" => 100, "vivmbbs" => 200}
```

```ruby
empty_hash = {}

default_hash = {}
default_hash.default = 1

hackerrank = {}
hackerrank["simmy"] = 100
hackerrank["vivmbbs"] = 200
```

## Ruby Hash - Each

```ruby
def iter_hash(hash)
    hash.each do |k, v|
        puts k
        puts v
    end
end
```

## Ruby Hash - Addition, Deletion, Selection

```ruby
hackerrank.keep_if {|h, k| k.is_a? Integer}
hackerrank.delete_if {|h, k| k.even?}
hackerrank.store(543121, 100)
```