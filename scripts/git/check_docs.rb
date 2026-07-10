#!/usr/bin/env ruby

require "pathname"

ROOT = Pathname.new(File.expand_path("../..", __dir__))
MARKDOWN_LINK = /(?<!!)\[[^\]]+\]\(([^)\s]+)\)/

def staged_files
  `git diff --cached --name-only --diff-filter=ACMR`.lines.map(&:strip)
end

def valid_markdown_filename?(path)
  name = File.basename(path)
  return true if name == "README.md"

  name.match?(/\A[A-Z][A-Z0-9_.-]*(?:v[0-9]+(?:\.[0-9]+)*)?\.md\z/) ||
    name.match?(/\A[a-z0-9]+(?:-[a-z0-9]+)*\.md\z/)
end

files = (ARGV.empty? ? staged_files : ARGV).select do |path|
  path.end_with?(".md") && File.file?(ROOT.join(path))
end

errors = []

files.each do |path|
  absolute_path = ROOT.join(path)

  unless valid_markdown_filename?(path)
    errors << "#{path}: filename must use lowercase kebab-case or an established uppercase canonical name"
  end

  File.foreach(absolute_path).with_index(1) do |line, line_number|
    errors << "#{path}:#{line_number}: trailing whitespace" if line.match?(/[ \t]+\n\z/)
  end

  File.read(absolute_path).scan(MARKDOWN_LINK).flatten.each do |target|
    next if target.match?(%r{\A(?:https?:|mailto:|#)})

    relative_path = target.split("#", 2).first
    next if relative_path.empty?

    destination = absolute_path.dirname.join(relative_path).cleanpath
    errors << "#{path}: missing local link target #{target}" unless destination.exist?
  end
end

if errors.empty?
  puts "Documentation checks passed."
  exit 0
end

warn errors.join("\n")
exit 1
