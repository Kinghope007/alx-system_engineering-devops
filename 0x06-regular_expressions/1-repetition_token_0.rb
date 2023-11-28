#!/usr/bin/env ruby
#Accept one argument from the command
input = ARGV[0]
# Define the regular expression 
regex = /hbt{2,5}n/
# Match the inout with the regex
match = input.scan(regex)
# Print aout matched result
puts match.join
