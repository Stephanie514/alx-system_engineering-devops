#!/usr/bin/env ruby
#See if there is an argument provided

if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <input_string>"
  exit(1)
end

input_string = ARGV[0]

matches = input_string.scan(/^h.n$/)

puts matches.join
