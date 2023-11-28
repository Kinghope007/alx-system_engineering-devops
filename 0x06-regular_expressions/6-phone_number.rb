#!/usr/bin/env ruby
# Accept the argument from command line
input = ARGV[0]
# Define regular expression
regex = /^[0-9]{10}$/
# MAtch regular expression with inpu
match = input.scan(regex)
# Print match
puts match.join
