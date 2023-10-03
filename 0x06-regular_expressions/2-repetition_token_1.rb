#!/usr/bin/env ruby
# Check if there is an argument provided

if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <input_string>"
  exit(1)
end

input_string = ARGV[0]

pattern = /hb?t?n/
matches = input_string.scan(pattern)

result = matches.join
puts result
