#!/usr/bin/env ruby

ALLOWED_CATEGORIES = %w[
  architecture
  editorial
  curriculum
  reference
  diagram
  resources
  domain
  ecosystem
  research
  governance
  tooling
  automation
  release
  docs
].freeze

message_path = ARGV.fetch(0) do
  warn "Usage: ruby scripts/git/check_commit_message.rb <message-file>"
  exit 1
end

subject = File.readlines(message_path, chomp: true).find do |line|
  !line.empty? && !line.start_with?("#")
end

if subject.nil?
  warn "Commit message must include a subject."
  exit 1
end

if subject.length > 72
  warn "Commit subject must be 72 characters or fewer."
  exit 1
end

category, summary = subject.split(": ", 2)

unless ALLOWED_CATEGORIES.include?(category) && summary&.match?(/\A[a-z].*[^.!?]\z/)
  warn "Commit subject must follow '<category>: <imperative summary>'."
  warn "Allowed categories: #{ALLOWED_CATEGORIES.join(", ")}."
  exit 1
end
