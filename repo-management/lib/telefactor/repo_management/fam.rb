# frozen_string_literal: true

require 'dry-initializer'

require 'telefactor/repo_management/oktokit_gateway'

module Telefactor::RepoManagement
  class Fam
    extend Dry::Initializer

    option :oktokit_gateway, default: proc { OktokitGateway.new }

    def repos
      @repos ||=
        oktokit_gateway.repos.select do |repo|
          repo.name.match?(/fam/) && !repo.fork?
        end
    end
  end
end
