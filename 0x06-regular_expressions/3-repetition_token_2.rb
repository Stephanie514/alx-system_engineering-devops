#!/usr/bin/env ruby
# If there is an arg given

if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <input_string>"
  exit(1)
end

input_string = ARGV[0]
matches = input_string.scan(/hbt+n/)
puts matches.join
