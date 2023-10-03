#!/usr/bin/env ruby
# Are there arguments provided

if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <input_str>"
  exit(1)
end

input_str = ARGV[0]

matches = input_str.scan(/^\d{10}$/)

puts matches.join
