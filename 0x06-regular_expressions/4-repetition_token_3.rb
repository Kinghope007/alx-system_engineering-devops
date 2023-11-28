#!/usr/bin/env ruby
#  Accept argument from command
input = ARGV[0]
# Define regular expression 
regex = /hbt{,4}n/
# Match regular expression with input
match = input.scan(regex)
# Print the match
puts match.join
