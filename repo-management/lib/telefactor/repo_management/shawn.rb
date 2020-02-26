# frozen_string_literal: true

require 'dry-initializer'

require 'telefactor/repo_management/oktokit_gateway'
require 'telefactor/repo_management/types'

module Telefactor::RepoManagement
  class Shawn
    extend Dry::Initializer

    REPO_NAME_SCHEMA_REGEXP = /(?<game>shawn)-(?<phase>\d+)/.freeze

    option :repos, default: proc { nil }
    option :oktokit_gateway, default: proc { OktokitGateway.new }

    class << self
      def resources_to_repos(resources)
        resources.map do |resource|
          name_captures =
            REPO_NAME_SCHEMA_REGEXP.match(resource[:name])&.named_captures || {}

          Repo.new(
            name: resource[:name],
            url: resource[:html_url],
            phase: name_captures.fetch('phase')
          )
        end
      end
    end

    def repos
      @repos ||= self.class.resources_to_repos(fetch_repo_resources)
    end

    def latest_phase
      repos.max_by(&:phase)
    end

    private 

    def fetch_repo_resources
      oktokit_gateway.repos.select do |resource|
        resource[:name].match?(REPO_NAME_SCHEMA_REGEXP) && !resource[:fork]
      end
    end

    class Roles
      EXAMINER = 'examiner'
      GM = 'gm'
      SOURCERER = 'sourcerer'

      def self.members
        { 'EXAMINER' => EXAMINER, 'GM' => GM, 'SOURCERER' => SOURCERER }.freeze
      end
    end

    class Repo < Types::Custom::StrictStruct
      ##
      # Core resource fields:
      attribute :name, Types::Strict::String
      attribute :url, Types::Strict::String

      ##
      # Telefactor fields:
      attribute :phase, Types::Coercible::Integer

      def role
        if phase.zero?
          Roles::GM
        elsif phase.odd?
          Roles::EXAMINER
        elsif phase.even?
          Roles::SOURCERER
        end
      end
    end
  end
end
