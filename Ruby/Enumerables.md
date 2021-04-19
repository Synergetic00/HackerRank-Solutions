# Medium

## Ruby - Enumerable - Introduction

```ruby
def iterate_colors(colors)
    arr = []
    colors.each{|color| arr.push(color)}
    return arr 
end
```

```ruby
def iterate_colors(colors)
    return colors.map{|color| color}
end
```

## Ruby - Enumerable - each_with_index

```ruby
def skip_animals(animals, skip)
    temp = []
    animals.each_with_index{|animal, i| temp.push("#{i}:#{animal}")}
    return temp.drop(skip)
end
```

## Ruby - Enumerable - collect

```ruby
def rot13(secret_messages)
    return secret_messages.map{|s| s.tr('A-Za-z','N-ZA-Mn-za-m')}
end
```

## Ruby - Enumerable - reduce

```ruby
def sum_terms(n)
  return (1..n).reduce(0) {|s, i| s + i * i + 1}
end
```

```ruby
def sum_terms(n)
  return (1..n).inject(0) {|s, i| s + i * i + 1}
end
```

## Ruby Enumerables: 'any', 'all', 'none', and 'find'

```ruby
def func_any(hash)
    hash.any? {|k, v| k.is_a?(Integer)}
end

def func_all(hash)
    hash.all? {|k, v| v.is_a?(Integer) && v < 10}
end

def func_none(hash)
    hash.none? {|k, v| v.nil?}
end

def func_find(hash)
    hash.find { |k, v| ([k, v].all?(Integer) && v < 20) || ([k, v].all?(String) && v.start_with?('a')) }
end
```

## Ruby - Enumerable - group_by

```ruby
def group_by_marks(marks, pass_marks)
   return marks.group_by {|k,v| v >= pass_marks ? "Passed" : "Failed"}
end
```