#!/usr/bin/env ruby
# Accet one argument from the man line
input = ARGV[0]
# define regular expression
regex = /hbt{1,4}n/
# Match regular expression with input
match = input.scan(regex)
#print match
puts match.join
