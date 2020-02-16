# frozen_string_literal: true

require 'tty-table'
require 'dry-initializer'

module Telefactor::RepoManagement
  class RepoDumper
    def dump(repos)
      rows =
        repos.map do |repo|
          CELL_CLASSES.map { |cell_class| cell_class.from_repo(repo).value }
        end

      rows.sort!

      table = TTY::Table.new(header: CELL_CLASSES.map(&:header), rows: rows)

      rendered_table = table.render_with(MarkdownBorder)

      puts(rendered_table)
    end

    class MarkdownBorder < TTY::Table::Border
      def_border do
        mid '-'
        mid_left '|'
        mid_mid '|'
        mid_right '|'

        left '|'
        center '|'
        right '|'
      end
    end

    class TableCell
      class << self
        def from_repo(repo)
          new(repo: repo)
        end

        def header
          raise 'ABC method not implemented'
        end
      end

      def intialize(*)
        raise 'ABC cannot be constructed'
      end

      def value
        raise 'ABC method not implemented'
      end
    end

    class Name < TableCell
      def self.header
        'Name'
      end

      attr_reader :value

      def initialize(repo:)
        @value = repo.name
      end
    end

    class URL < TableCell
      def self.header
        'URL'
      end

      attr_reader :value

      def initialize(repo:)
        @value = repo.url
      end
    end

    class Phase < TableCell
      def self.header
        'Phase'
      end

      attr_reader :value

      def initialize(repo:)
        @value = repo.phase
      end
    end

    class Role < TableCell
      def self.header
        'Role'
      end

      attr_reader :value

      def initialize(repo:)
        @value = repo.role
      end
    end

    CELL_CLASSES = [Phase, Role, Name, URL].freeze
  end
end
