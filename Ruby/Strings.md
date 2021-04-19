# Easy

## Ruby - Strings - Introduction

```ruby
def single_quote
  'Hello World and others!'
end

def double_quote
  "Hello World and others!"
end

def here_doc
    <<-EOM
  "Hello World and others!"
  EOM
end
```

## Ruby - Strings - Encoding

```ruby
def transcode(str)
    return str.force_encoding(Encoding::UTF_8)
end
```

## Ruby - Strings - Indexing

```ruby
def serial_average(input)
    x = input[4,5].to_f
    y = input[10,5].to_f
    return "#{input[0,3]}-#{((x+y)/2).round(2)}"
end
```

## Ruby - Strings - Iteration

```ruby
def count_multibyte_char(input)
    input.each_char.count {|x| x.bytesize > 1}
end
```

## Ruby - Strings - Methods I

```ruby
def process_text(arr)
    arr.map{|str| str.chomp.strip}.join(' ')
end
```

## Ruby - Strings - Methods II

```ruby
def strike(word)
    "<strike>#{word}</strike>"
end

def mask_article(string, words)
    words.map{|word| string.gsub!(word, strike(word))}
    return string
end
```