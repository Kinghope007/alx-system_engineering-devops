#!/usr/bin/env ruby
# Accept one argument
input = ARGV[0]
# Define the regular expression
regex = /hb{,1}tn/
# match input with regular expression
match = input.scan(regex)
# print result
puts match.join
