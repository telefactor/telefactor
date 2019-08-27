# frozen_string_literal: true

require 'faraday-http-cache'
require 'octokit'

module Telefactor::RepoManagement
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

    def fam_repos
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
end
