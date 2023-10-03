#!/usr/bin/env ruby
#See if an argumentis present

if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <log_file>"
  exit(1)
end

logfil_path = ARGV[0]

unless File.exist?(logfil_path)
  puts "File not found: #{logfil_path}"
  exit(1)
end

sender = ""
receiver = ""
flags = ""

File.open(logfil_path, "r") do |file|
  file.each_line do |line|
    if line =~ /from:\+*\w*/
      sender = line.scan(/from:\+*\w*/).join[5..-1]
    elsif line =~ /to:\+*\w*/
      receiver = line.scan(/to:\+*\w*/).join[3..-1]
    elsif line =~ /flags:(.*?)\]/
      flags = line.scan(/flags:(.*?)\]/).flatten.first
    end
  end
end

msg = "#{sender},#{receiver},#{flags}"
puts msg
