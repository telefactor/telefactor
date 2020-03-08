# frozen_string_literal: true

require 'faraday-http-cache'
require 'octokit'

module Telefactor::RepoManagement
  class OktokitGateway
    extend Dry::Initializer

    option :client, default: proc { OktokitGateway.create_octokit_client }

    class << self
      def create_octokit_client
        stack =
          Faraday::RackBuilder.new do |builder|
            builder.use Faraday::HttpCache,
                        serializer: Marshal, shared_cache: false
            builder.use Octokit::Response::RaiseError
            builder.adapter Faraday.default_adapter
          end
        Octokit.middleware = stack

        Octokit::Client.new(
          access_token: Secrets.secrets.github.access_token, auto_paginate: true
        )
      end
    end

    def user
      client.user
    end

    def repos
      client.repositories
    end

    def create_repo(name)
      client.create_repository(
        name,
        private: true,
        description: "Telefactor: #{name}",
        auto_init: true
      )
    end
  end
end
