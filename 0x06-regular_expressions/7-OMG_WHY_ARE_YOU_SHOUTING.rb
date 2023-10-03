#!/usr/bin/env ruby
# Check if there is an argument provided

if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <input_str>"
  exit(1)
end

input_str = ARGV[0]

caps_letter_pat = /[A-Z]/
matches = input_str.scan(caps_letter_pat)

caps_letters = matches.join
puts caps_letters
