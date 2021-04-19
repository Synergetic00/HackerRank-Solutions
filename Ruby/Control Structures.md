# Easy

## Ruby Control Structures - Each

```ruby
def scoring(array)
    array.each do |user|
        user.update_score
    end
end
```

## Ruby Control Structures - Unless

```ruby
def scoring(array)
    array.each do |user|
        unless user.is_admin?
            user.update_score
        end
    end
end
```

## Ruby Control Structures - Infinite Loop

```ruby
loop do
    coder.practice
    break if coder.oh_one? == true
end
```

## Ruby Control Structures - Until

```ruby
until coder.oh_one? == true
    coder.practice
end
```

```ruby
while not coder.oh_one? == true
    coder.practice
end
```

```ruby
coder.practice until coder.oh_one? == true
```

# Medium

## Ruby Control Structures - Case (Bonus Question)

```ruby
def identify_class(obj)
    case obj
        when Hacker
            puts "It's a Hacker!"
        when Submission
            puts "It's a Submission!"
        when TestCase
            puts "It's a TestCase!"
        when Contest
            puts "It's a Contest!"
        else
            puts "It's an unknown model"
    end
end
```