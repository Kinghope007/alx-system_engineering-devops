#!/usr/bin/env ruby
# Accet one argument from the man line
input = ARGV[0]
# define regular expression
regex = /hb(t){1,4444}n/
# Match regular expression with input
match = input.scan(regex)
#print match
puts match.join
