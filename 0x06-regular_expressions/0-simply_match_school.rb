#!/usr/bin/env ruby
# Accept one argument from commnand line
input = ARGV[0]
# Define the regular expression
regex = /School/
# Use the regular expression to matcg the input
match = input.scan(regex)
# Print the result
puts match.join
