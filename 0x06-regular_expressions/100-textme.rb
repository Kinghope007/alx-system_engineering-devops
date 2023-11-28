#!/usr/bin/env ruby

# Accept the log entry as an argument from the command line
log_entry = ARGV[0]

# Define the regular expressions to extract sender, receiver, and flags
sender_regex = /\[from:([^\]]+)\]/
receiver_regex = /\[to:([^\]]+)\]/
flags_regex = /\[flags:([^\]]+)\]/

# Extract sender, receiver, and flags using regular expressions
sender = log_entry.match(sender_regex)&.captures&.first || ""
receiver = log_entry.match(receiver_regex)&.captures&.first || ""
flags = log_entry.match(flags_regex)&.captures&.first || ""

# Print the formatted result
puts "#{sender},#{receiver},#{flags}"
