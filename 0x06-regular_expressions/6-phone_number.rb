#!/usr/bin/env ruby
#This is a ruby regexp that match a 10 digit phone number
puts ARGV[0].scan(/^[0-9]{10}$/).join
