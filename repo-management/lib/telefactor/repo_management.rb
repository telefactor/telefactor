# frozen_string_literal: true

require 'telefactor/repo_management/version'

module Telefactor
  module RepoManagement
    require 'faraday-http-cache'
    require 'octokit'

    class Manager
      class << self
        def create_octokit_client
          stack = Faraday::RackBuilder.new do |builder|
            builder.use Faraday::HttpCache, serializer: Marshal, shared_cache: false
            builder.use Octokit::Response::RaiseError
            builder.adapter Faraday.default_adapter
          end
          Octokit.middleware = stack

          Octokit::Client.new(access_token: Secrets.secrets.github.access_token)
        end
      end

      def user
        client.user
      end

      def repos
        client.repositories
      end

      def telefactor_repos
        repos.select do |repo|
          repo.name.match?(/fam/) && !repo.fork?
        end
      end

      def client
        @client ||=
          self.class.create_octokit_client.tap do |client_for_config|
            client_for_config.auto_paginate = true
          end
      end
    end

    module Secrets
      require 'dry-struct'
      require 'pathname'
      require 'safe_yaml'

      SafeYAML::OPTIONS[:default_mode] = :safe

      class << self
        def secrets
          @secrets ||= wrap_with_models(load_yaml_file)
        end

        def load_yaml_file
          SafeYAML.load_file('./config/secrets.yaml')
        end

        def wrap_with_models(secrets_hashes)
          puts secrets_hashes
          Models::Secrets.new(secrets_hashes)
        end
      end

      module Models
        Types = Dry.Types

        class BaseModel < Dry::Struct
          # throw an error when unknown keys provided
          schema schema.strict
          # convert string keys to symbols
          transform_keys(&:to_sym)
        end

        class GitHub < BaseModel
          attribute :access_token, Types::String
        end

        class Secrets < BaseModel
          attribute :github, GitHub
        end
      end
    end
  end
end
