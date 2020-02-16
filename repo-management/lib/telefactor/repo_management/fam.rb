# frozen_string_literal: true

require 'dry-initializer'

require 'telefactor/repo_management/oktokit_gateway'
require 'telefactor/repo_management/types'

module Telefactor::RepoManagement
  class Fam
    extend Dry::Initializer

    option :oktokit_gateway, default: proc { OktokitGateway.new }

    class << self
      def resources_to_repos(resources)
        repo_name_schema_regexp = /(?<game>telefactor-fam)-(?<role>examiner|sourcerer)-(?<phase>\w*)/
        resources.map do |resource|
          name_captures =
            repo_name_schema_regexp
            .match(resource[:name])
            &.named_captures || {}

          Repo.new(
            name: resource[:name],
            url: resource[:html_url],
            phase: name_captures.fetch('phase', -1),
            role: name_captures.fetch('role', Roles::GM)
          )
        end
      end
    end

    def repos
      @repos ||= self.class.resources_to_repos(fetch_repo_resources)
    end

    def fetch_repo_resources
      oktokit_gateway.repos.select do |resource|
        resource[:name].match?(/fam/) && !resource[:fork]
      end
    end

    class Roles
      EXAMINER = 'examiner'
      GM = 'gm'
      SOURCERER = 'sourcerer'

      def self.members
        {
          'EXAMINER' => EXAMINER,
          'GM' => GM,
          'SOURCERER' => SOURCERER
        }.freeze
      end
    end

    class Phases
      def self.members
        {
          -1  => ''  ,
          0  => 'zero'  ,
          1  => 'one'   ,
          2  => 'two'   ,
          3  => 'three' ,
          4  => 'four'  ,
          5  => 'five'  ,
          6  => 'six'   ,
          7  => 'seven' ,
          8  => 'eight' ,
          9  => 'nine'  ,
          10 => 'ten'   ,
        }.freeze
      end
    end

    class Repo < Types::Custom::StrictStruct
      ##
      # Core resource fields:
      attribute :name, Types::Strict::String
      attribute :url, Types::Strict::String

      ##
      # Telefactor fields:
      attribute :phase, Types::Coercible::Integer.enum(Phases.members)
      attribute :role, Types::Strict::String.enum(Roles.members)
    end
  end
end
