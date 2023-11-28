#!/usr/bin/env ruby
# Accept argument from command line
input = ARGV[0]
# Define regular expression
regex = /^h.n$/
# match regular expression with the input
match = input.scan(regex)
# Print patch
puts match.join
