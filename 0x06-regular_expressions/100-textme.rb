#!/usr/bin/env ruby
sender = ARGV[0].scan(/\[[a-z]{4}:(.*?)\]/).join
receiver = ARGV[0].scan(/\[[a-z]{2}:(.*?)\]/).join
flags = ARGV[0].scan(/\[[a-z]{5}:(.*?)\]/).join
puts sender + "," + receiver + "," + flags
