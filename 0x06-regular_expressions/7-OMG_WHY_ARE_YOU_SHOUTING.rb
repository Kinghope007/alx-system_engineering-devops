#!/usr/bin/env ruby
# Accept argument from command line
input = ARGV[0]
# Define regular expression
regex = /[A-Z]/
# Match regular expression with input
match = input.scan(regex)
#print the match
puts match.join
