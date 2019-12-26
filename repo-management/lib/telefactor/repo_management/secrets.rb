# frozen_string_literal: true

require 'dry-struct'
require 'safe_yaml'

require 'telefactor/repo_management/types'

SafeYAML::OPTIONS[:default_mode] = :safe

module Telefactor::RepoManagement
  module Secrets
    class << self
      def secrets
        @secrets ||= wrap_with_structs(load_yaml_file)
      end

      def load_yaml_file
        SafeYAML.load_file('./config/secrets.yaml')
      end

      def wrap_with_structs(secrets_hashes)
        Structs::Secrets.new(secrets_hashes)
      end
    end

    module Structs
      class GitHub < Telefactor::RepoManagement::Types::Custom::StrictStruct
        attribute :access_token, Telefactor::RepoManagement::Types::String
      end

      class Secrets < Telefactor::RepoManagement::Types::Custom::StrictStruct
        attribute :github, GitHub
      end
    end
  end
end
